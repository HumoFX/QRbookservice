from django.urls import path
from django.conf.urls import url, include

from . import views

app_name = 'articles'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:book_id>/', views.onClicks, name='onClick'),
    path('category/<int:category_id>/', views.detail, name='detail'),
    path('category/<int:category_id>/<int:book_id>/', views.onClicksCategory, name='onClickCat'),
    path('<int:article_id>/leave_comment', views.leave_comment, name='leave_comment'),
    path('search/', views.SearchResultsView.as_view(), name='search_results'),
    path('search/<int:book_id>/', views.onClickSearch, name='onClickSearch'),
    url(r'^success', views.success, name='success'),
]
