from django.db import models
# from .exif import process_image
# Create your models here.
# class photo(models.Model):
#
#     image = models.ImageField(upload_to='images')
#     views = models.IntegerField(default=0)
#     description = models.CharField(max_length=150)
#
#



class wildlife(models.Model):

    photographer = models.CharField(max_length=20)
    shot_on = models.CharField(max_length=50)
    image = models.ImageField(upload_to='wildlife/images')
    description = models.CharField(max_length=150)
    views = models.IntegerField(default=0)
    batch = models.CharField(max_length=4)
    insta = models.URLField()


    # exif = models.OneToOneField(exif,on_delete=models.CASCADE)

    # tags = process_image(get_path(image))

    brand = models.CharField(max_length=50,null=True,blank=True)
    model = models.CharField(max_length=50,null=True,blank=True)
    date = models.CharField(max_length=50,null=True,blank=True)
    shutterspeed = models.CharField(max_length=50,null=True,blank=True)
    focallength = models.CharField(max_length=50,null=True,blank=True)
    aperture = models.CharField(max_length=50,null=True,blank=True)
    iso = models.CharField(max_length=50,null=True,blank=True)
    lens = models.CharField(max_length=50,null=True,blank=True)

    def __str__(self):
        return self.photographer

class board(models.Model):

    genre = models.CharField(max_length=20)
    detail1 = models.ForeignKey(wildlife,on_delete=models.CASCADE,related_name='+')
    detail2 = models.ForeignKey(wildlife,on_delete=models.CASCADE,related_name='+')
    detail3 = models.ForeignKey(wildlife,on_delete=models.CASCADE,related_name='+')
    detail4 = models.ForeignKey(wildlife,on_delete=models.CASCADE,related_name='+')
    detail5 = models.ForeignKey(wildlife,on_delete=models.CASCADE,related_name='+')
    detail6 = models.ForeignKey(wildlife,on_delete=models.CASCADE,related_name='+')
    detail7 = models.ForeignKey(wildlife,on_delete=models.CASCADE,related_name='+')
    detail8 = models.ForeignKey(wildlife,on_delete=models.CASCADE,related_name='+')
    detail9 = models.ForeignKey(wildlife,on_delete=models.CASCADE,related_name='+')
    detail10 = models.ForeignKey(wildlife,on_delete=models.CASCADE,blank=True,null=True)
    def __str__(self):
        return self.genre


# class image(models.Model):
#     image = models.ImageField(upload_to='images')
#
# class details(models.Model,image):




# class exif(models.Model):
#
#     image = models.ForeignKey(image,on_delete=models.CASCADE,null=True,blank=True)
#     brand = models.CharField(max_length=50)
#     model = models.CharField(max_length=50)
#     date = models.CharField(max_length=50)
#     shutterspeed = models.CharField(max_length=50)
#     focallength = models.CharField(max_length=50)
#     aperture = models.CharField(max_length=50)
#     iso = models.CharField(max_length=50)
#     lens = models.CharField(max_length=50)
# #
#

# class portraiture(models.Model):
#
#     photographer = models.CharField(max_length=20)
#     shot_on = models.CharField(max_length=50)
#     image = models.ImageField(upload_to='portrait/images')
#     description = models.CharField(max_length=150)
#     views = models.IntegerField(default=0)
#     batch = models.CharField(max_length=4)
#     insta = models.URLField()
#
# class lifestyle(models.Model):
#
#     photographer = models.CharField(max_length=20)
#     shot_on = models.CharField(max_length=50)
#     image = models.ImageField(upload_to='lifestyle/images')
#     description = models.CharField(max_length=150)
#     views = models.IntegerField(default=0)
#     batch = models.CharField(max_length=4)
#     insta = models.URLField()
#
# class street(models.Model):
#
#     photographer = models.CharField(max_length=20)
#     shot_on = models.CharField(max_length=50)
#     image = models.ImageField(upload_to='street/images')
#     description = models.CharField(max_length=150)
#     views = models.IntegerField(default=0)
#     batch = models.CharField(max_length=4)
#     insta = models.URLField()
#
# class landscape(models.Model):
#
#     photographer = models.CharField(max_length=20)
#     shot_on = models.CharField(max_length=50)
#     image = models.ImageField(upload_to='wildlife/images')
#     description = models.CharField(max_length=150)
#     views = models.IntegerField(default=0)
#     batch = models.CharField(max_length=4)
#     insta = models.URLField()
#
# class abstract(models.Model):
#
#     photographer = models.CharField(max_length=20)
#     shot_on = models.CharField(max_length=50)
#     image = models.ImageField(upload_to='abstract/images')
#     description = models.CharField(max_length=150)
#     views = models.IntegerField(default=0)
#     batch = models.CharField(max_length=4)
#     insta = models.URLField()
#
# class night_life(models.Model):
#
#     photographer = models.CharField(max_length=20)
#     shot_on = models.CharField(max_length=50)
#     image = models.ImageField(upload_to='night_life/images')
#     description = models.CharField(max_length=150)
#     views = models.IntegerField(default=0)
#     batch = models.CharField(max_length=4)
#     insta = models.URLField()
#
# class long_exposure(models.Model):
#
#     photographer = models.CharField(max_length=20)
#     shot_on = models.CharField(max_length=50)
#     image = models.ImageField(upload_to='long_exposure/images')
#     description = models.CharField(max_length=150)
#     views = models.IntegerField(default=0)
#     batch = models.CharField(max_length=4)
#     insta = models.URLField()
#
# class bird(models.Model):
#
#     photographer = models.CharField(max_length=20)
#     shot_on = models.CharField(max_length=50)
#     image = models.ImageField(upload_to='bird/images')
#     description = models.CharField(max_length=150)
#     views = models.IntegerField(default=0)
#     batch = models.CharField(max_length=4)
#     insta = models.URLField()
#
# class architechture(models.Model):
#
#     photographer = models.CharField(max_length=20)
#     shot_on = models.CharField(max_length=50)
#     image = models.ImageField(upload_to='architechture/images')
#     description = models.CharField(max_length=150)
#     views = models.IntegerField(default=0)
#     batch = models.CharField(max_length=4)
#     insta = models.URLField()
#
# class vogue(models.Model):
#
#     photographer = models.CharField(max_length=20)
#     shot_on = models.CharField(max_length=50)
#     image = models.ImageField(upload_to='vogue/images')
#     description = models.CharField(max_length=150)
#     views = models.IntegerField(default=0)
#     batch = models.CharField(max_length=4)
#     insta = models.URLField()
