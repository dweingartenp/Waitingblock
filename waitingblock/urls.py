from django.conf.urls import url
from django.urls import include, path
from waitingblock.views import WaitingblockView, CustomerUpdateView, TablesView
from . import views


#urlpatterns = [
#    url(r'^$', WaitingblockView.as_view(), name='home', ),
#    url(r'^update/', CustomerUpdateView.as_view(), name='status_update', ),
#    url(r'^update/(?P<pk>\d+)/$', CustomerUpdateView.as_view(), name='status_update', ),
#    url(r'^tables/', TablesView.as_view(), name='tables', ),
#]

urlpatterns = [
    path('', WaitingblockView.as_view(), name='home'),
    path('success/', WaitingblockView.redirect_view),
    path('update/', CustomerUpdateView.as_view(), name='status_update'),
#    path('update/<int:id>/', CustomerUpdateView.as_view(), name='status_update'),
#    path('update/success/', WaitingblockView.redirect_view),
    path('tables/', TablesView.as_view(), name='tables'),
]
