from django.db import models
from django.utils import timezone
import datetime

# Create your models here.
class Links(models.Model):
    link_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    def __str__(self):
        return self.link_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)