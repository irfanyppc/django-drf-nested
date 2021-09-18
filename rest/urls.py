from django.urls import include, path
from rest_framework_nested import routers
from . import views



router = routers.SimpleRouter()
router.register(r'accounts', views.AccountViewset)
## generates:
# /accounts/
# /accounts/{pk}/


campaign_router = routers.NestedSimpleRouter( router, r'accounts', lookup='account')
campaign_router.register(r'campaigns', views.CampaignViewset)
## generates:
# /accounts/{pk}/campaigns/
# /accounts/{pk}/campaigns/{pk}/

adgroup_router = routers.NestedSimpleRouter(campaign_router, r'campaigns', lookup='campaign')
adgroup_router.register(r'adgroups', views.AdGroupViewset)
## generates:
# /accounts/{pk}/campaigns/{pk}/adgroups/
# /accounts/{pk}/campaigns/{pk}/adgroups/{pk}/



urlpatterns = [
    path(r'', include(router.urls)),
    path(r'', include(campaign_router.urls)),
    path(r'', include(adgroup_router.urls)),
]