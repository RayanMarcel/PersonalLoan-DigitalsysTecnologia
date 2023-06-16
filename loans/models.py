from django.db import models
from .choices import STATUS_CHOICES

class Proposal(models.Model):
    full_name = models.CharField(max_length=200)
    cpf = models.CharField(max_length=14)
    address = models.CharField(max_length=400)
    loan_value = models.DecimalField(max_digits=15, decimal_places=2)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='PENDING')
    reviewed = models.BooleanField(default=False)
