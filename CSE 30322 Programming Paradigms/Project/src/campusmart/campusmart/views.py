from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import transaction
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Listing, ListingCounter, Message, User, PurchasedListingCounter
from .forms import ListingForm, ListingImageFormSet
from .forms import MessageForm
import requests

# Dsiplays your listings that you have
@login_required
def listings_mine(request):
    listings = Listing.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'listings_mine.html', {'listings': listings})

# Allows you to create a listing
@login_required
def create_listing(request):
    counter, created = ListingCounter.objects.get_or_create(user=request.user)
    purchased_counter, created = PurchasedListingCounter.objects.get_or_create(user=request.user)
    print(purchased_counter.can_post())
    print(counter.can_post_free())
    # Check if user can post for free
    using_purchase = False
    if not counter.can_post_free() and not purchased_counter.can_post():
        return redirect('purchase_listings')  # TODO: FEATURE 4
    if not counter.can_post_free() and purchased_counter.can_post():
        using_purchase = True
    # On post request, save everything to db
    if request.method == 'POST':
        if not request.FILES:
            form = ListingForm()
            formset = ListingImageFormSet(instance=Listing())
            return render(request, 'listing_form.html', {
                'daily': 3-counter.daily_count,
                'purchased': purchased_counter.extra_posts,
                'form': form,
                'formset': formset,
                'is_creating': True,
                'image_error': True
            })
        form = ListingForm(request.POST)
        print(request.FILES)

        formset = ListingImageFormSet(request.POST, request.FILES, instance=Listing())
        
        if form.is_valid() and formset.is_valid():
            with transaction.atomic():
                listing = form.save(commit=False)
                listing.user = request.user
                listing.save()
                
                # save the image formset
                formset.instance = listing
                formset.save()
                
                # increment the user's daily post count
                if using_purchase:
                    purchased_counter.decrement_count()
                else:
                    counter.increment_count()
                
                messages.success(request, "Listing created successfully!")
                return redirect('listing_detail', pk=listing.pk)
    else:
        form = ListingForm()
        formset = ListingImageFormSet(instance=Listing())
    
    return render(request, 'listing_form.html', {
        'daily': 3-counter.daily_count,
        'purchased': purchased_counter.extra_posts,
        'form': form,
        'formset': formset,
        'is_creating': True,
        'image_error': False
    })

# Allows you to update a listing
@login_required
def update_listing(request, pk):
    listing = get_object_or_404(Listing, pk=pk, user=request.user)
    
    if request.method == 'POST':
        form = ListingForm(request.POST, instance=listing)
        formset = ListingImageFormSet(request.POST, request.FILES, instance=listing)
        
        if form.is_valid() and formset.is_valid():
            with transaction.atomic():
                form.save()
                formset.save()
                messages.success(request, "Listing updated successfully!")
                return redirect('listing_detail', pk=listing.pk)
    else:
        form = ListingForm(instance=listing)
        formset = ListingImageFormSet(instance=listing)
    
    return render(request, 'listing_form.html', {
        'form': form,
        'formset': formset,
        'listing': listing,
        'is_creating': False,
        'image_error': False
    })

@login_required
def listing_detail(request, pk):
    listing = get_object_or_404(Listing, pk=pk)
    # Return a different page based on whether the owner or someone else is viewing the listing
    if listing.user == request.user:
        template_name = 'listing_detail.html'
    else:
        template_name = 'listing_detail_with_messaging.html'
    
    return render(request, template_name, {'listing': listing})


@login_required
def toggle_listing_status(request, pk):
    listing = get_object_or_404(Listing, pk=pk, user=request.user)
    
    if listing.status == 'AVAILABLE':
        listing.status = 'UNAVAILABLE'
    else:
        listing.status = 'AVAILABLE'
    
    listing.save()
    messages.success(request, f"Listing marked as {listing.get_status_display()}.")
    return redirect('listing_detail', pk=listing.pk)

@login_required
def delete_listing(request, pk):
    try:
        listing = Listing.objects.get(pk=pk, user=request.user)
    except Listing.DoesNotExist:
        return redirect('listings_mine')
    
    if request.method == 'POST':
        listing.delete()
        messages.success(request, "Listing deleted successfully!")
        return redirect('listings_mine')
    
    return render(request, 'confirm_delete.html', {'listing': listing})

# Feature 4
# get request sends form w/ balance. Makes call to api to get balance.
# post request sends pay call to api
@login_required
def purchase_listings(request):
    access_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzU0MzQ1NzIzLCJpYXQiOjE3NDU3MDU3MjMsImp0aSI6ImNkNGY5M2ZhYjMwYzQ4MDJiMTQ1MzJmMDc3N2I2MGZmIiwidXNlcl9pZCI6ODB9.a2Njx9XueZ0exvNj30DELtcSfFJsQmYrgfxldmZzeO4"
    email = request.user.email

    if request.method == "POST":
        purchase_number = int(request.POST.get('purchase_number'))
        payment_success = user_pay(access_token,email,purchase_number)
        print(purchase_number)
        print("pay")
        print(payment_success)
        if not payment_success:
            balance = view_balance_for_user(access_token, email)
            balance = balance['amount'] if balance else 0
            return render(request, 'purchase_listings.html', {
                'balance': balance,
                'error': 'Insufficient funds.'
            })
        user = User.objects.get(id=request.user.id)

        # Check if a PurchasedListingCounter already exists for this user
        listing_counter, created = PurchasedListingCounter.objects.get_or_create(user=user)

        # If it exists, update the extra_posts count, otherwise create a new instance
        listing_counter.extra_posts += purchase_number
        listing_counter.save()
        return redirect('listings_mine')

    balance = view_balance_for_user(access_token, email)
    balance = balance['amount'] if balance else 0
    purchased_counter, created = PurchasedListingCounter.objects.get_or_create(user=request.user)
    return render(request, 'purchase_listings.html', {
        'balance': balance,
        'purchased': purchased_counter.extra_posts,
    })

def view_balance_for_user(access_token, email):
    headers = {'Authorization': f'Bearer {access_token}'}
    api_response = requests.get(f"https://jcssantos.pythonanywhere.com/api/group2/group2/player/{email}/", headers=headers)

    if api_response.status_code == 200:
       return api_response.json()
    else:
       print("Failed to access the API endpoint to view balance for user:", api_response.status_code)

def user_pay(access_token, email, amount):
   # Use the access token to make an authenticated request
   headers = {
       'Authorization': f'Bearer {access_token}'
   }
   data = {"amount": amount} # non-negative integer value to be decreased
   # Make a POST request with the authorization header and data payload
   api_response = requests.post(f"https://jcssantos.pythonanywhere.com/api/group2/group2/player/{email}/pay", headers=headers, data=data)


   if api_response.status_code == 200:
       # Process the data from the API
       return api_response.json()
   else:
       print("Failed to access the API endpoint to pay:", api_response.status_code)

# 3.1 and 3.2 Browse listings and search
@login_required
def browse_listings(request):
    query = request.GET.get('q', '')
    listings = Listing.objects.filter(status='AVAILABLE').exclude(user=request.user).order_by('-created_at')
    # Search if the user types in the search bar and enters
    if query:
        listings = listings.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query)
        )

    # Display 20 items at a time
    paginator = Paginator(listings, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'listings': page_obj, 'query': query}

    return render(request, 'browse_listings.html', context)


# Allows the user to send and receive messages
@login_required
def send_message(request, listing_id):
    listing = get_object_or_404(Listing, id=listing_id)
    if request.method == 'POST':
        # validate the message, and send to db
        form = MessageForm(request.POST)
        if form.is_valid():
            new_message = form.save(commit=False)
            new_message.sender = request.user
            new_message.recipient = listing.user
            new_message.listing = listing
            new_message.save()
            
            messages.success(request, "Message sent!")
            return redirect('listing_detail', pk=listing_id)
    else:
        form = MessageForm()
    
    return render(request, 'send_message.html', {'form': form,'listing': listing})

@login_required
def inbox(request):
    user_messages = request.user.received_messages.select_related('sender', 'listing')
    return render(request, 'inbox.html', {'messages': user_messages})

@login_required
def view_message(request, message_id):
    # If the message does not exist OR user is not right, sends back to inbox.
    try:
        message_obj = Message.objects.get(id=message_id, recipient=request.user)
    except Message.DoesNotExist:
        return redirect('inbox')
    return render(request, 'view_message.html', {'message': message_obj})

def custom_404_redirect(request, exception):
    return redirect('home')