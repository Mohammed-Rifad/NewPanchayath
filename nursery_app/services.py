from random import randint

from nursery_app.models import CartDetails, NurseryProduct



def getProductFeatures(product_data):
    FeaturesKey={}
    FeaturesValue={}
    if product_data.m_id.m_id==1:
        feat1="Type"
        feat1Val=product_data.cat_id.c_name.title()
        feat2="Sales package"
        feat2Val=product_data.p_sales_package
        feat3="Conatiner Type"
        feat3Val=product_data.p_container
        feat4="Caring Tips"
        feat4Val=product_data.p_carin_tips

        FeaturesKey['feat1']=feat1
        FeaturesKey['feat2']=feat2
        FeaturesKey['feat3']=feat3
        FeaturesKey['feat4']=feat4

        FeaturesValue['value1']=feat1Val.title()
        FeaturesValue['value2']=feat2Val.title()
        FeaturesValue['value3']=feat3Val.title()
        FeaturesValue['value4']=feat4Val
    if product_data.m_id.m_id==2:
        feat1="Location Suitable"
        feat1Val=product_data.p_location.title()
        feat2="Sales package"
        feat2Val=product_data.p_sales_package
        feat3="Material"
        feat3Val=product_data.p_material
        feat4="Color"
        feat4Val=product_data.p_color.title()

        FeaturesKey['feat1']=feat1
        FeaturesKey['feat2']=feat2
        FeaturesKey['feat3']=feat3
        FeaturesKey['feat4']=feat4

        FeaturesValue['value1']=feat1Val.title()
        FeaturesValue['value2']=feat2Val.title()
        FeaturesValue['value3']=feat3Val.title()
        FeaturesValue['value4']=feat4Val
       
    return FeaturesKey,FeaturesValue


def AddToCart(p_id,u_id,qty):
    product_data=NurseryProduct.objects.get(p_id=p_id)
    # cust_id=CustomerDetails.objects.get(cust_id=u_id)
    # qty=request.POST['txtQty']
    price=product_data.p_price * int(qty)
    product_exist=CartDetails.objects.filter(nursery_product=p_id,cust_id=u_id).exists()
    if not product_exist:  
        cart=CartDetails(nursery_product=product_data,cust_id=u_id,qty=qty,total=price)
        cart.save()

# def getOrderID():
#       order_id=randint(1000000000,9999999999)
#       exist=OrderDetails.objects.get()