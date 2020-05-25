from django.test import TestCase

from .models import Post
# Create your tests here.

class PostModelTest(TestCase):

    def setUP(self):
        Post.objects.create(text="just a test")

    def test_text_content(self):
        p = Post.objects.get(pk=1)
        expected_text = f'{p.text}'
        self.assertEqual(expected_text,"just a text")
