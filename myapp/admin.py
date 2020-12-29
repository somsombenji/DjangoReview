from django.contrib import admin
from .models import Blog #같은 폴더에 있는 models라는 파일에서 Blog 클래스를 import

admin.site.register(Blog)