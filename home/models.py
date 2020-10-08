from django.db import models
from django.db.models.signals import pre_save
# Create your models here.
from quiz.utils import unique_slug_generator
from django.contrib.auth.models import User
class Topics(models.Model):
    
    heading = models.CharField(max_length=100,null=True)
    slug = models.SlugField(blank=True,null=True)
    def __str__(self):
        return str(self.heading)
    
def slug_generator(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
pre_save.connect(slug_generator,sender=Topics)  

class Quuestions(models.Model):
    s_n_o = models.IntegerField(default=0,null=True)
    Topicss = models.ForeignKey(Topics,on_delete=models.SET_NULL,blank=True,null=True)
    questions  = models.CharField(max_length=100,null=True)
    option1 = models.CharField(max_length=100,null=True)
    option2 = models.CharField(max_length=100,null=True)
    option3 = models.CharField(max_length=100,null=True)
    options =  [
        ("option1","option1"),
        ("option2","option2"),
        ("option3","option3"),
    ]
      
    
    correct = models.CharField(max_length=100,choices=options,default="option1")
    def __str__(self):
        return str(self.questions)


class users(models.Model):
    name = models.CharField(max_length=30,null=True)
    slug =models.SlugField(blank=True,null=True)
    def __str__(self):
        return str(self.name)


class no_tests(models.Model):
    nameofthetest = models.ForeignKey(Topics,on_delete=models.SET_NULL,blank=True,null=True)
    user_name= models.ForeignKey(User,on_delete=models.SET_NULL,blank=True,null=True)
    nomarks = models.IntegerField(default=0,null=True)
    def __str__(self):
        return str(self.nameofthetest)