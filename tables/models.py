from django.db import models

# Create your models here.


class TablesModel(models.Model):
    """ A model to create a booking """
    name = models.CharField(max_length=50, null=False, blank=False)
    email = models.CharField(max_length=50, null=False, blank=False)
    phone = models.CharField(max_length=50, null=False, blank=False)
    guests = models.IntegerField(null=False, blank=False)
    datetime = models.DateTimeField(null=False, blank=False)
    message = models.CharField(max_length=200)

    class Meta:
        """ Verbose name for admin """
        verbose_name_plural = 'Evening Tables'

    def __str__(self):
        return f"{self.name} - {self.email}"