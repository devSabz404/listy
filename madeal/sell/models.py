from django.db import models
from django.conf import settings


from django.urls import reverse


# Create your models here.




class Location(models.Model):

    name = models.CharField(max_length=50,
                            db_index=True)
    slug = models.SlugField(max_length=50,
                            unique=True)
    
    def __str__(self):
        return self.name

    class Meta:

        ordering = ('name',)
        verbose_name = 'location'

  

        



class Advert(models.Model):
    CONDITION=(
        ('B','Brand New'),
        ('U','Used'),
    )
    
    ##user = models.OneToOneField(
        #settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    
    category= models.ForeignKey('Category',
                                 related_name='categories',
                                 on_delete=models.CASCADE)
    location = models.ForeignKey(Location,
                                 related_name='locations',
                                 on_delete=models.CASCADE)
    slug = models.SlugField(max_length=50, db_index=True)
   
    image=models.ImageField(upload_to="img/%y")
    condition=models.CharField(max_length=10,choices=CONDITION)
    description=models.TextField(max_length=300)
    price=models.FloatField()
    created = models.DateTimeField(auto_now_add=True)
    available = models.BooleanField(default=True)

    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        return reverse('advert-detail', args=[str(self.id)])

class Profile(models.Model):

    user_name = models.OneToOneField(
        settings.AUTH_USER_MODEL, related_name="userz", on_delete=models.CASCADE)
   
   
    
    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        return reverse('profile', args=[str(self.id)])
        # return reverse('profile', kwargs={'pk': self.pk})


class Category(models.Model):

    name = models.CharField(max_length=60,
                            db_index=True)
    slug = models.SlugField(max_length=60,
                            unique=True)
    advert = models.ManyToManyField(Advert,related_name='adverts')

    def get_advert(self):
        return "\n".join([p.advert for p in self.advert.all()])

    def __str__(self):
        return self.name

    class Meta:

        ordering = ('name',)
        verbose_name = 'category'


def get_absolute_url(self):
    """Returns the url to access a detail record for this book."""
    return reverse('category-detail', args=[str(self.id)])
