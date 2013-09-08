from django.contrib import admin
from video_manager.models import Rating
from video_manager.models import Surgeon
from video_manager.models import Task
from video_manager.models import Video

admin.site.register(Rating)
admin.site.register(Surgeon)
admin.site.register(Task)
admin.site.register(Video)