from django.urls import include, re_path
# from django.conf.urls import include, re_path
from django.contrib.auth import views
from django.contrib import admin
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'',include('Awwards.urls')),
    re_path(r'^accounts/', include('registration.backends.simple.urls')),
    # re_path(r'^login/$', views.LogintView.as_view(), {"next_page": 'Logout'}),
    re_path(r'^logout/$', views.LogoutView.as_view(), {"next_page": '/'}),
    re_path(r'^tinymce/', include('tinymce.urls')),
    re_path(r'^api-token-auth/', obtain_auth_token)
  
]


