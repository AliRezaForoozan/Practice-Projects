from django.shortcuts import render
from . models import person

def home(request):

    allField = person.objects.all()
    frst = person.objects.first()
    dic_persons = {"First_Name":"AliReza","Last_Name":"Forouzan","allfield":allField,"first":frst}
    return render(request,'index.html',context=dic_persons)

# Create your views here.
