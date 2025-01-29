from django.urls import path
from .views import BücherAPIView

urlpatterns = [
    path('bücher/',BücherAPIView.as_view() ),

]