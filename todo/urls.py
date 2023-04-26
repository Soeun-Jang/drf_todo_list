from django.urls import path
from todo import views


urlpatterns = [
    path('', views.TodoListView.as_view(), name='todolistview'),
    path('<int:id>/', views.TodoDetailView.as_view(), name='tododetailview')
]

