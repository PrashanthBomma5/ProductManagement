from django.shortcuts import render,redirect
from .forms import ProductForm
from .models import Product,Category
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.contrib.auth.decorators import login_required


# Create your views here.

# to view all the product in the showproducts.html
# @login_required(login_url='accounts/login')
# def ShowAllProducts(request):

#     category= request.GET.get('category')  # get the clicked category
#     if category == None:  
#         products = Product.objects.filter(is_published=True).order_by('price')  #DB--> Table
#     else:  
#         products = Product.objects.filter(category__name=category)


#     categories =Category.objects.all()
#     number_of_products=Product.objects.all().count()
#     page_num = request.GET.get('pages')  #creating the total pages
#     paginator = Paginator(products,3)  #setting total no products in a page
    

#     try:
#         products = paginator.page(page_num)
#     except PageNotAnInteger:
#         products=paginator.page(1)
#     except EmptyPage:
#         products = paginator.page(paginator.num_pages)

#     context={
#         'products':products,
#         'number_of_products':number_of_products,
#         'categories':categories,
#     }
#     return render(request,'showProducts.html',context)
@login_required(login_url='accounts/login')
def ShowAllProducts(request):

    # Get the category filter from the URL parameters
    category_name = request.GET.get('category')

    # If no category filter is applied, show all products
    if category_name is None:
        products = Product.objects.filter(is_published=True).order_by('price')
    else:
        # Filter products based on the selected category
        products = Product.objects.filter(category__name=category_name, is_published=True).order_by('price')

    # Get all categories for navigation
    categories = Category.objects.all()
    number_of_products = Product.objects.all().count()

    # Pagination
    page_num = request.GET.get('page')
    paginator = Paginator(products, 3)

    try:
        products = paginator.page(page_num)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    context = {
        'products': products,
        'number_of_products': number_of_products,
        'categories': categories,
    }
    return render(request, 'showProducts.html', context)

# to view single productdeatails in the productdetails.html
@login_required(login_url='showproducts')
def productDetail(request,pk):
    eachproduct=Product.objects.get(id=pk)
    context={ 
        'eachproduct':eachproduct,
    }
    return render(request,'productDetail.html',context)

# to add the new productdeatil from the html template page
@login_required(login_url='showproducts')
def addProduct(request):
    form  = ProductForm()

    if request.method == 'POST':
        form = ProductForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('showproducts')

    context ={
        'form':form
    }
    return render(request,'addProduct.html',context)

#to update the product form from the HTML template page,updateproduct.html
@login_required(login_url='showproducts')
def  updateProduct(request,pk):
    product=Product.objects.get(id=pk)
    form = ProductForm(instance=product)
    if request.method == 'POST':
        form=ProductForm(request.POST,request.FILES,instance=product)
        if form.is_valid():
            form.save()
            return redirect('showproducts')
    context={
        'form':form

    }
    return render(request,'updateProducts.html',context)

# deleting the record from the databse from the table ,based on the primary key or unique key
@login_required(login_url='showproducts')
def deleteproduct(request,pk):
    product = Product.objects.get(id=pk)
    product.delete()
    return redirect('showproducts')

# creating a function for searching the data from the database using the  keyword
@login_required(login_url='showproducts')
def searchBar(request):
    if request.method == 'GET': #get = GET =>True 
        query = request.GET.get('query') #query =  ex:999
        if query:
            products = Product.objects.filter(price__contains = query)
            return render(request,'search.html',{'products':products})
        else:
            print('no products to found in the database')
            return render(request,'search.html',{})
        


