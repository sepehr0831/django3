
from django.urls import path
from .views import HomeView ,ArticleDetailView ,AddPostView , UpdateView, DeletePostView , AddCategoryView , Categoryview , LikeView , Authorview , AddCommentView


urlpatterns = [
    path("",HomeView.as_view(),name="home"),
    path("article/<int:pk>",ArticleDetailView.as_view(), name="article-detail"),
    path("add_post",AddPostView.as_view() , name="add_post"),
    path("article/edit/<int:pk>",UpdateView.as_view() , name="update_post"),
    path("article/<int:pk>/remove",DeletePostView.as_view() , name="delete_post"),
    path("add_category",AddCategoryView.as_view() , name="add_category"),
    path("category/<str:cats>/",Categoryview , name="category"),
    path("author/<str:username>/",Authorview , name="author"),
    path("like/<int:pk>",LikeView , name="like_post"),
    path("article/<int:pk>/comment/",AddCommentView.as_view() ,name="add_comment"),
]

