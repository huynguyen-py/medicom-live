from django.urls import path
from .views import Posts
from . import views
urlpatterns = [
    path('category/<int:Category_Id>', views.Category_Detail, name="category_detail"),
    path('<int:Post_Id>/', views.post_detail_test.as_view(), name="post_detail"),
    path('newpost/', views.SiteAddPost.as_view(), name="add_post"),
    path('updatepost/<int:pk>', views.SiteUpdatePost.as_view(), name="update_post"),
    path('deletepost/<int:pk>', views.SiteDeletePost.as_view(), name="delete_post"),

    path('like/<int:pk>', views.LikeView, name="like_post"),

    path('listcategory/', Posts.as_view(), name="post"),
    path('newcategory/', views.SiteAddCate.as_view(), name="add_category"),
    path('updatecategory/<int:pk>', views.SiteUpdateCate.as_view(), name="update_category"),
    path('delete_category/<int:pk>', views.SiteDeleteCate.as_view(), name="delete_category"),

]
