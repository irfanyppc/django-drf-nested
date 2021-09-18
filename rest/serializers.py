from rest_framework import serializers
from . import models
from rest_framework_nested.relations import *
from rest_framework_nested.serializers import NestedHyperlinkedModelSerializer


class AccountSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = models.Account
        fields = ( '__all__' )


class CampaignSerializer(NestedHyperlinkedModelSerializer):
    parent_lookup_kwargs = {
        'account_pk': 'account__pk',
   }

    class Meta:
        model = models.Campaign
        fields = ( '__all__' )


class AdGroupSerializer(serializers.ModelSerializer):

    parent_lookup_kwargs = {
        'campaign_pk': 'campaign__pk',
        'account_pk': 'campaign__acccount__pk',
    }

    class Meta:
        model = models.AdGroup
        fields = ('__all__')

