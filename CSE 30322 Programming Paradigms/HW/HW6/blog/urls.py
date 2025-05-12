from django.urls import path

from . import views
app_name = 'blog'  # creates a namespace for this app
urlpatterns = [
    path('',views.IndexView.as_view(), name='blogs'), 
    path('<int:pk>/', views.BlogDetailView.as_view(), name='blogpost'), 
]
