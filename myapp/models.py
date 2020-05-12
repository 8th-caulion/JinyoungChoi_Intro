from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length = 200)
    name = models.CharField(max_length = 40)
    location = models.CharField(max_length=40)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:40]

#여기부터 comment
class Comment(models.Model):
    post = models.ForeignKey('myapp.Blog', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    pub_date = models.DateTimeField('date published')
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text