# articles/urls.def

from django.urls import path
from . import views
urlpatterns = [
    path('', views.ArticleListView.as_view(), name='article_list'),
    path('<int:pk>/edit', views.ArticleUpdateView.as_view(), name='article-edit'),
    path('<int:pk>/', views.ArticleDetailView.as_view(), name='article-detail'),
    path('<int:pk>/delete', views.ArticleDeleteView.as_view(), name='article-delete'),
]
