from django.db import models

# title, content, author_name, pub_date
class Blog(models.Model):
  title = models.CharField(max_length=200)
  content = models.CharField(max_length=1000)
  author_name = models.CharField(max_length=200)
  pub_date = models.DateTimeField('date_published')


