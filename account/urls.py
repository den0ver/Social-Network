from django.contrib.auth import views as auth_views
from django.urls import path
from django.urls import reverse_lazy
from . import views

app_name = 'account'


urlpatterns = [
    #предыдущий URL-адрес
    #path('login/', views.user_login, name='login'),

    #URL-адреса для входа и выхода
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    #URL-адреса для смены пароля
    path('password-change/', auth_views.PasswordChangeView.as_view(success_url=reverse_lazy('account:password_change_done')), name="password_change"),
    path('password-change/done/', auth_views.PasswordChangeDoneView.as_view(), name="password_change_done"),

    path('', views.dashboard, name='dashboard'),
]