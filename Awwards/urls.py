from django.urls import re_path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    # re_path('^$',views.post,name = 'newpost'),
    re_path(r'^$',views.post_item,name='postToday'),
    re_path(r'^accounts/profile/$',views.profile,name='profile_edit'),
    re_path(r'^post/(\d+)',views.post_item,name ='post'),
    re_path(r'^search/', views.search_results, name='search_results'),
    re_path(r'^new/updateUser$', views.updatePost, name='updateUser'),
    # re_path(r'^profile/(?P<username>\w+)/settings', add_profile, name='Profile'),
    re_path(r'^api/merch/$', views.MerchList.as_view()),
    re_path(r"^/profile/(\d+)", views.add_profile, name="profile"),
    # re_path(r'^project/(?P<id>\d+)',views.project,name='project'),
    
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)