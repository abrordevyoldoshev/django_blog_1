# from django.test import TestCase
# from django.contrib.auth import get_user_model
# from django.urls import reverse
# from .models import Post
#
#
# # Create your tests here.
# class BlogTest(TestCase):
#     def setUp(self):
#         self.user = get_user_model().object_creatre_user(
#             username='testuser',
#             email='test@email.com',
#             password='secret'
#         )
#         self.post = Post.objects.create(
#             title='Yangi post',
#             body='Post matni',
#             author=self.user
#         )
#
#     def test_string_representation(self):
#         self.assertEqual(f"{self.post.title}", 'Yangi Post'),
#         self.assertEqual(f"{self.post.author}", 'testuser')
#         self.assertEqual(f"{self.post.body}", 'testuser')
#
#     def test_post_list_view(self):
#         response = self.client.get(reverse('home'))
#         self.assertEqual(response.status_code, 200)
#         self.assertContains(response, 'Post matni')
#         self.assertTemplateUsed(response, 'home,html')
#
#     def test_post_detail_view(self):
#         response = self.client.get('/post/1/')
#         no_response = self.client.get('/post/10000/')
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(no_response.status_code, 400)
#         self.assertContains(response, 'Yangi post')
#         self.assertTemplateUsed(response, 'post_detail.html')
