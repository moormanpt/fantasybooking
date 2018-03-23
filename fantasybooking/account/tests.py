from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.hashers import make_password
from model_mommy import mommy
from .models import User


class UserManager(TestCase):
    def test_create_user(self):
        user = User.objects.create_user("jonnyrico@fednet.gov", password="iwanttoknowmore")
        User.objects.get(id=user.id)



class LoginTest(TestCase):
    def setUp(self):
        self.user = mommy.make_recipe('fantasybooking.account.user')
        self.password = "wouldYouLikeToKnowMore"
        self.user.set_password(self.password)
        self.user.save()
        self.form_data = {"username": self.user.email,
                          "password": self.password,
                          }

    def test_user_login_unsuccessful(self):
        """
        on successful registration, keep user on login page
        and show error
        """
        self.form_data['password'] = "bugs rule federation drulz"
        url = reverse("login")
        response = self.client.post(url, self.form_data)
        actual = response.status_code
        expected = 200
        self.assertEqual(actual, expected)
        actual = response.context_data['form'].errors['__all__']
        expected = ['Please enter a correct email address and password. Note that both fields may be case-sensitive.']
        self.assertEqual(actual, expected)

    def test_login_works(self):
        """
        on attempted login, move user to the special page
        """
        url = reverse('login')
        actual = self.client.post(url, self.form_data)
        expected = reverse("home")
        self.assertRedirects(actual, expected)


