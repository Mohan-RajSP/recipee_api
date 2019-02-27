from django.contrib.auth import get_user_model
from django.test import TestCase

class user_Create_check(TestCase):

    def test_user_create(self):

        email = "test@gmail.com"
        password = "Test@123"
        user = get_user_model().objects.create_user(email =email, password= password)
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_user_email(self):

        email = "test1@gmail.com"
        password = "Test1@123"
        user = get_user_model().objects.create_user(email = email, password = password)
        self.assertEqual(user.email, email.lower())

    def test_mail_invalid(self):

        with self.assertRaises(ValueError):
        # if we execute the below create function, the model fucntion should raise value error.
        #if it doesnot raise, then it is a failure
            user = get_user_model().objects.create_user(email=None, password = "Test@123")

    def test_superuser_creation(self):

        email = "test2@gmail.com"
        password = "Test@123"

        user = get_user_model().objects.create_superuser(email=email, password= password)
        self.assertTrue(user.is_superuser)
