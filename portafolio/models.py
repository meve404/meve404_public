from django.db import models
from PIL import Image

class project(models.Model):
    projectName = models.CharField(max_length=200)
    description = models.TextField(max_length=2000)
    lenguagesUsed = models.CharField(max_length=200)
    inDevelopment = models.BooleanField(default=False)
    projectLink = models.CharField(max_length=200, blank=True, null=True)
    gitHubRepo = models.CharField(max_length=200, blank=True, null=True)

    #SlideShow
    ImageSlide1 = models.ImageField(upload_to='hdFtuI2_sA', help_text='1903 x 960')
    ImageSlide2 = models.ImageField(upload_to='hdFtuI2_sA', blank=True, null=True)
    ImageSlide3 = models.ImageField(upload_to='hdFtuI2_sA', blank=True, null=True)

    updated = models.DateTimeField(auto_now=True) #takes a snapshot everytime the field is updated
    created = models.DateTimeField(auto_now_add=True) #takes a snapshot when the instance is created

    def save(self, *args, **kwargs): #it is when .save() is used
        try:
            super().save(*args, **kwargs)
            #resize the image uploaded by overwriting the save method
            slide_list = [self.ImageSlide1, self.ImageSlide2, self.ImageSlide3] #list of carousel images
            for item in slide_list: #for loop to resize all the images
                img = Image.open(item.path)
                if img.height > 900 or img.width > 900:
                    output_size = (900, 900)
                    img.thumbnail(output_size)
                    img.save(item.path)

        except:
            super().save(*args, **kwargs)

    def delete(self, *args, **kwargs): # it is when .delete() is used
        slide_list = [self.ImageSlide1, self.ImageSlide2, self.ImageSlide3]
        for item in slide_list:
            item.delete()
        
        super().delete(*args, **kwargs)
    
    def __str__(self):
        return self.projectName