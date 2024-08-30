from django.urls import path
from django.contrib.auth.views import LogoutView, LoginView
from . import views

# urlpatterns = [
#     path('login', views.login, name='login'),
#     path('logout', views.logout, name='logout'),
#     path('register', views.register, name='register'),
#     path('dashboard', views.dashboard, name='dashboard'),
# ]

# urlpatterns = [
#     path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
#     path('register/', views.register_view, name='register'),
#     path('logout/', LogoutView.as_view(), name='logout'),
#     path('dashboard/', views.dashboard_view, name='dashboard'),
# ]

app_name = 'accounts'

urlpatterns = [
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', LogoutView.as_view(next_page='accounts:login'), name='logout'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
]