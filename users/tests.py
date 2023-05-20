from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase
from users.models import User

class UserRegistrationAPIViewTestCase(APITestCase):
    def test_registration(self):
        url = reverse("signupview")
        user_data = {
            "email" : "test00@test.com",
            "username" : "testz",
            "age" : 15,
            "gender" : "Female",
            "introduction" : "hihihi",
            "password" : "xptmxm123@456"
        }
        response =self.client.post(url, user_data)
        self.assertEqual(response.status_code, 201)

    # def test_login(self):
    #     url = reverse("signinview")
    #     user_data = {
    #         "email" : "test00@test.com",
    #         "username" : "testz",
    #         "age" : 15,
    #         "gender" : "Female",
    #         "introduction" : "hihihi",
    #         "password" : "xptmxm123@456"
    #     }
    #     response =self.client.post(url, user_data)
    #     print(response.data)
    #     self.assertEqual(response.status_code, 200)

class LoginUserTest(APITestCase):
    def setUp(self):
        self.data = {
            'email': 'sogummi@test.com',
            'password':'test123',
            'username':'sogummi'
          }
        self.user = User.objects.create_user(**self.data)
    def test_login(self):
        response = self.client.post(reverse('signinview'), self.data)
        self.assertEqual(response.status_code, 200)
    
    def test_get_user_data(self):
        access_token = self.client.post(reverse('signinview'), self.data).data['access']
        response = self.client.get(
          path=reverse('userview', args=[self.user.id]),
          HTTP_AUTHORIZATION = f"Bearer {access_token}"
        )
        print(response.data)
        # self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['username'], self.data['username'])