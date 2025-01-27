from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('directors/', views.DirectorListAPIView.as_view(), name='directors-list'),
    path('directors/<int:id>/', views.DirectorDetailAPIView.as_view(), name='directors-detail'),
    path('movies/', views.MovieListAPIView.as_view(), name='movies-list'),
    path('movies/<int:id>/', views.MovieDetailAPIView.as_view(), name='movies-detail'),
    path('reviews/', views.ReviewListAPIView.as_view(), name='review-list'),
    path('reviews/<int:id>/', views.ReviewDetailAPIView.as_view(), name='review-detail'),
]
