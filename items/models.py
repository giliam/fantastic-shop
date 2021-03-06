from django.db import models

class Item(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, blank=True, default='')
    owner = models.ForeignKey('auth.User', related_name='items')
    
    class Meta:
        ordering = ('created',)
