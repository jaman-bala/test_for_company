from django.urls import path
from .views import AdvertList, AdvertDetail

urlpatterns = [
    path('api/advert-list/', AdvertList.as_view()),
    path('api/advert/<int:pk>/', AdvertDetail.as_view()),
]
