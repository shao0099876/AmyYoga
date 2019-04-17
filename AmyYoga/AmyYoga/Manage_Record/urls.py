from django.urls import path
from . import  views
urlpatterns = {
    path('', views.showtherecord),
    path('<int:recordid>', views.detailrecord),
    path('<int:cord>/mks', views.makerecord,name='makesure'),
    path('<int:discord>/dis', views.canclerecord,name='canclesure'),
}