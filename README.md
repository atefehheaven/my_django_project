My Django Blog Application
یک اپلیکیشن وبلاگ ساده و کامل که با استفاده از فریم‌ورک Django و Django REST Framework (DRF) ساخته شده است. این پروژه تمام فرآیندهای اصلی مدیریت داده (CRUD) و احراز هویت کاربر را شامل می‌شود و به عنوان نمونه کار برای برنامه‌نویسان بک‌اند پایتون طراحی شده است.

قابلیت‌های اصلی
مدیریت پست‌ها (CRUD): ایجاد، مشاهده، ویرایش و حذف پست‌های بلاگ.
احراز هویت کاربر:ثبت نام،ورود و خروج امن کاربران.
پنل ادمین قدرتمند:مدیریت داده ها(پست ها و کاربران)از طریق پنل مدیریت داخلی جنگو.
استفاده از API کامل با DRF:یک APIکامل برای مدیریت پست ها که برای اتصال به فرانت اند های مدرن(React یا Vue.js) آماده است.
تست خودکار:تست های خودکار برای مدل ها و View های اصلی جهت اطمینان از صحت عملکرد کد.

ناوری‌های استفاده شده
زبان برنامه‌نویسی: Python 3
فریم‌ورک وب: Django
و Django REST Framework(DRF):API
پایگاه داده:PostgreSQL
سیستم کنترل نسخه: Git و GitHub

نحوه راه اندازی پروژه بصورت محلی:
1.مخزن پروژه را از گیت هاب به کامپیوتر خودتان منتقل کنید:
git clone https://github.com/your-username/my_django_project.git
cd my_django_project
بجای your_username نام کاربری گیت هاب خودتان را بنویسید.

2.راه اندازی محیط مجازی:
یک محیط مجازی جدید بسازید و فعال کنید(Virtual Environment):

python -m venv venv
# در ویندوز:
.\venv\Scripts\activate
# در لینوکس/مک:
source venv/bin/activate

3.نصب وابستگی ها:
فایل requirment.txt را با pip نصب کنید.
نکته:اگر این فایل را نداشتید با دستور
pip freeze > requirements.txt
آن را ایجاد کنید.
pip install -r requirements.txt

4.تنظیمات پایگاه داده:
اطلاهات پایگاه داده PostgreSQL خود را در فایل myproject/settings.py وارد کنید.

# myproject/settings.py

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'mydjangodb',
        'USER': 'postgres',
        'PASSWORD': 'YOUR_POSTGRES_PASSWORD',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

5.اجرای Migrationها:
فرمان های زیر را برای ایجاد جداول در پایگاه داده ایجاد کنید:

python manage.py makemigrations myapp
python manage.py migrate

6.ایجاد کاربر مدیر(Superuser):
برای دسترسی به پنل ادمین، یک کاربر مدیر ایجاد کنید:

python manage.py createsuperuser

7.ایجاد سرور توسعه:
سرور جنگو را اجرا کنید:

python manage.py runserver


در نهایت میتوانید اپلیکیشن را در آدرس http://127.0.0.1:8000/ مشاهده کنید.
