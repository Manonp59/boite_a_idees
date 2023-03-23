from django.urls import path 
from . import views

urlpatterns = [
    path('idea_list/', views.IdeaListView.as_view(), name='idea-list'),
    path('idea_detail/<int:pk>', views.IdeaDetailView.as_view(), name="idea-detail"),
    path('idea_create/', views.IdeaCreateView.as_view(), name="idea-create"),
    path('idea_detail/<int:pk>/like/',views.like,name='like'),
    path('idea_detail/<int:pk>/dislike/',views.dislike,name='dislike'),
    
]