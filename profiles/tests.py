from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

from profiles.models import Profile


class ProfilesModelTest(TestCase):
    def setUp(self):
         user_data = {
          "password": "pbkdf2_sha256$180000$8ZKjEEdeYubZ$jq4T/Vaa2DWdAvzNys4ynNO6Wd/PsWe3dux20F7BGgQ=",
          "username": "4meRomance",
          "first_name": "John",
          "last_name": "Rodriguez",
          "email": "coemperor@famemma.net",
         }
         user = User(**user_data)
         user.save()
         profile_data = {
          "user_id": user.id,
          "favorite_city": "Barcelona"
         }
         profile = Profile(**profile_data)
         profile.save()

    def test_user_label(self):
        user = User.objects.first()
        field_label = user._meta.get_field('password').verbose_name
        self.assertEqual(field_label, 'password')
        field_label = user._meta.get_field('username').verbose_name
        self.assertEqual(field_label, 'username')

    def test_profile_label(self):
        profile = Profile.objects.first()
        field_label = profile._meta.get_field('user').verbose_name
        self.assertEqual(field_label, 'user')
        field_label = profile._meta.get_field('favorite_city').verbose_name
        self.assertEqual(field_label, 'favorite city')

    def test_url(self):
        profile = Profile.objects.first()
        url = reverse('profiles_index')
        self.assertEqual(url, '/profiles/')
        url = reverse('profile', kwargs={'username' : profile.user})
        self.assertEqual(url, f'/profiles/{profile.user}/')

    def test_profiles_index_view(self):
        url = reverse('profiles_index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "profiles/index.html")
        self.assertTrue("profiles_list" in response.context)

    def test_profiles_profile_view(self):
        profile = Profile.objects.first()
        url = reverse('profile', kwargs={'username' : profile.user})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "profiles/profile.html")
        self.assertTrue("profile" in response.context)


