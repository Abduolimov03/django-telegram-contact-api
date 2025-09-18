from django.urls import path
from .views import ContactApiView

urlpatterns = [
    path('api/contact/', ContactApiView.as_view())
]