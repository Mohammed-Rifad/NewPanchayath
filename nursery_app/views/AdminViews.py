from nursery_app.models import MainCategory
from django.forms.widgets import SelectDateWidget
from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from nursery_app.Forms.AdminForms import *

def AdminHome(request):
    return render(request,'Admin/AdminHome.html')


def AddCategory(request):
    form=CategoryForm()
    main_cat=MainCategory.objects.all()
    if request.method=='POST':
        form=CategoryForm(request.POST,request.FILES)
        if form.is_valid():
            m_id=MainCategory.objects.get(m_id=request.POST['main_cat'])
            c_name=form.cleaned_data['c_name'].lower()
            c_desc=form.cleaned_data['c_desc'].lower()
            c_img=form.cleaned_data['c_img']

            cat_exist=CategoryDetails.objects.filter(m_id=m_id,c_name=c_name).exists()
            if not cat_exist:
                qry=CategoryDetails(m_id=m_id,c_name=c_name,c_desc=c_desc,c_img=c_img)
                qry.save()
                msg="Category Added Succesfully"
                return render(request,'Admin/AddCategory.html',{'form':form,'msg':msg,'main_cat':main_cat})
            else:
                msg="Category Already Added"
                return render(request,'Admin/AddCategory.html',{'form':form,'msg':msg,'main_cat':main_cat})
        else:
            print(form.errors)
    return render(request,'Admin/AddCategory.html',{'form':form,'main_cat':main_cat})

def AddNurseryPlants(request):
    form=NurseryPlantsForm()
    categories=CategoryDetails.objects.filter(m_id=1)
    if request.method=='POST':
        form=NurseryPlantsForm(request.POST,request.FILES)
        if form.is_valid():
            cat_id=CategoryDetails.objects.get(c_id=request.POST['cat'])
            m_id=MainCategory.objects.get(m_id=1)
            p_name=form.cleaned_data['p_name'].lower()
            p_desc=form.cleaned_data['p_desc'].lower()
            p_dimension=form.cleaned_data['p_dimension']
            p_sales_package=form.cleaned_data['p_sales_package'].lower()
            p_container=form.cleaned_data['p_container'].lower()
            p_caring_tips=form.cleaned_data['p_caring_tips'].lower()
            p_price=form.cleaned_data['p_price']
            p_stock=form.cleaned_data['p_stock']
            p_exp_days=form.cleaned_data['p_exp_days']
            p_img=form.cleaned_data['p_img']

            product_exist=NurseryProduct.objects.filter(cat_id=request.POST['cat'],p_name=p_name).exists()
            if not product_exist:
                qry=NurseryProduct(cat_id=cat_id,m_id=m_id,p_name=p_name,p_desc=p_desc,p_dimension=p_dimension,p_sales_package=p_sales_package,p_container=p_container,p_caring_tips=p_caring_tips,p_price=p_price,p_exp_days=p_exp_days,p_stock=p_stock,p_img=p_img)
                qry.save()
                msg="Product Added Succesfully"
                return render(request,'Admin/AddPlants.html',{'form':form,'categories':categories,'msg':msg})
            else:
                msg="Product Already Added"
                return render(request,'Admin/AddPlants.html',{'form':form,'categories':categories,'msg':msg})
  
    return render(request,'Admin/AddPlants.html',{'form':form,'categories':categories})

def AddPots(request):
    form=PotsForm()
    categories=CategoryDetails.objects.filter(m_id=2)
    if request.method=='POST':
        form=PotsForm(request.POST,request.FILES)
        if form.is_valid():
            cat_id=CategoryDetails.objects.get(c_id=request.POST['cat'])
            m_id=MainCategory.objects.get(m_id=2)
            p_name=form.cleaned_data['p_name'].lower()
            p_desc=form.cleaned_data['p_desc'].lower()
            p_dimension=form.cleaned_data['p_dimension']
            p_sales_package=form.cleaned_data['p_sales_package'].lower()
            p_color=form.cleaned_data['p_color'].lower()
            p_location=form.cleaned_data['p_location'].lower()
            p_price=form.cleaned_data['p_price']
            p_material=form.cleaned_data['p_material']
            p_stock=form.cleaned_data['p_stock']
            p_exp_days=form.cleaned_data['p_exp_days']
            p_img=form.cleaned_data['p_img']

            product_exist=NurseryProduct.objects.filter(cat_id=request.POST['cat'],p_name=p_name).exists()
            if not product_exist:
                qry=NurseryProduct(cat_id=cat_id,m_id=m_id,p_name=p_name,p_desc=p_desc,p_material=p_material,p_dimension=p_dimension,p_sales_package=p_sales_package,p_color=p_color,p_location=p_location,p_price=p_price,p_exp_days=p_exp_days,p_stock=p_stock,p_img=p_img)
                qry.save()
                msg="Product Added Succesfully"
                return render(request,'Admin/AddPots.html',{'form':form,'categories':categories,'msg':msg})
            else:
                msg="Product Already Added"
                return render(request,'Admin/AddPots.html',{'form':form,'categories':categories,'msg':msg})
        else:
            print(form.errors)
    return render(request,'Admin/AddPots.html',{'form':form,'categories':categories,})

def AddStands(request):
    form=StandForm()
    categories=CategoryDetails.objects.filter(m_id=3)
    if request.method=='POST':
        form=StandForm(request.POST,request.FILES)
        if form.is_valid():
            cat_id=CategoryDetails.objects.get(c_id=request.POST['cat'])
            m_id=MainCategory.objects.get(m_id=3)
            p_name=form.cleaned_data['p_name'].lower()
            p_desc=form.cleaned_data['p_desc'].lower()
            p_dimension=form.cleaned_data['p_dimension']
            p_sales_package=form.cleaned_data['p_sales_package'].lower()
            p_color=form.cleaned_data['p_color'].lower()
            p_shape=form.cleaned_data['p_shape'].lower()
            p_location=form.cleaned_data['p_location'].lower()
            p_price=form.cleaned_data['p_price']
            p_stock=form.cleaned_data['p_stock']
            p_exp_days=form.cleaned_data['p_exp_days']
            p_img=form.cleaned_data['p_img']


            product_exist=NurseryProduct.objects.filter(cat_id=request.POST['cat'],p_name=p_name).exists()
            if not product_exist:
                qry=NurseryProduct(cat_id=cat_id,m_id=m_id,p_name=p_name,p_shape=p_shape,p_desc=p_desc,p_dimension=p_dimension,p_sales_package=p_sales_package,p_color=p_color,p_location=p_location,p_price=p_price,p_exp_days=p_exp_days,p_stock=p_stock,p_img=p_img)
                qry.save()
                msg="Product Added Succesfully"
                return render(request,'Admin/AddStands.html',{'form':form,'categories':categories,'msg':msg})
            else:
                msg="Product Already Added"
                return render(request,'Admin/AddStands.html',{'form':form,'categories':categories,'msg':msg})
        else:
            print(form.errors)
    return render(request,'Admin/AddStands.html',{'form':form,'categories':categories,})


def AddFertilizers(request):
    categories=CategoryDetails.objects.filter(m_id=5)
    form=FertilizersForm()
    if request.method=='POST':
        form=FertilizersForm(request.POST,request.FILES)
        if form.is_valid():
            cat_id=CategoryDetails.objects.get(c_id=request.POST['cat'])
            m_id=MainCategory.objects.get(m_id=5)
            p_name=form.cleaned_data['p_name']
            p_desc=form.cleaned_data['p_desc']
            p_sales_package=form.cleaned_data['p_sales_package']
            p_suitable_for=form.cleaned_data['p_suitable_for']
            p_type=form.cleaned_data['p_type']
            p_price=form.cleaned_data['p_price']
            p_stock=form.cleaned_data['p_stock']
            p_exp_days=form.cleaned_data['p_exp_days']
            p_img=form.cleaned_data['p_img']
            product_exist=NurseryProduct.objects.filter(cat_id=cat_id,p_name=p_name).exists()
            if not product_exist:
                qry=NurseryProduct(cat_id=cat_id,m_id=m_id,p_name=p_name,p_desc=p_desc,p_suitable_for=p_suitable_for,p_type=p_type,p_sales_package=p_sales_package,p_price=p_price,p_stock=p_stock,p_exp_days=p_exp_days,p_img=p_img)
                qry.save()
                msg="Fertilizer Added Succesfully"
                return render(request,'Admin/AddFertilizer.html',{'form':form,'msg':msg,'categories':categories})
            else:
                msg="Fertilizer Already Added"
                return render(request,'Admin/AddFertilizer.html',{'form':form,'msg':msg,'categories':categories})
        else:
            print(form.errors)
    return render(request,'Admin/AddFertilizer.html',{'form':form,'categories':categories})

def AddSeeds(request):
    form=SeedForm()
    categories=CategoryDetails.objects.filter(m_id=4)
    
    if request.method=='POST':
        form=SeedForm(request.POST,request.FILES)
        if form.is_valid():
            cat_id=CategoryDetails.objects.get(c_id=request.POST['cat'])
            m_id=MainCategory.objects.get(m_id=4)
            p_name=form.cleaned_data['p_name']
            p_desc=form.cleaned_data['p_desc']
            
            p_sales_package=form.cleaned_data['p_sales_package']
            p_price=form.cleaned_data['p_price']
            p_stock=form.cleaned_data['p_stock']
            p_exp_days=form.cleaned_data['p_exp_days']
            p_img=form.cleaned_data['p_img']
            
            product_exist=NurseryProduct.objects.filter(cat_id=cat_id,p_name=p_name).exists()
            if not product_exist:
                qry=NurseryProduct(cat_id=cat_id,m_id=m_id,p_name=p_name,p_desc=p_desc,p_sales_package=p_sales_package,p_price=p_price,p_stock=p_stock,p_exp_days=p_exp_days,p_img=p_img)
                qry.save()
                msg="Seeds Added Succesfully"
                return render(request,'Admin/AddSeeds.html',{'form':form,'msg':msg,'categories':categories})
            else:
                msg="Seeds Already Added"
                return render(request,'Admin/AddSeeds.html',{'form':form,'msg':msg,'categories':categories})
        else:
            print(form.errors)
    return render(request,'Admin/AddSeeds.html',{'form':form,'categories':categories})

def AddTools(request):
    categories=CategoryDetails.objects.filter(m_id=6)
    form=OtherProducts()
    
    if request.method=='POST':
        form=OtherProducts(request.POST,request.FILES)
        if form.is_valid():
            cat_id=CategoryDetails.objects.get(c_id=request.POST['cat'])
            m_id=MainCategory.objects.get(m_id=6)
            p_name=form.cleaned_data['p_name']
            p_desc=form.cleaned_data['p_desc']
            p_sales_package=form.cleaned_data['p_sales_package']
            p_price=form.cleaned_data['p_price']
            p_stock=form.cleaned_data['p_stock']
            p_features=form.cleaned_data['p_features']
            p_exp_days=form.cleaned_data['p_exp_days']
            p_img=form.cleaned_data['p_img']
            product_exist=NurseryProduct.objects.filter(cat_id=cat_id,p_name=p_name).exists()
            if not product_exist:
                qry=NurseryProduct(cat_id=cat_id,m_id=m_id,p_name=p_name,p_desc=p_desc,p_features=p_features,p_sales_package=p_sales_package,p_price=p_price,p_stock=p_stock,p_exp_days=p_exp_days,p_img=p_img)
                qry.save()
                msg="Tool Added Succesfully"
                return render(request,'Admin/AddTools.html',{'form':form,'categories':categories,'msg':msg})
            else:
                msg="Seeds Already Added"
                return render(request,'Admin/AddTools.html',{'form':form,'categories':categories,'msg':msg})
        else:
            print(form.errors)
    return render(request,'Admin/AddTools.html',{'form':form,'categories':categories})
