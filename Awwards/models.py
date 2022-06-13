import profile
from unicodedata import name
from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from tinymce.models import HTMLField
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    user =models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
    profile_image = models.ImageField(upload_to="images",default="https://www.thespruce.com/thmb/Cn3rYk2FGUYrM8f_Yk99y9vcu8Q=/2121x1414/filters:no_upscale():max_bytes(150000):strip_icc()/patterned-carpet-in-decorative-living-room-interior-with-painting-above-couch--real-photo-996692496-dec2473f5d434d2c8eb50a7cd18b3758.jpg")
    name = models.CharField(max_length=50,blank=True)
    bio = models.TextField(max_length=600,default="awwards Bio",blank=True)
    contact = models.EmailField(max_length=300,blank=True)
    

    def __str__(self):
        return f"{self.user.username } Profile"

    def save_profile(self):
        self.save()
        
    def delete_profile(self):
        self.delete()

class AwwardsMerch(models.Model):
    name = models.CharField(max_length=40)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=20)

class Post(models.Model):
    title =  models.CharField(max_length=30)
    image = models.ImageField(upload_to='post/')
    description = models.TextField()
    link = models.CharField(max_length=500)
    user = models.ForeignKey(User,on_delete=models.CASCADE)


    def __str__(self):
            return self.title         


    def save_post(self):
        self.save()
        
    def delete_post(self):
        self.delete()

  
    @classmethod
    def search_by_title(cls,search_term):
        posts = cls.objects.filter(title__icontains=search_term)
        return posts





class Rating(models.Model):
    rating = (
            (1, '1'),
            (2, '2'),
            (3, '3'),
            (4, '4'),
            (5, '5'),
            (6, '6'),
            (7, '7'),
            (8, '8'),
            (9, '9'),
            (10, '10'),
    )
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='ratings',null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,related_name='rater')
    content = models.IntegerField(choices=rating,blank=True)
    design = models.IntegerField(choices=rating,blank=True)
    usability = models.IntegerField(choices=rating,blank=True)
    score = models.FloatField(default=0,blank=True)
    content_coverage = models.FloatField(default=0,blank=True)
    design_coverage = models.FloatField(default=0,blank=True)
    usability_coverage = models.FloatField(default=0,blank=True)

    def save_ratings(self):
            return  self.save()

    def __str__(self):
            return f"{self.post} Rating"
