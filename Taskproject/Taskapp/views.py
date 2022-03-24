from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def demo(request):
    #name="Page"
    return render(request,"index.html")
#def calc(request):
    #x=int(request.GET['num1'])
    #y=int(request.GET['num2'])
    #c=x+y
    #d=x-y
    #e=x*y
    #f=x/y
    #return render(request,'result.html', {'result1':c, 'result2':d, 'result3':e, 'result4':f})
