from django.db import models
from django.db.models import Q
from model_utils import Choices

ORDER_COLUMN_CHOICES = Choices(
    ('0', 'id'),
    ('1', 'keyword'),
    ('2', 'status'),
    ('3', 'match_type'),
)

# Account
class Account(models.Model):    
    account_name = models.CharField(max_length=128)

    def __str__(self):
        return self.account_name

# Campaign
class Campaign(models.Model):
    class Status(models.TextChoices):
        Enabled = "Enabled"
        Paused = "Paused"

    account = models.ForeignKey(
       to=Account, on_delete=models.CASCADE, related_name='campaigns'
      )
    campaign_name = models.CharField(max_length=128)
    status = models.CharField(max_length=21, choices=Status.choices, default=Status.Paused)

    def __str__(self):
        return self.campaign_name

# AdGroup
class AdGroup(models.Model):
    class Status(models.TextChoices):
        Enabled = "Enabled"
        Paused = "Paused"

    campaign = models.ForeignKey(
       to=Campaign, on_delete=models.CASCADE, related_name='adgroups'
      )
    adgroup_name = models.CharField(max_length=128)
    status = models.CharField(max_length=21, choices=Status.choices, default=Status.Enabled)

    def __str__(self):
        return self.adgroup_name

# Keyword
class Keyword(models.Model):
    class Status(models.TextChoices):
        Enabled = "Enabled"
        Paused = "Paused"

    class MatchType(models.TextChoices):
        Exact = "Exact"
        Phrase = "Phrase"
        Broad = "Broad"

    adgroup = models.ForeignKey(
       to=AdGroup, on_delete=models.CASCADE, related_name='keywords'
      )
    keyword = models.CharField(max_length=128)
    status = models.CharField(max_length=21, choices=Status.choices, default=Status.Enabled)
    match_type = models.CharField(max_length=21, choices=MatchType.choices, default=MatchType.Exact)

    def __str__(self):
        return self.keyword


