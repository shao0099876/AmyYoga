from django.urls import path, include
from .views import *

scenepattern = {
    path('', buycourse),
    path('make/', makebuycourse)

}
managepattern = {
    path('', showtherecord),
    path('<int:recordid>/', detailrecord),
    path('confirm/<int:cord>/', makerecord),
    path('cancel/<int:discord>/', canclerecord)
}
urlpatterns = {
    path('view/', purchaseCourse),
    path('<course>/', purchase),
    path('scene/', include(scenepattern)),
    path('manage/', include(managepattern))
}
