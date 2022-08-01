from django.contrib import admin
from django.urls import path

from board.views import func,cat,Add_Post,Update_Post,Delete_Post,ListView_Post,post_detail,Add_Comment,Update_comment,Delete_Comment

urlpatterns = [
    path('', func,name="index"),
    path('cat/<int:id>', cat, name="cat"),
    path('cat/<int:id>/post', Add_Post.as_view(),name='newpost'),
    path('cat/<int:pk>/updatepost', Update_Post.as_view(), name='updatepost'),
    path('cat/<int:pk>/deletepost', Delete_Post.as_view(), name='deletepost'),
    path('cat/<int:id>/postdetails', post_detail, name='postdetails'),
    path('cat/<int:catid>/comment/<int:postid>',Add_Comment.as_view(),name="addcomment"),
    path('cat/<int:pk>/updatecomment/<int:catid>', Update_comment.as_view(), name="updatecomment"),
    path('cat/<int:pk>/deletecomment/<int:catid>', Delete_Comment.as_view(), name="deletecomment"),

]