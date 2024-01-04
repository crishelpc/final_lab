from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), 
    path('about/', views.about, name='about'),
    path('login/', views.login_user, name='login'), 
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('product/<int:pk>', views.product, name='product'),
    path('category/<int:pk>', views.category, name='category'),
    path('category/add_category', views.add_category, name='add_category'),
    path('category/<pk>/edit_category', views.edit_category, name='edit_category'),
]
    
