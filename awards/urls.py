from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns=[
    path ('',views.index,name = 'index'),
    path('register',views.register,name='register'),
    path('signin',views.login_in,name='signin'),
    path('logout',views.log_out,name='logout'),
    # path('home',views.home,name='home'),
    # path('profile',views.profile,name='profile'),
    
    
]


if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    urlpatterns += staticfiles_urlpatterns()
