from django.db import models
class Document(models.Model):
    docfile = models.FileField(upload_to='')
    def __str__(self):
        return str(self.docfile)
    