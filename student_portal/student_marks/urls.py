from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.HomePage.as_view(), name = 'home'),
    url(r'^entermarks/$', views.EnterMarksView.as_view(), name='enter_marks'),
    url(r'^success/(?P<pk>\d+)$', views.Success.as_view(), name='success'),
    url(r'^leaderboard/$',views.MarksListView.as_view(), name = 'leaderboard'),
]