from django.contrib import admin
from rest import models

# Register Boiler Plate models
class KeywordAdmin(admin.ModelAdmin):
    list_display = ('keyword',
                    'status',
                    'match_type',
                    )

class AdgroupAdmin(admin.ModelAdmin):
    list_display = ('adgroup_name',
                    'status',
                    )

class CampaignAdmin(admin.ModelAdmin):
    list_display = ('campaign_name',
                    'status',
                    )


admin.site.register(models.Account)
admin.site.register(models.Campaign, CampaignAdmin)
admin.site.register(models.AdGroup, AdgroupAdmin)
admin.site.register(models.Keyword, KeywordAdmin)
