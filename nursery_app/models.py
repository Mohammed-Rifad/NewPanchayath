from nursery_app.views.CustomerViews import ProductDetails
from django import db
from django.db import models
from django.db.models.base import Model
from passlib.hash import pbkdf2_sha256
# Create your models here.



class AdminDetails(models.Model):
    login_id=models.CharField(max_length=20,db_column="log_id")
    login_passwd=models.CharField(max_length=120,db_column='passwd')

    class Meta:
        db_table="tb_super"

    def verifyPasswd(self,raw_passwd):
        return pbkdf2_sha256.verify(raw_passwd,self.login_passwd)

class MainCategory(models.Model):
    m_id=models.AutoField(primary_key=True,db_column="m_id")
    m_name=models.CharField(max_length=20,db_column="m_name")
  
    class Meta:
        db_table="tb_main"

class CategoryDetails(models.Model):
    
    c_id=models.AutoField(primary_key=True,db_column="c_id")
    m_id=models.ForeignKey(MainCategory,on_delete=models.CASCADE,db_column="m_id")
    c_name=models.CharField(max_length=30,db_column="c_name")
    c_desc=models.CharField(max_length=200,db_column="c_desc")
    c_img=models.ImageField(upload_to="Category/",db_column="c_img")

    class Meta:
        db_table="tb_category"


class NurseryProduct(models.Model):
    p_id=models.AutoField(primary_key=True,db_column="p_id")
    cat_id=models.ForeignKey(CategoryDetails,on_delete=models.CASCADE,db_column="cat_id",null=True)
    m_id=models.ForeignKey(MainCategory,on_delete=models.CASCADE,db_column="m_id")
    p_name=models.CharField(max_length=20,db_column="p_name")
    p_desc=models.CharField(max_length=200,db_column="p_desc")
    p_dimension=models.CharField(max_length=30,db_column="p_dimension")
    p_location=models.CharField(max_length=20,db_column="p_location")
    p_color=models.CharField(max_length=10,db_column="p_color")
    p_sales_package=models.CharField(max_length=20,db_column="p_package")
    p_material=models.CharField(max_length=20,db_column="p_material",default="")
    p_shape=models.CharField(max_length=20,db_column="p_shape",default="")
    p_qty=models.IntegerField(db_column="p_qty",null=True)
    p_type=models.CharField(max_length=20,db_column="p_type",default="")
    p_suitable_for=models.CharField(max_length=20,db_column="p_suitable")
    p_seed=models.CharField(max_length=20,db_column="p_seed")
    p_container=models.CharField(max_length=20,db_column="p_container",null=True)
    p_caring_tips=models.CharField(max_length=200,db_column="p_tips",null=True)
    p_features=models.CharField(max_length=100,db_column="p_features")
    p_price=models.FloatField(db_column="p_price")
    p_offer=models.FloatField(db_column="p_offer",default=0)
    p_rating=models.FloatField(db_column="p_rating",default=0)
    p_exp_days=models.IntegerField(db_column="p_expected_days")
    p_img=models.ImageField(upload_to="Products/",db_column="p_img")
    p_stock=models.IntegerField(db_column="p_stock",default=0)
    p_status=models.CharField(max_length=20,default="available")
    
    class Meta:
        db_table="tb_nursery_product"

class CustomerDetails(models.Model):
    cust_id=models.AutoField(primary_key=True)
    cust_name=models.CharField(max_length=30,db_column="c_name")
    cust_address=models.CharField(max_length=255,db_column="c_address")
    cust_phno=models.CharField(max_length=10,db_column="c_phno")
    cust_email=models.CharField(max_length=40,db_column="c_email")
    cust_passwd=models.CharField(max_length=40,db_column="c_passwd")
    cust_img=models.ImageField(upload_to="Customer/",db_column="c_img")
    class Meta:
        db_table="tb_customer"

    def verifyPasswd(self,raw_passwd):
        return pbkdf2_sha256.verify(raw_passwd,self.cust_passwd)


class CartDetails(models.Model):
    cart_id=models.AutoField(primary_key=True,db_column="c_id")
    cust_id=models.ForeignKey(CustomerDetails,on_delete=models.CASCADE,db_column="cust_id")
    nursery_product=models.ForeignKey(NurseryProduct,on_delete=models.CASCADE,null=True,blank=True,db_column="n_id")
    qty=models.IntegerField(db_column="qty")
    total=models.FloatField(db_column="total")
   
    class Meta:
        db_table="tb_cart"


# class OrderDetails(models.Model):
#     order_no=models.CharField(max_length=20,primary_key=True,db_column='ord_no')
#     prod_id=models.ForeignKey(ProductDetails,on_delete=models.CASCADE,db_column='pr_id')
#     cust_id=models.ForeignKey(CustomerDetails,on_delete=models.CASCADE,db_column='cust_id')
#     order_date=models.CharField(max_length=10,db_column='ord_date')
#     exp_delivery=models.CharField(max_length=10,db_column='exp_date')
#     qty=models.IntegerField(db_column='qty')
#     total=models.FloatField(db_column='total')
#     order_status=models.CharField(max_length=10,db_column='ord_status')

#     class Meta:
#         db_table="tb_order"




