
from django.shortcuts import render, get_object_or_404

from rest_framework import viewsets, status
from rest_framework.response import Response

from .serializers import  *
from . import models


class AccountViewset(viewsets.ModelViewSet):
    serializer_class = AccountSerializer    
    queryset = models.Account.objects.all()    


class CampaignViewset(viewsets.ModelViewSet):
    serializer_class = CampaignSerializer    
    queryset = models.Campaign.objects.all()    
    
    def get_queryset(self):
         return models.Campaign.objects.filter(account=self.kwargs['account_pk'])


class AdGroupViewset(viewsets.ModelViewSet):
    serializer_class = AdGroupSerializer    
    queryset = models.AdGroup.objects.all()    

    def get_queryset(self):
        return models.AdGroup.objects.filter(campaign=self.kwargs['campaign_pk'],
                                            campaign__account=self.kwargs['account_pk']
                                            )

