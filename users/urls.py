from django.urls import path
from users import views


urlpatterns = [
    path('signup/', views.SignupView.as_view(), name='signupview'),
    path('login/', views.CustomToekonObtainPairView.as_view(), name='signupview')
]
