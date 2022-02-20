from django.urls import path,include
from blog import views

urlpatterns = [
    path('',views.PostListView.as_view(),name='post_list_view'),
    path('about/',views.AboutView.as_view(),name='about_me'),
    # we need to define type of primary key that we are getting after path.
    # otherwise it will anything that comes after post/ as pk and  throw an error
    # specifying pk is only int will help resolving the issue
    path('post/<int:pk>',views.PostDetailView.as_view(),name='post_detail_view'),
    path('post/create/',views.CreatePostView.as_view(),name='create_post_view'),
    path('post/<int:pk>/update',views.UpdatePostView.as_view(),name='update_post_view'),
    path('post/<int:pk>/delete',views.DeletePostView.as_view(),name='delete_post_view'),
    path('drafts/',views.DraftListView.as_view(),name='post_draft_view'),
    path('post/<int:pk>/comment',views.add_comment_to_post,name='add_comment_to_post'),
    path('comment/<int:pk>/approve',views.comment_approve,name='comment_approve'),
    path('comment/<int:pk>/remove',views.comment_remove,name='comment_remove'),
    path('post/<int:pk>/publish/', views.post_publish, name='post_publish'),
    

]
