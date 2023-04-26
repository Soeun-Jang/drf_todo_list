from django.urls import path
from users import views



urlpatterns = [
    path('signup/', views.SignupView.as_view(), name='signupview'),
    path('login/', views.CustomTokenObtainPairView.as_view(), name='signupview'),
    path('<int:id>/', views.UserView.as_view(), name='userview')
]
