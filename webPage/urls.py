from django.urls import path

from webPage.views import MainIndex

urlpatterns = [
    path('', MainIndex.as_view(), name='index'),

]
