from django.urls import path
from . import views


urlpatterns = [
    path('basic_list', views.view_basic_list, name='view_basic_list'),
    path('', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('manage_account/<int:pk>/', views.manage_account, name='manage_account'),
    path('delete_account/<int:pk>/', views.delete_account, name='delete_account'),
    path('change_password/<int:pk>/', views.change_password, name='change_password'),
    path('view_menu', views.view_menu, name='view_menu'),
    path('add_menu', views.add_menu, name='add_menu'),
    path('view_detail/<int:pk>/', views.view_detail, name='view_detail'),
    path('update_dish/<int:pk>/', views.update_dish, name='update_dish'),
    path('delete_dish/<int:pk>/', views.delete_dish, name='delete_dish')
]