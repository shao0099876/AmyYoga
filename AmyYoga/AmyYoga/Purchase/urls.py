from django.urls import path, include
from .views import *

unpayedpatterns = {
    path('', uncustomercourse),
    path('cancel/<number>/', cancelorder),
}
customerpatterns = {
    path('payed/', customercourse),
    path('unpayed/', include(unpayedpatterns)),
}
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
    path('view/mks/', purchase),
    path('scene/', include(scenepattern)),
    path('manage/', include(managepattern)),
    path('customer/', include(customerpatterns)),
}
