from django.contrib import admin
from .models import InstaUser, Photo, Follower, Likes, Comments
# Register your models here.
admin.site.register(InstaUser)
admin.site.register(Photo)
admin.site.register(Follower)
admin.site.register(Likes)
admin.site.register(Comments)
