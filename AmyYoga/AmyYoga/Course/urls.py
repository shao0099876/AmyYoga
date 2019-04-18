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
adminpatterns = {
    path('', admin_coursemessage),
    path('<coursename>/', Coursename),
}
modifypatterns = {
    path('', modifycourse),
    path('<coursename>/', ModCourse),
}
deletepatterns = {
    path('', deletecourse),
    path('<coursename>/', DelCourse),
}
restorepatterns = {
    path('', readdcourse),
    path('<coursename>/', reAddCourse),
}
urlpatterns = {
    path('customer/', include(customerpatterns)),
    path('admin/', include(adminpatterns)),
    path('add/', addcourse),
    path('modify/', include(modifypatterns)),
    path('delete/', include(deletepatterns)),
    path('restore/', include(restorepatterns)),
}
