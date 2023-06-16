from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Proposal
from .serializers import ProposalSerializer
from .tasks import evaluate_proposal

class ProposalViewSet(viewsets.ModelViewSet):
    queryset = Proposal.objects.all()
    serializer_class = ProposalSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        evaluate_proposal.delay(serializer.data['id'])

        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
