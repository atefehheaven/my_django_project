# myapp/models.py
from django.db import models

# هر کلاس مدل، یک جدول در پایگاه داده رو نشون میده
class Post(models.Model):
    title = models.CharField(max_length=200) # فیلد متنی با حداکثر 200 کاراکتر
    content = models.TextField()             # فیلد متنی بلند
    pub_date = models.DateTimeField(auto_now_add=True) # تاریخ انتشار (به صورت خودکار اضافه میشه)

    def __str__(self):
        # این متد نشون میده وقتی آبجکت Post رو پرینت میکنی یا توی پنل ادمین میبینی، چی نمایش داده بشه
        return self.title
    
class Contact(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()