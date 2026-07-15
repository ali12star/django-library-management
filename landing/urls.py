from django.urls import path
from .views import contact_view , home_view , book_detail_view

app_name = 'landing'

urlpatterns = [
    path('contact/', contact_view),
    path('' , home_view , name='home'),
    path('book/<int:book_id>/', book_detail_view)
]