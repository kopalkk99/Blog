from django.db import models
from django.utils import timezone
from django.urls import reverse
# Create your models here.
class Post(models.Model):

    author = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    post_title = models.CharField(max_length = 256)
    post_desc = models.TextField() # not mandatory to have max_length
    created_date = models.DateTimeField(default = timezone.now)
    published_date = models.DateTimeField(blank= True,null=True)

    ## why cannot we have publish function in our views????
    def publish(self):
        self.published_date = timezone.now()
        self.save()
    def approve_comment(self):
        return self.comments.filter(approved_comment=True)

    ## straight representation of the model
    def __str__(self):
        return self.post_title

    def get_absolute_url(self):
        return reverse("post_detail_view",kwargs={'pk':self.pk})
class Comment(models.Model):

    post = models.ForeignKey('blog.Post',related_name ='comments',on_delete=models.CASCADE)
    author = models.CharField(max_length =  256) #we wont select from list or use logged in user
    comment_desc = models.TextField()
    created_date = models.DateField(default = timezone.now)
    approved_comment = models.BooleanField(default = False)


    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.comment_desc

    def get_absolute_url(self):
        return reverse("post_list_view")
