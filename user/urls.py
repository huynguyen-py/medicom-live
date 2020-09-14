from django.urls import path

from . import views
from post import views as views_post
from user.views import SiteLoginView, SiteProfileView, SiteLogoutView, SiteRegisterView, AdminCvView
from django.urls import include
urlpatterns = [
    #path('MediUser/', views_post),
    path('profileAdmin/', AdminCvView.as_view(), name="admin_cv"),
    path('login/', SiteLoginView.as_view(), name="login"),
    path('logout/', SiteLogoutView.as_view(), name="logout"),
    path('register/', SiteRegisterView.as_view(), name="register"),
    path('profile/', SiteProfileView.as_view(), name="profile"),

]
