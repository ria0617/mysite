from blog import views
from django.urls import path, re_path


app_name = 'blog'
urlpatterns = [
    path('', views.PostLV.as_view(), name='index'),
    path('post/', views.PostLV.as_view(), name='post_list'),
    
    #정규표현식
    re_path(r'^post/(?P<slug>[-\w]+)/$', views.PostDV.as_view(), name='post_detail'),
    
    path('archive/', views.PostAV.as_view(), name='post_archive'),
    path('archive/<int:year>/', views.PostYAV.as_view(), name= 'post_year_archive'),
    path('archive/<int:year>/<str:month>/', views.PostMAV.as_view(), name='post_month_archive'),
    path('archive/<int:year>/<str:month>/<int:day>/', views.PostDAV.as_view(), name='post_day_archive'),
    
    path('archive/today/', views.PostTAV.as_view(), name='post_today_archive'),
    
    #태그 관련
    path('tag/', views.TagCloudTV.as_view(), name='tag_cloud'), 
    path('tag/<str:tag>/', views.TaggedObjectLV.as_view(), name='tagged_object_list'), 
    
    #검색 관련
    path('search/', views.SearchFormView.as_view(), name='search'),
    
    #편집 관련
    path('add/', views.PostCreateView.as_view(), name='add', ),
    path('change/', views.PostChangeLV.as_view(), name = 'change', ),
    path('<int:pk>/update/', views.PostUpdateView.as_view(), name='update', ),
    path('<int:pk>/delete/', views.PostDeleteView.as_view(), name='delete', ), 
    
    
]
