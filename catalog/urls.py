from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import ProductListView, Product2ListView, ProductDetailView, ContactsPageVeiw
app_name = CatalogConfig.name
urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
    path('contacts/', ContactsPageVeiw.as_view(), name='contacts'),
    path('product/', Product2ListView.as_view(), name='product'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail')
]
