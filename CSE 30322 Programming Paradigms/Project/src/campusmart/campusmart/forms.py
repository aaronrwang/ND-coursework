from django import forms
from .models import Listing, ListingImage, Message

# Form for the listings (nneds a title and description)
class ListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = ['title', 'description', 'price', 'condition']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }
    
    def clean_title(self):
        title = self.cleaned_data.get('title')
        if not title:
            raise forms.ValidationError("Title cannot be empty.")
        return title
    
    def clean_description(self):
        description = self.cleaned_data.get('description')
        if not description:
            raise forms.ValidationError("Description cannot be empty.")
        return description

class ListingImageForm(forms.ModelForm):
    class Meta:
        model = ListingImage
        fields = ['image']
    
    image = forms.ImageField(label='Image')

# For multiple images
ListingImageFormSet = forms.inlineformset_factory(
    Listing, ListingImage, form=ListingImageForm, extra=1, can_delete=True
)

# For the messages
class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['subject', 'body']
