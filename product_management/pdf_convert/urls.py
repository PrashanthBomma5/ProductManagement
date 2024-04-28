from django.urls import path
from .import views
urlpatterns=[
    path('showproducts',views.show_products,name='showproductss'),
    path('createpdf',views.render_pdf_view,name='createpdf'),
]