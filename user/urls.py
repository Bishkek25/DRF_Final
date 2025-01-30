from . import views
from django.urls import path

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.LoginAPIView.as_view(), name='login'),
    path('confirm/', views.SNSCodeConfirm.as_view(), name='logout'),
]