from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse

# Create your views here.
def student(request):
    ST=Student_Form()
    d={'fo':ST}
    if request.method=='POST':
        FD=Student_Form(request.POST)
        if FD.is_valid():
            return HttpResponse(str(FD.cleaned_data))
    return render(request,'student.html',d)
