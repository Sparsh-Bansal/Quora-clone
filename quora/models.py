from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Question(models.Model):

    STATUS_CHOICES = (
        ('draft' , 'Draft'),
        ('published' , 'Published')
    )

    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=120)
    author = models.ForeignKey(User , related_name='blog_posts' , on_delete=models.CASCADE)
    body = models.TextField()
    likes = models.ManyToManyField(User , related_name='post_likes',blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10 , choices=STATUS_CHOICES,default='draft')
    restrict_comments = models.BooleanField(default=False)
    favourite_ques = models.ManyToManyField(User,related_name='favourite_ques',blank=True)

    def __str__(self):
        return self.title



class Profile(models.Model):

    user = models.OneToOneField(User,on_delete=models.CASCADE)
    DOB = models.DateField(null=True,blank=True)
    photo = models.ImageField(null=True,blank=True)

    def __str__(self):
        return "profile {}".format(self.user.username)



class Comment(models.Model):

    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_comment')
    ques = models.ForeignKey(Question,on_delete=models.CASCADE,related_name='ques_comment')
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}-{}'.format(self.ques.title , self.user.username)



class Replies(models.Model):

    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_reply')
    comment = models.ForeignKey(Comment , on_delete=models.CASCADE,related_name='comment_reply')
    ques = models.ForeignKey(Question,on_delete=models.CASCADE,related_name='ques_reply')
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}-{}-{}'.format(self.comment.id,self.ques.title,self.user.username)
