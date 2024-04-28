from django.urls import path
from products import views
urlpatterns = [
    path('',views.ShowAllProducts,name='showproducts'),
    path('product/<int:pk>',views.productDetail,name='productDetail'),
    path('addProdcut',views.addProduct,name='addProcduct'),
    path('updateproduct/<int:pk>',views.updateProduct,name='updateproduct'),
    path('deleteproduct/<int:pk>',views.deleteproduct,name='deleteproduct'),
    path('searchbar',views.searchBar,name='searchbar'),
]
