from django.urls import include, re_path
# from django.conf.urls import include, re_path
from django.contrib.auth import views
from django.contrib import admin
from rest_framework.authtoken.views import obtain_auth_token
from django.contrib.auth import views as auth_views

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'',include('Awwards.urls')),
    re_path(r'^accounts/', include('registration.backends.simple.urls')),
    # re_path(r'^logout/$', views.LogoutView.as_view(), {"next_page": '/'}),
    re_path(r'^tinymce/', include('tinymce.urls')),
    re_path(r'^api-token-auth/', obtain_auth_token),
    re_path(r'^logout/', auth_views.logout_then_login),
  
]


