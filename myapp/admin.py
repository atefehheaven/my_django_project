# myapp/admin.py
from django.contrib import admin
from .models import Post # مدل Post رو از فایل models.py خودمون ایمپورت میکنیم

# مدل Post رو در پنل ادمین ثبت میکنیم
admin.site.register(Post)