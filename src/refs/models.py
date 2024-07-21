from django.db import models

# Create your models here.
class Genre(models.Model):
    """class for genre references"""
    name = models.CharField(max_length=100)
    description = models.TextField(
        blank=True,
        null=True
    )

    def get_absolute_url(self):
        return f'/genre-detail/{self.pk}'
    
    
class Series(models.Model):
    """class for series references"""
    name = models.CharField(max_length=100)
    description = models.TextField(
        blank=True,
        null=True
    )


    def __str__(self) -> str:
        return f'{self.name}'

    def get_absolute_url(self):
        return f'/series-detail/{self.pk}'

class Author(models.Model):
    """class for author references"""
    name = models.CharField(max_length=100)
    series = models.ForeignKey(Series, on_delete=models.PROTECT, related_name="authors")
    description = models.TextField(
        blank=True,
        null=True
    )


    def get_absolute_url(self):
        return f'/author-detail/{self.pk}'
    
class Publisher(models.Model):
    """class for publisher references"""
    name = models.CharField(max_length=100)
    description = models.TextField(
        blank=True,
        null=True
    )


    def get_absolute_url(self):
        return f'/publisher-detail/{self.pk}'
    