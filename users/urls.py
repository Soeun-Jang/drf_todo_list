from django.urls import path
from users import views


urlpatterns = [
    path('', views.SignupView.as_view(), name='signupview')
]
