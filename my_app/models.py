from django.db import models
from django.urls import reverse
from django.utils import timezone
from cloudinary.models import CloudinaryField # type: ignore


# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)

    def get_absolute_url(self):
        return reverse('author-detail', args=[str(self.id)])
    
    def __str__(self) :
        return f'{self.first_name} {self.last_name}'
    

class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.email
    

class Blog(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = CloudinaryField("image",null=True)
    date_posted = models.DateTimeField(default=timezone.now)
    last_updated = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)

    class Meta:
        ordering = ['-date_posted']


    def __str__(self) :
        return self.title
    
    def published(cls):
        return cls.objects.filter(is_published=True)
    
    


    