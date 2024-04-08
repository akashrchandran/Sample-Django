from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from .views import (AddView, DivideView, DownloadFileView, LoginView,
                    MultiplyView, RegisterView, SubtractView, UploadFileView)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('upload/', UploadFileView.as_view(), name='upload_file'),
    path('download/<int:pk>/', DownloadFileView.as_view(), name='download_file'),
    path('add/', AddView.as_view(), name='add'),
    path('subtract/', SubtractView.as_view(), name='subtract'),
    path('multiply/', MultiplyView.as_view(), name='multiply'),
    path('divide/', DivideView.as_view(), name='divide'),
]