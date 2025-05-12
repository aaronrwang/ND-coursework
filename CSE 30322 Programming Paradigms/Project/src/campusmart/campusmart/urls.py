"""
URL configuration for campusmart project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from . import views


urlpatterns = [ #different pages for the different links
    # default admin
    path('admin/', admin.site.urls),

    # send to accounts app to deal with log in.
    path('accounts/', include('accounts.urls')), # App to handle login stuff

    # Home page; does not do anything just says home page.
    path('', TemplateView.as_view(template_name='home.html'), name='home'),

    # 2.1
    path('listings/mine/', views.listings_mine, name='listings_mine'),

    path('listings/new/', views.create_listing, name='create_listing'),
    path('listings/<int:pk>/', views.listing_detail, name='listing_detail'),

    # POST APIS
    # 2.2
    path('listings/<int:pk>/edit/', views.update_listing, name='update_listing'),
    path('listings/<int:pk>/toggle-status/', views.toggle_listing_status, name='toggle_listing_status'),

    # 2.3
    path('listings/<int:pk>/delete/', views.delete_listing, name='delete_listing'),

    # TODO: to be fully implemented in 4.1
    path('purchase-listings/', views.purchase_listings, name='purchase_listings'),

    # 3.1 and 3.2
    path('listings/browse/', views.browse_listings, name='browse_listings'), 

    # 3.3
    path('listings/<int:listing_id>/send-message/', views.send_message, name='send_message'), 
    path('messages/inbox/', views.inbox, name='inbox'),
    path('messages/<int:message_id>/', views.view_message, name='view_message'),
]

# safety clause. when trying to access smth that doesnt exist redirect.
# this only works when debug = False, but pictures dont work.
# handler404 = 'campusmart.views.custom_404_redirect'

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)