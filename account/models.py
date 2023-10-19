from django.db import models
from django.conf import settings
from django.templatetags.static import static
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True , null=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d/', default=static('defaults/default.png'))

    def __Str__(self):
        return f'Profile of {self.user.username}'