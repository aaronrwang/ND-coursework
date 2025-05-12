from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

#models for the different market item description choices
class Listing(models.Model):
    CONDITION_CHOICES = [
        ('NEW', 'New'),
        ('LIKE_NEW', 'Like New'),
        ('USED', 'Used'),
        ('FAIR', 'Fair'),
    ]
    
    STATUS_CHOICES = [
        ('AVAILABLE', 'Available'),
        ('UNAVAILABLE', 'Unavailable'),
    ]
    
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    condition = models.CharField(max_length=10, choices=CONDITION_CHOICES)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='AVAILABLE')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='listings')
    
    def __str__(self):
        return self.title
    
class ListingImage(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='listing_images/')
    
    def __str__(self):
        return f"Image for {self.listing.title}"

# For tracking daily posts
class ListingCounter(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    count_date = models.DateField(default=timezone.now)
    daily_count = models.IntegerField(default=0)
    
    def __str__(self):
        return f"{self.user.username}'s listing count for {self.count_date}"
    
    def reset_if_new_day(self):
        today = timezone.now().date()
        if self.count_date != today:
            self.count_date = today
            self.daily_count = 0
            self.save()
    
    def increment_count(self):
        self.reset_if_new_day()
        self.daily_count += 1
        self.save()
    
    def can_post_free(self):
        self.reset_if_new_day()
        return self.daily_count < 3

# For tracking purchased extra posts.
class PurchasedListingCounter(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    extra_posts = models.IntegerField(default=0)

    def can_post(self):
        return self.extra_posts >= 1

    def decrement_count(self):
        self.extra_posts -= 1
        self.save()
    
# Model to send messages to users about their posts
class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name='messages')
    subject = models.CharField(max_length=1000)
    body = models.TextField()
