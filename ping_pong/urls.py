from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework import routers

from game_app.api import FirstRoundViewSet,SecondRoundViewSet, ThirdRoundViewSet, RefereeViewSet, AddUserViewSet

admin.autodiscover()


router = routers.DefaultRouter()

# router.register(r'referee',RefereeViewSet,base_name='referee')
router.register(r'first_round',FirstRoundViewSet,'first_round')
router.register(r'add_user',AddUserViewSet)
router.register(r'second_round',SecondRoundViewSet,base_name='second round')
router.register(r'third_round',ThirdRoundViewSet,base_name="third round")


urlpatterns = patterns('',
    url(r'^', include(router.urls)),

    # Examples:
    # url(r'^$', 'ping_pong.views.home', name='home'),
    # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # url(r'^', include('game_app.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
