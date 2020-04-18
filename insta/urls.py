from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.home, name='home'),
    path('index', views.index, name='index'),
    path('sign_up', views.sign_up, name='sign_up'),
    path('logout', views.logout, name='logout'),
    path('upload/<str:pk>', views.upload, name='upload'),
    path('own-profile', views.own_profile, name='own-profile'),
    path('profile/<str:pk>', views.profile, name='profile'),
    path('profilepic-upload/<str:pk>', views.profilepic_upload),
    path('list', views.list, name='list'),
    path('profile/follow/<str:pk>', views.follow, name='follow'),
    path('profile/unfollow/<str:pk>', views.unfollow, name='unfollow'),
    path('feed_profile/follow/<str:pk>', views.follow),
    path('feed_profile/unfollow/<str:pk>', views.unfollow),
    path('feed_profile/<str:pk>', views.feed_profile),
    path('photo/<str:pk>', views.post_detail),
    path('photo/like/<str:pk>', views.like),
    path('photo/unlike/<str:pk>', views.unlike),
    path('photo/comment/<str:pk>', views.comment),
    path('own_post_detail/<str:pk>', views.own_post_detail),
    path('own_post_detail/like/<str:pk>', views.like),
    path('own_post_detail/unlike/<str:pk>', views.unlike),
    path('own_post_detail/comment/<str:pk>', views.comment),
    path('own_post_detail/edit/<str:pk>', views.edit),
    path('own_post_detail/delete/<str:pk>', views.delete),
]

urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
