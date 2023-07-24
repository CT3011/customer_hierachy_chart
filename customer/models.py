from django.db.models import ForeignKey, Model, CASCADE, CharField
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User

# Create your models here.
class Customer(Model):
    user = ForeignKey(User, verbose_name=_("User"), on_delete=CASCADE, related_name='customers')
    contact = CharField(max_length=15, verbose_name=_('Contact number'))


    def __str__(self):
        return f"{self.user.username}"
