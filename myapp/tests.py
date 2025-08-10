# myapp/tests.py

from django.test import TestCase
from django.urls import reverse
from .models import Post

# تست برای مدل Post
class PostModelTests(TestCase):

    def test_post_str_representation(self):
        """
        تست می کند که متد __str__ مدل Post، عنوان پست را برمی گرداند.
        """
        post = Post(title="عنوان یک پست تست")
        self.assertEqual(str(post), "عنوان یک پست تست")

# تست برای View ها
class PostViewsTests(TestCase):

    def test_post_list_view_status_code(self):
        """
        تست می کند که View لیست پست ها کد وضعیت 200 را برمی گرداند.
        """
        response = self.client.get(reverse('post_list'))
        self.assertEqual(response.status_code, 200)

    def test_post_list_view_template(self):
        """
        تست می کند که View لیست پست ها از تمپلیت صحیح استفاده می کند.
        """
        response = self.client.get(reverse('post_list'))
        self.assertTemplateUsed(response, 'index.html')

    def test_post_list_view_content(self):
        """
        تست می کند که View لیست پست ها حاوی متن مورد نظر است.
        """
        response = self.client.get(reverse('post_list'))
        self.assertContains(response, "All Blog Posts")

    def test_post_detail_view_status_code_for_existing_post(self):
        """
        تست می کند که View جزئیات پست برای یک پست موجود، کد وضعیت 200 را برمی گرداند.
        """
        # ابتدا یک پست می سازیم تا بتوانیم آن را تست کنیم
        post = Post.objects.create(title="پست تست", content="این یک محتوای تست است.")
        response = self.client.get(reverse('post_detail', args=[post.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'post_detail.html')
        self.assertContains(response, "پست تست")

    def test_post_detail_view_404_for_non_existent_post(self):
        """
        تست می کند که View جزئیات پست برای یک پست ناموجود، کد وضعیت 404 را برمی گرداند.
        """
        response = self.client.get(reverse('post_detail', args=[999])) # آیدی ناموجود
        self.assertEqual(response.status_code, 404)