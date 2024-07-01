from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.apps import CatalogConfig
from catalog.views import ProductListView, Product2ListView, ProductDetailView, ContactsPageVeiw, ProductCreateView, \
    ProductUpdateView, ProductDeleteView, CategoryListView

app_name = CatalogConfig.name
urlpatterns = [
    path('', cache_page(60)(ProductListView.as_view()), name='home'),
    path('contacts/', ContactsPageVeiw.as_view(), name='contacts'),
    path('product/', Product2ListView.as_view(), name='product'),
    path('product/<int:pk>/', cache_page(60)(ProductDetailView.as_view()), name='product_detail'),
    path('create/', ProductCreateView.as_view(), name='create'),
    path('edit/<int:pk>/', ProductUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>/', ProductDeleteView.as_view(), name='delete'),
    path('category/', CategoryListView.as_view(), name='category'),
]
