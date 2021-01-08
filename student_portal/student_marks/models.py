from django.db import models
from django.urls import reverse
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Marks(models.Model):
    rollno = models.PositiveSmallIntegerField(unique=True, validators=[MinValueValidator(1),
                                            MaxValueValidator(200)])
    name = models.CharField(max_length=200)
    maths = models.PositiveSmallIntegerField(validators=[MinValueValidator(0),
                                            MaxValueValidator(100)])
    physics = models.PositiveSmallIntegerField(validators=[MinValueValidator(0),
                                            MaxValueValidator(100)])
    chemistry = models.PositiveSmallIntegerField(validators=[MinValueValidator(0),
                                            MaxValueValidator(100)])
    total = models.PositiveSmallIntegerField(blank=True, null=True)
    percentage = models.FloatField(blank=True, null=True)
    
    def save(self, *args, **kwargs):
        self.total = self.maths+self.physics+self.chemistry
        self.percentage = round(self.total/3, 2)
        super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse("success", kwargs={'pk':self.pk})

    def __str__(self):
        return self.name


