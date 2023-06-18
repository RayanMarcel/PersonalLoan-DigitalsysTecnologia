from .models import Proposal
from django.contrib import admin

class ProposalAdmin(admin.ModelAdmin):
    list_display = ('pk', 'full_name', 'cpf', 'loan_value', 'status', 'reviewed')

admin.site.register(Proposal, ProposalAdmin)

