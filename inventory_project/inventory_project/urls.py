from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from inventory import inventory_list, add_inventory, inventory_detail, delete_inventory



urlpatterns = [
    path('admin/', admin.site.urls),
     path('', auth_views.LoginView.as_view(template_name='inventory/home.html'), name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='inventory/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='inventory/logout.html'), name='logout'),
    path('signup/', auth_views.register, name='signup'),
     path('inventory/', inventory_list, name='inventory_list'),
    path('inventory/add/', add_inventory, name='add_inventory'),
    path('inventory/<int:pk>/', inventory_detail, name='inventory_detail'),
    path('inventory/<int:pk>/delete/', delete_inventory, name='delete_inventory'),
]
