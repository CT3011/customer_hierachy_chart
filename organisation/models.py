from django.forms import EmailField
from django.utils.translation import gettext_lazy  as _
from mptt.models import MPTTModel, TreeForeignKey
from django.db.models import CharField, ForeignKey, TextField, DateTimeField, CASCADE, Model, TextChoices
from django.contrib.auth.models import User

from customer.models import Customer

# Create your models here.


class Organisation(MPTTModel):

    class Status(TextChoices):
        ACTIVE = 'A', _('Active')
        DELETED = 'D', _('Deleted')

    status = CharField(default=Status.ACTIVE, max_length=1, choices=Status.choices)
    parent = TreeForeignKey(on_delete=CASCADE, to="self", null=True, blank=True)
    name = CharField(max_length=100)
    address_line_1 = TextField()
    address_line_2 = TextField()
    city = CharField(max_length=200)
    state = CharField(max_length=200) 
    country = CharField(max_length=200) 
    pincode = CharField(max_length=200)
    email = EmailField() 
    conatact_no = CharField(max_length=15)
    created_by = ForeignKey(User, on_delete=CASCADE, related_name='organisations')
    created_at = DateTimeField(auto_now_add=True)
    updated_by = ForeignKey(User,  on_delete=CASCADE, related_name='updated_organisations', null=True, blank=True)
    update_at = DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.pk}: {self.name}"
    



class OrgCustomer(Model):
    class Status(TextChoices):
        ACTIVE = 'A', _('Active')
        DELETED = 'D', _('Deleted')

    status = CharField(default=Status.ACTIVE, max_length=1, choices=Status.choices)
    customer = ForeignKey(Customer, on_delete=CASCADE, blank=True, null=True, related_name='org_customer')
    organisation = ForeignKey(Organisation, on_delete=CASCADE, related_name='org_customer')
    created_by = ForeignKey(User, on_delete=CASCADE, related_name='orgcustomer')
    created_at = DateTimeField(auto_now_add=True)
    updated_by = ForeignKey(User,  on_delete=CASCADE, related_name='updated_orgcustomer', null=True, blank=True)
    update_at = DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.customer}{self.organisation}"