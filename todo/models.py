from django.db import models

class Post(models.Model):

    title = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    photo = models.URLField(blank=True)
    count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Choice(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
    def __str__(self):
        return str(self.post) + " --  " + self.text
