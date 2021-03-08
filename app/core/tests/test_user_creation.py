from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    def test_user_creation(self):
        """For testing if the user is created"""
        email = "alan@iitg.ac.in"
        password = "123456"
        user = get_user_model().objects.create_user(email=email, password=password)
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_user_email_normalized(self):
        """Testing if the user email is normalized"""
        email = "alan@IITG.AC.IN"
        user = get_user_model().objects.create_user(email, "123453456")
        self.assertEqual(user.email, email.lower())

    def test_email_is_valid(self):
        """Testing if the valueerror is raised for empty email"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, "1234")

    def test_user_create_superuser(self):
        """Testing the superuser creation"""
        user = get_user_model().objects.create_superuser("asdfg@iitg.ac.in", "12345")
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)