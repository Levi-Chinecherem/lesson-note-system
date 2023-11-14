# account/urls.py

from django.urls import path
from .views import CustomLoginView, CustomLogoutView, CustomSignupView, CustomPasswordChangeView, CustomPasswordChangeDoneView

app_name = 'account'

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('signup/', CustomSignupView.as_view(), name='signup'),
    path('password-change/', CustomPasswordChangeView.as_view(), name='password_change'),
    path('password-change-done/', CustomPasswordChangeDoneView.as_view(), name='password_change_done'),
    # Add more patterns as needed
]
