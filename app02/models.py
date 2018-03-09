from django.db import models

from DjangoUeditor.models import UEditorField
# Create your models here.



class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=100)
    photo = models.ImageField('上传图片', upload_to='photos',null=True)

    def __unicode__(self):
        return self.first_name



    def __str__(self):
        return self.first_name

class Album(models.Model):
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    num_stars = models.IntegerField()

    def __unicode__(self):
        return self.name

class Album2(Album):
    class Meta:
        verbose_name = 'Album2'
        verbose_name_plural = verbose_name
        proxy = True

class Topping(models.Model):
    # ...
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Pizza(models.Model):
    # ...
    name = models.CharField(max_length=100,default="")
    toppings = models.ManyToManyField(Topping)
    contents = UEditorField('内容', height=500, width=700, default='', imagePath="ueditor/",
                           filePath='ueditor/', blank=True)


    def __str__(self):
        return self.name


    class Meta:
        permissions = (
            ("create_discussion", "Can create a discussion"),
            ("create_discussion2", "Can create a discussion2"),
            ("reply_discussion", "Can reply discussion"),
            ("reply_discussion2", "Can reply discussion2"),
        )