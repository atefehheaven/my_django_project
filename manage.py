#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()

# django-admin startproject myproject  دستور ساخت اسکلت پروژه

# python manage.py makemigrations myapp  دستور تبدیل به جنگو
# python manage.py createsuperuser دستور ساخت پنل ادمین




# python -m venv venv
# .\venv\Scripts\activate
# pip install django
# pip install psycopg2-binary
# pip install djangorestframework