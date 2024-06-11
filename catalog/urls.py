from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import ProductListView, Product2ListView, ProductDetailView, ContactsPageVeiw, ProductCreateView, \
    ProductUpdateView, ProductDeleteView

app_name = CatalogConfig.name
urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
    path('contacts/', ContactsPageVeiw.as_view(), name='contacts'),
    path('product/', Product2ListView.as_view(), name='product'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('create/', ProductCreateView.as_view(), name='create'),
    path('edit/<int:pk>/', ProductUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>/', ProductDeleteView.as_view(), name='delete')
]
