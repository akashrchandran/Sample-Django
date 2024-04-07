from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('upload/', views.upload_file, name='upload_file'),
    path('download/<int:pk>/', views.download_file, name='download_file'),
    path('add/', views.add, name='add'),
    path('subtract/', views.subtract, name='subtract'),
    path('multiply/', views.multiply, name='multiply'),
    path('divide/', views.divide, name='divide'),
]