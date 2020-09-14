from django.urls import path
from .views import Home


from django.urls import include
urlpatterns = [
    path('', Home.as_view(), name="home"),
    path('posts/', include('post.urls')),
    path('MediUser/', include('user.urls'))
]
