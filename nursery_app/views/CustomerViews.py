from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from ..models import CustomerDetails, NurseryProduct,CartDetails
from datetime import date, datetime,timedelta
from ..services import AddToCart, getProductFeatures

def CustomerHome(request):
    return render(request,'Customer/CustomerHome.html')

def ViewProducts(request):
    product_type=request.GET['p']

    if product_type=='plt' :id=1
    elif product_type=='pt':id=2
    elif product_type=='std':id=3
    elif product_type=='sd':id=4
    elif product_type=='frt':id=5
    elif product_type=='oth':id=6

    product_list=NurseryProduct.objects.filter(m_id=id)
    return render(request,'Customer/ViewProducts.html',{'product_list':product_list,})


def ProductDetails(request,pid):
    product_detail=NurseryProduct.objects.get(p_id=pid)
    cur_date=date.today()
    exp_date1=cur_date+timedelta(days=1)
    exp_date2=cur_date+timedelta(days=product_detail.p_exp_days)
    featuresKey,featuresValue=getProductFeatures(product_detail)
  
    if request.method=="POST":
        user=CustomerDetails.objects.get(cust_id=request.session['user_id'])
        qty=request.POST['txtQty']
        AddToCart(pid,user,qty)
        return render(request,'Customer/ProductDetails.html',{'product_detail':product_detail,'exp_date1':exp_date1,'exp_date2':exp_date2,'featuresKey':featuresKey,'featuresValue':featuresValue})
    
    
    return render(request,'Customer/ProductDetails.html',{'product_detail':product_detail,'exp_date1':exp_date1,'exp_date2':exp_date2,'featuresKey':featuresKey,'featuresValue':featuresValue})

def Cart(request):
    
   
    if request.method=='POST':
        if 'update' in request.POST:
            pr_id=request.POST['pr_id']
            product_data=NurseryProduct.objects.get(p_id=pr_id)
            cart_data=CartDetails.objects.get(nursery_product=pr_id,cust_id=request.session['user_id'])
            qty=request.POST['qty']
            cart_data.qty=qty
            cart_data.total=product_data.p_price * int(qty)
            cart_data.save()
        
        # if 'remove' in request.POST:
        #     pr_id=request.POST['pr_id']
        #     user_id=request.session['user_id']
        #     cart_product=CartDetails.objects.get(nursery_product=pr_id,cust_id=request.session['user_id'])
        #     cart_product.delete()
    total=0
    cart_list=CartDetails.objects.filter(cust_id=request.session['user_id'])
    for product in cart_list:
        total=total+product.total
    
    return render(request,'Customer/Cart.html',{'cart_list':cart_list,'total':total})