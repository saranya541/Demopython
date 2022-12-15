from . import views
from django.urls import path



urlpatterns = [


    path('',views.form,name='form'),
    # path('add/',views.cal,name='cal'),

    # path('contact/',views.contact,name="contact"),
    # path('detail/',views.detail,name="detail"),
    # path('thanks/',views.thanks,name='thanks')

]
