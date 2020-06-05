from django.conf.urls import url
from . import views
from .views import ItemList,RegisterationView,LoginView,LogoutView

urlpatterns = [
    url('^$', views.index, name = 'index'),
    url('addUser/', RegisterationView.as_view(), name="register"),
    url('login/', LoginView.as_view(), name="login"),
    url('logout/', LogoutView.as_view(), name="logout"),
    url('^contact$', views.contact, name = 'contact'),
    url('^index$', views.index, name = 'index'),
    url('^about$', views.about, name = 'about'),
    url('^demo', views.demo, name = 'demo'),
    url('^item', views.item, name = 'item'),
    url('^payment', views.payment, name = 'payment'),
    url('Item', ItemList.as_view(), name='Item'),
]

