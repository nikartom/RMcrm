from django.urls import path
from . import views, auth_views

app_name = "crm"   


urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("register", auth_views.register_request, name="register"),
    path("login", auth_views.login_request, name="login"),
    path("logout", auth_views.logout_request, name= "logout"),
    path("password_reset", auth_views.password_reset_request, name="password_reset"),
]