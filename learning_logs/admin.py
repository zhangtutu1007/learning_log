from django.contrib import admin
from learning_logs.models import Topic
admin.site.register(Topic)
from learning_logs.models import Entry
admin.site.register(Entry)
# Register your models here.
