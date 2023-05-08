from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from brookwoodapp.models import Log, brookuser,product, category, complaint, Review
from brookwoodapp import models
import decimal
# Create your views here.


def admin_dashboard(request):
    return render(request,'Admin_dashboard.html')

def admin_view_complaint_report(request):
    data=complaint.objects.all()
    return render(request,'view_complaints_and_reply.html',{'data':data})

def admin_single_complaints(request,id):
    Data = complaint.objects.get(id=id)
    return render(request,'admin_replay.html',{'Data':Data})

def admin_add_replay(request,id):
    if request.method=="POST":
        add=complaint.objects.get(id=id)
        add.replay=request.POST["replay"]
        add.complaint_status="1"
        add.save()
        return redirect("admin_view_complaint_report")

def admin_view_bill_report(request):
    return render(request,'bill_report.html')

def admin_view_feedback(request):
    data=Review.objects.all()
    return render(request,'admin_view_feedback.html',{'data':data})    

def admin_add_product(request):
    return render(request,'add_product.html')

def admin_view_product(request):
    return render(request,'view_product.html')

def admin_login(request):
    return render(request,'page-login.html')

# def login_admin(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate(username=username,password=password)
#         print(user)

#         if user is not None and username=="admin" and password=="admn":
#             login(request,user)
#             return render(request,'Admin_dashboard.html')
#         else:
#             messages.info(request,'Invalid Credentials')
#             return redirect('admin_login')
                
#     else:
#         return render(request, 'page-login.html')


def admin_view_users(request):
    data=brookuser.objects.all()
    print(data)
    return render(request,"users.html",{'data':data})



def admin_add_all_product(request):
    if request.method == 'POST':
        category_name = request.POST.get('category_name')
        product_name = request.POST.get('product_name')
        prices = request.POST.get('price')
        price=int(prices)
        GSTs = request.POST.get('GST')
        GST=int(GSTs)
        T_priceS = price * GST / 100
        T_price=int(T_priceS)
        price_total = T_price+price
        product_details = request.POST.get('product_details')
        image = request.FILES['image']
        stock = request.POST.get('stock')
        
        product_status = '0'

        ProductDetails = models.product(category=category_name,product_name=product_name, price=price,GST=GST,product_price=price_total,product_details=product_details,image=image,stock=stock,product_status=product_status)
        ProductDetails.save()
            
        return redirect('admin_view_product')
    else:
        return render(request, 'Add_Product.html')



def admin_view_all_product(request):
    data=product.objects.all()
    print(data)
    return render(request,"view_product.html",{'data':data})



def admin_delete_product(request,id):
    delmember = product.objects.get(id=id)
    print(delmember)
    delmember.delete()
    return redirect('admin_view_all_product')


def admin_edit_product(request,id):
    Data = product.objects.get(id=id)
    return render(request,'admin_edit_products.html',{'Data':Data})


def productformupdate(request,id):
    if request.method=="POST":
        add=product.objects.get(id=id)
        add.product_name=request.POST["product_name"]
        add.price=request.POST["price"]
        add.GST=request.POST["GST"]
        add.product_details=request.POST["product_details"]
        add.stock=request.POST["stock"]
        add.save()
        return redirect("admin_view_all_product")


def admin_edit_product(request,id):
    Data = product.objects.get(id=id)
    return render(request,'admin_edit_products.html',{'Data':Data})


def admin_add_category_page(request):
    return render(request,'admin_add_category.html')


def admin_add_category(request):
    if request.method == 'POST':
        category_name = request.POST.get('category_name')
        category_status = '0'

        CategoryDetails = models.category(category_name=category_name,category_status=category_status)
        CategoryDetails.save()
            
        return render(request,'view_product.html')
    else:
        return render(request, 'admin_add_category.html')