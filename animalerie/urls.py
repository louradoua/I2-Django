from django.urls import path
from . import views

urlpatterns = [
    path('posts', views.post_list, name='post_list'),
    path('', views.animal_list, name='animal_list'),
    path('animal/<str:id_animal>/', views.animal_detail, name='animal_detail'),
    path('animal/<str:id_animal>/?error=<str:error>', views.animal_detail, name='animal_detail_mes'),
    path('post/new/', views.post_new, name='post_new'),
]

