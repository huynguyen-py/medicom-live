from django.urls import path
from .views import Home, Landing_Page


from django.urls import include
urlpatterns = [
    path('', Landing_Page.as_view(), name="landing_page"),
    path('home/', Home.as_view(), name="home"),
    path('posts/', include('post.urls')),
    path('MediUser/', include('user.urls'))
]
