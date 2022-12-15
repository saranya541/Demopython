from django.urls import path
from .import views
app_name='shop'
urlpatterns = [

    path('',views.allpdtcat,name='allpdtcat'),
    path('<slug:c_slug>/',views.allpdtcat,name='products_by_category'),
    path('<slug:c_slug>/<slug:product_slug>/',views.pdtDetail,name='pdtCatDetail')
    ]