from .models import Proposal
from django.db import transaction
from .tasks import evaluate_proposal
from .serializers import ProposalSerializer
from rest_framework.response import Response
from rest_framework import viewsets, status, permissions

class ProposalViewSet(viewsets.ModelViewSet):
    queryset = Proposal.objects.all()
    serializer_class = ProposalSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        transaction.on_commit(lambda: evaluate_proposal.delay(serializer.data['id']))

        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
