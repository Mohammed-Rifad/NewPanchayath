from django.urls import path
from .views import CommonViews,AdminViews,CustomerViews

app_name="e_nursery"

urlpatterns = [
   path('',CommonViews.ProjectHome),
   path('AdminData',CommonViews.AdminData),
   path('Register',CommonViews.CustomerReg,name="cust_reg"),
   path('CustomerHome',CustomerViews.CustomerHome,name="cust_home"),
   path('CustomerHome/ViewProducts',CustomerViews.ViewProducts,name="cust_view_products"),
   path('CustomerHome/ProductDetails/<int:pid>',CustomerViews.ProductDetails,name="cust_product_details"),

   path('login',CommonViews.Login,name="login"),
   path('ViewProducts',CommonViews.ViewProducts,name="view_products"),
   path('CustomerHome/Cart',CustomerViews.Cart,name="cart"),
   path('ProductDetails/<int:pid>',CommonViews.ProductDetails,name="product_details"),
   path('AdminHome',AdminViews.AdminHome,name="admin_home"),
   path('Admin/AddCat',AdminViews.AddCategory,name="add_cat"),
   path('Admin/AddPlants',AdminViews.AddNurseryPlants,name="add_plants"),
   path('Admin/AddPots',AdminViews.AddPots,name="add_pots"),
   path('Admin/AddStands',AdminViews.AddStands,name="add_stands"),
   path('Admin/Fertilizer',AdminViews.AddFertilizers,name="add_fertilizer"),
   path('Admin/Seeds',AdminViews.AddSeeds,name="add_seeds"),
   path('Admin/Tools',AdminViews.AddTools,name="add_tools")
]