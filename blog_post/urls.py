from django.urls import path
from .views import (BlogListView,
                    BlogDetailsView,
                    BlogCreateView,
                    BlogUpdateView,
                    BlogDeleteView)

urlpatterns = [
    path('',view=BlogListView.as_view(),name='home'),
    path("post/<int:pk>/",view=BlogDetailsView.as_view(),name='post_details'),
    path("post/<int:pk>/edit/",view=BlogUpdateView.as_view(),name='post_edit'),
    path("post/<int:pk>/delete/",view=BlogDeleteView.as_view(),name='post_delete'),
    path("post/new/",view=BlogCreateView.as_view(),name='post_new'),
]