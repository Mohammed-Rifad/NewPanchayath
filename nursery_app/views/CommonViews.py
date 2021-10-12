from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from passlib.hash import pbkdf2_sha256
from datetime import date, datetime,timedelta
from ..services import getProductFeatures
from ..models import AdminDetails, CustomerDetails, NurseryProduct
from nursery_app.Forms.CommonForms import LoginForm
from nursery_app.Forms.CustomerForms import CustomerRegForm

def ProjectHome(request):
    return render(request,'Common/ProjectMaster.html')

def Login(request):
    form=LoginForm()
    if request.method=='POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            login_id=form.cleaned_data['login_id']
            login_passwd=form.cleaned_data['login_passwd']
            if(login_id)=='Admin':
                auth_check=AdminDetails.objects.filter(login_id=login_id).exists()
                if auth_check:
                    auth_data=AdminDetails.objects.get(login_id=login_id)
                    auth_passwd=auth_data.verifyPasswd(login_passwd)
                    if auth_passwd:
                      
                        return redirect("e_nursery:admin_home")
                    else:
                        msg="Incorrect Password"
                    return render(request,'Common/CommonLogin.html',{'form':form,'msg':msg,})
                else:
                    msg="Incorrect UserName or Password"
                    
                    return render(request,'Common/CommonLogin.html',{'form':form,'msg':msg,})
            if '@' in login_id:
                auth_check=CustomerDetails.objects.filter(cust_email=login_id).exists()
                if auth_check:
                    auth_data=CustomerDetails.objects.get(cust_email=login_id)
                    auth_passwd=auth_data.verifyPasswd(login_passwd)
                    if auth_passwd:
                        request.session['user_id']=auth_data.cust_id
                        return redirect("e_nursery:cust_home")
                    
                    else:
                        msg="Incorrect Password"
                        return render(request,'Common/CommonLogin.html',{'form':form,'msg':msg,})
                else:
                     msg="Incorrect UserName or Password"
                    
                     return render(request,'Common/CommonLogin.html',{'form':form,'msg':msg,})

    return render(request,'Common/CommonLogin.html',{'form':form})

def AdminData(request):
    passwd=pbkdf2_sha256.hash("admin",rounds=1000,salt_size=32)
    qry=AdminDetails(login_id="Admin",login_passwd=passwd)
    qry.save()
    return redirect("e_nursery:login")

def ViewProducts(request):
    product_type=request.GET['p']

    if product_type=='plt' :id=1
    elif product_type=='pt':id=2
    elif product_type=='std':id=3
    elif product_type=='sd':id=4
    elif product_type=='frt':id=5
    elif product_type=='oth':id=6

    product_list=NurseryProduct.objects.filter(m_id=id)

    for i in product_list:
        print(i.p_img.url)

    return render(request,'Common/ViewProducts.html',{'product_list':product_list,})

def ProductDetails(request,pid):
    product_detail=NurseryProduct.objects.get(p_id=pid)
    cur_date=date.today()
    exp_date1=cur_date+timedelta(days=1)
    exp_date2=cur_date+timedelta(days=product_detail.p_exp_days)
    featuresKey,featuresValue=getProductFeatures(product_detail)
  
    print()
    return render(request,'Common/ProductDetails.html',{'product_detail':product_detail,'exp_date1':exp_date1,'exp_date2':exp_date2,'featuresKey':featuresKey,'featuresValue':featuresValue})


def Cart(request):
    return render(request,'Common/Cart.html')

def CustomerReg(request):
    form=CustomerRegForm()
    if request.method=='POST':
        form=CustomerRegForm(request.POST,request.FILES)
        if form.is_valid():
            cust_name=form.cleaned_data['cust_name'].lower()
            cust_address=form.cleaned_data['cust_address'].lower()
            cust_phno=form.cleaned_data['cust_phno']
            cust_email=form.cleaned_data['cust_email']
            cust_passwd=form.cleaned_data['cust_passwd']
            cust_img=form.cleaned_data['cust_img']
            
            passwd=pbkdf2_sha256.hash(cust_passwd,rounds=1000,salt_size=32)
            customer_exist=CustomerDetails.objects.filter(cust_email=cust_email).exists()
            if not customer_exist:
                qry=CustomerDetails(cust_name=cust_name,cust_address=cust_address,cust_email=cust_email,cust_phno=cust_phno,cust_passwd=passwd,cust_img=cust_img)
                qry.save()
                msg="Customer Added Succesfully"
                return render(request,'Common/CustomerRegister.html',{'form':form,'msg':msg})
            else:
                msg="Customer Already Added"
                return render(request,'Common/CustomerRegister.html',{'form':form,'msg':msg})
    return render(request,'Common/CustomerRegister.html',{'form':form})