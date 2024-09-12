from django.shortcuts import render,HttpResponse
from .models import Data

# Create your views here.

def data(request):
    if request.method=='GET':
      return render(request,'data.html')
    else:
       Data(
          Title=request.POST['title'],
          Description=request.POST['description'],
          Date=request.POST['date']
       ).save() 
    return render(request,'main.html')

def information(request,id):
   info=Data.objects.filter(id=id)
   return render(request,'information.html',{'info':info})

def delete(request,id):
     info1=Data.objects.get(id=id)
     info1.delete()
     return render(request,'main.html') 


def main(request):
    title=Data.objects.all()
    return render(request,'main.html',{"title":title})


def update(request,id):
   info2=Data.objects.get(id=id)
   return render(request,'update.html',{'info2':info2})

def updateinf(request,id):
   info3=Data.objects.get(id=id)
   info3.Title=request.POST['title']
   info3.Description=request.POST['description']
   info3.Date=request.POST['date']
   info3.save()
   return render(request,'main.html')

   
   


   
       

