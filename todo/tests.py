from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from users.models import User
from faker import Faker
from .models import TodoArticle
from .serializers import TodoSerializer



class ArticleCreateTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.data = {
            'email': 'sogummi@test.com',
            'password':'test123',
            'username':'sogummi'
          }
        cls.article_data = {'title':'testtitle'}
        cls.user = User.objects.create_user(**cls.data)
  
    def setUp(self):
        self.access_token = self.client.post(reverse('signinview'), self.data).data['access']

    def test_fail_if_not_loggied_in(self):
        url = reverse("todolistview")
        response = self.client.post(url, self.article_data)
        self.assertEqual(response.status_code, 401)
        
    def test_create_article(self):
        response = self.client.post(
          path=reverse("todolistview"),
          data = self.article_data,
          HTTP_AUTHORIZATION = f"Bearer {self.access_token}"
          )
        self.assertEqual(response.status_code, 201)


class ArticleReadTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.faker = Faker()
        cls.articles = []
        for i in range(10):
            cls.user = User.objects.create_user(cls.faker.email(), cls.faker.password())
            cls.articles.append(TodoArticle.objects.create(title=cls.faker.sentence(), user=cls.user))

    def test_get_todoarticle(self):
        for article in self.articles:
            url = article.get_absolute_url()
            response = self.client.get(url)
            serializer = TodoSerializer(article).data
            for key, value in serializer.items():
                self.assertEqual(response.data[key], value)
                print(key, value)