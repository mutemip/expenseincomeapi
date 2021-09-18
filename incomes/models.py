from django.db import models
from authorization.models import User

# Create your models here.
class Income(models.Model):
    SOURCE_OPTIONS = {
        ('SALARY', 'SALARY'),
        ('BUSINESS', 'BUSINESS'),
        ('SIDE_HUSTLES', 'SIDE_HUSTLES'),
        ('OTHERS', 'OTHERS')
    }
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    source = models.CharField(max_length=255, choices=SOURCE_OPTIONS)
    amount = models.DecimalField(max_digits=10, decimal_places=2, max_length=255)
    description = models.TextField()
    date = models.DateField(blank=False, null=False)

    class Meta:
        ordering: ['-date']

    def __str__(self):
        return str(self.owner) + 's income'