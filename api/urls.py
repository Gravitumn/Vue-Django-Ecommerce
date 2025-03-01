from django.contrib import admin
from django.urls import path, include

from django.urls import path
from .views import user_views
from .views import product_views
from .views import category_views
from rest_framework.routers import DefaultRouter



urlpatterns = [
    #authentication
    path('api/set-csrf-token', user_views.set_csrf_token, name='set_csrf_token'),
    path('api/login', user_views.login_view, name='login'),
    path('api/logout', user_views.logout_view, name='logout'),
    path('api/user', user_views.user, name='user'),
    path('api/register', user_views.register, name='register'),

    #user
    path('api/get_all_users',user_views.get_all_users, name='get_all_users'),
    path('api/update_user/<int:user_id>/',user_views.update_user, name='update_user'),
    path('api/delete_user/<int:user_id>/',user_views.delete_user, name='delete_user'),

    #product
    path('api/get_all_products',product_views.get_all_products,name='get_all_products'),
    path('api/show_all_products',product_views.show_all_products,name='show_all_products'),
    path('api/admin_get_all_products',product_views.admin_get_all_products,name='admin_get_all_products'),
    path('api/addProduct',product_views.add_product,name='add_product'),
    path('api/update_product/<int:product_id>/',product_views.update_product,name='update_product'),
    path('api/update_product_image/<int:product_id>/',product_views.update_product_image,name='update_product_image'),
    path('api/delete_product/<int:product_id>/',product_views.delete_product,name = 'delete_product'),
    path('api/get_super_category_products/<int:super_category_id>',product_views.get_super_category_products, name= 'get_super_category_products'),
    
    #Category
    path('api/get_super_category',category_views.get_super_category,name='get_super_category'),
    path('api/get_sub_category',category_views.get_sub_category,name='get_sub_category'),
    path('api/get_sub_category_by_parent/<int:parent_id>',category_views.get_sub_category_by_parent,name='get_sub_category_by_parent'),
]