from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework import routers

from game_app.api import *
admin.autodiscover()


router = routers.DefaultRouter()

router.register(r'referee',RefereeViewSet)
router.register(r'first_round',RefereeViewSet)
# router.register(r'second_match',RefereeViewSet)
# router.register(r'third__match',RefereeViewSet)
# router.register(r'fourth_match',RefereeViewSet)
# router.register(r'semifinal_match_1',RefereeViewSet)
# router.register(r'semifinal_match_2',RefereeViewSet)
# router.register(r'final_match',RefereeViewSet)
# router.register(r'result',RefereeViewSet)


urlpatterns = patterns('',
    url(r'^', include(router.urls)),

    # Examples:
    # url(r'^$', 'ping_pong.views.home', name='home'),
    # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # url(r'^', include('game_app.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
