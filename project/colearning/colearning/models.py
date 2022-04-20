from django.db import models


class Post(models.Model):
    space_name = models.CharField(max_length = 20, default = "Unkown")
    title = models.CharField(max_length = 100, default = "Unknown" )
    content = models.TextField(default = "Blank")

    def __str__(self):
        return space_name.char
        
class Item(models.Model):
    post = models.ForeignKey(Post, on_delete = models.CASCADE)
    text = models.CharField(max_length = 300, default = "Blank")
    complete = models.BooleanField()

    def __str__(self):
        return self.text