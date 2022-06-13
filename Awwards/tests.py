from turtle import title
from django.test import TestCase
from .models import Profile, Post, Rating

# Create your tests here.
# from django.test import TestCase
import profile
from tkinter import image_names
from unicodedata import name
from django.test import TestCase
from .models import Profile,Post, 


class ProfileTestClass(TestCase):
     """
    defining testcase for User class
    """
     def setUp(self):
         self.Brian = Profile(name = "Brian",bio = "kenyan born")

     def test_instance(self) :
         self.assertTrue(isinstance(self.Brian,Profile)) 

     
     def test_save_method(self):
        self.Brian.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) > 0)   



class RatingTestClass(TestCase):
    """
     defining test for rating class
    """
    def setUp(self):
        """
        Creating a new instance of the rating class
        """
        self.rating =Rating(name = 'brian')
        self.rating.save()

    def test_instance(self):
        self.assertTrue(isinstance(self. rating))

    def test_save_method(self):
        rating = Rating.objects.all()
        self.assertTrue(len(rating) > 0)        



class PostTestClass(TestCase):

    def setUp(self):
        """
        # Creating a new post and saving it
        """

        self.Brian= Post(title = 'Brian')
        self.Brian.save_post()

        # Creating a new tag and saving it
        self.new_post = title(name = 'testing')
        self.new_post.save()

        self.new_image= Post(image_name = 'upload')
        self.new_image.save()

        self.new_image.title.add(self.new_post)

    def tearDown(self):
        Profile.objects.all().delete()
        title.objects.all().delete()
        title.objects.all().delete()


def test_profile_today(self):
        post = Post.todays_post()
        self.assertTrue(len(post)>0)