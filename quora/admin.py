from django.contrib import admin
from .models import Question , Profile , Comment , Replies

# Register your models here.
admin.site.register(Question)
admin.site.register(Profile)
admin.site.register(Comment)
admin.site.register(Replies)