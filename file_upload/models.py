from django.db import models

# Create your models here.
class Files(models.Model):
    name = models.CharField(max_length=50,default="")
    Email = models.EmailField(max_length=50,default="")
    Roll_no = models.CharField(max_length=50,default="")


    file = models.FileField(upload_to="project_k", default="")

cd
    def __str__(self):
        return self.name

    def delete(self, using=None, keep_parents=False):
        self.file.delete()
        super().delete( using=None, keep_parents=False)
