from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('profile/<str:pk>', views.profile, name='profile'),
    path('adding/<str:id>', views.adding, name='adding'),
    path('delete/<str:id>', views.delete, name='drop'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('add/', views.add_movie, name='add'),
    path('watching/<str:id>', views.watching, name='watching'),
    path('delete_movie/<str:id>', views.delete_movie, name='delete'),
    path('update_user/', views.update_user, name='update_user'),
    path('delete_comment/<str:id>', views.delete_comment, name='delete_comment')

]
