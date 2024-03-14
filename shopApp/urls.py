from django.conf.urls import url
from shopApp import views

urlpatterns = [
    url(r'^prd/$',views.ShopAPI),
    url(r'^prd/([0-9]+)$',views.ShopAPI),
    url(r'^order/$',views.OrderAPI),
    url(r'^order/([0-9]+)$',views.OrderAPI),
    url(r'^products-ordered/$', views.product_list_ordered),
]