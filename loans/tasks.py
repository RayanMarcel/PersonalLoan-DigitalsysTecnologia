from celery import shared_task
from .models import Proposal

@shared_task
def evaluate_proposal(proposal_id):
    proposal = Proposal.objects.get(id=proposal_id)

    total_proposals = Proposal.objects.filter(reviewed=True).count()
    approved_proposals = Proposal.objects.filter(status='APPROVED').count()

    if approved_proposals < total_proposals / 2:
        proposal.status = 'APPROVED'
    else:
        proposal.status = 'DENIED'
    
    proposal.reviewed = True
    proposal.save()
