from django.db import models

# Create your models here.

from django.db import models

# Create your models here.

class Post(models.Model):
    tittle = models.CharField(max_length=50)
    body = models.TextField()

    def _str_(self):
        return self.tittle 