from django.db import models
from django.utils.translation import ugettext_lazy as _
from main.models import User
from djmoney.models.fields import MoneyField
# Create your models here.
class Event(models.Model):
    owner=models.ForeignKey(User,on_delete=models.CASCADE)
    description=models.TextField(_('event description'),)
    title=models.CharField(_('event title'),max_length=200)
    cover=models.ImageField(_('event cover'),upload_to="events/",null=True,blank=True)
    price=MoneyField(_('event price'),max_digits=10,decimal_places=2,default=0,default_currency='XOF')
    location=models.CharField(_('event location'),max_length=200)
    date=models.DateTimeField(_('event date'),auto_now_add=True)
    creation_date=models.DateTimeField(_('event creation date'),auto_now_add=True)
    available_place=models.CharField(_('available places'),max_length=10)
    sells=models.IntegerField(default=0)

    def __str__(self):
        return self.title

class Ticket(models.Model):
    event=models.ForeignKey(Event, on_delete=models.CASCADE)
    customer=models.ForeignKey(User,on_delete=models.CASCADE)
    application_date=models.DateTimeField(auto_now=True)
    number=models.CharField(max_length=200)

    def __str__(self):
        return self.event
