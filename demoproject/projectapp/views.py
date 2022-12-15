from django.http import HttpResponse
from django.shortcuts import render
from . models import place,traveler


# Create your views here.

def form(request):
   obj=place.objects.all()
   dis=traveler.objects.all()
   return render(request,"index.html",{'result':obj,'result1':dis})
# def about(request):
#    return HttpResponse("about inmakes")
# def cal(request):
#    x=int(request.GET['num1'])
#    y=int(request.GET['num2'])
#    ans1=x+y
#    a = int(request.GET['num1'])
#    b = int(request.GET['num2'])
#    ans2=a*b
#    h = int(request.GET['num1'])
#    i= int(request.GET['num2'])
#    ans3=h/i
#    j= int(request.GET['num1'])
#    k= int(request.GET['num2'])
#    ans4=j-k

#    return render(request,"result.html",{'result':ans1,'result1':ans2,'result2':ans3,'result3':ans4})

# def detail(request):

#    return HttpResponse("details of django")
# def thanks(request):
#    return HttpResponse("thank you inmakes")