from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/',views.ProfileView.as_view(),name = 'oneuser'),
    path('login/',views.LoginView.as_view(),name='login'),
    path('register/',views.RegisterView.as_view(),name='register'),
    path('password-reset/',views.RequestPasswordResetView.as_view(),name='passwordreset'),
    path('password-reset-confirm/',views.PasswordResetConfirmView.as_view(),name='passwordresetconfirm'),
    path('change-password/',views.ChangePasswordView.as_view(),name='changepassword')

]
