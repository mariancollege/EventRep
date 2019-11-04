

from django.shortcuts import render, render_to_response
from EventApp.models import *
from django.http import HttpResponse
# Create your views here.

def testttable(request):
    return render(request,'enduser/testttable.html', context={'data': User.objects.all()})
def log(request):
    if request.method == "POST":
        u = request.POST['txtemail']
        p = request.POST['txtpassword']
        if User.objects.all().filter(username=u).filter(password=p).exists():

            return render_to_response('enduser/event.html', {'loginmessage': ' '})
        else:
            return render(request, 'enduser/log.html', context={'loginmessage': 'Incorrect Email or Password!'})
    if request.method == "GET":
        return render_to_response('enduser/log.html', {'loginmessage': ' '})
    return render_to_response('enduser/log.html', {'loginmessage': ' '})



def index(request):
    return render(request, 'enduser/index.html')


def forget(request):
    return render(request, 'enduser/forget-pass.html')


def event(request):
    return render(request, 'enduser/event.html')

# gender= models.CharField(widget=models.RadioSelect(name))


def regis(request):
    if request.method == "POST":
        email = request.POST['txtemail']
        password1 = request.POST['password']
        password2 = request.POST['txtpassword']
        uregno = request.POST['registerno']
        uname= request.POST['uname']
        collegee=request.POST['college']
        department=request.POST['department']
        coursee=request.POST['course']
        genderr=request.POST['option1']
        # photoo=request.POST['photo']
        contacto=request.POST['contactno']
        yop=request.POST['yop']
        if password1 == password2:
            User.objects.get_or_create(username=email,password=password2,regno=uregno,gender=genderr,name=uname,collegeid=collegee,departmentid=department,courseid=coursee,contactno=int(contacto),yop=int(yop))
            return render_to_response('enduser/event.html',{'message':'Registration Successfull'})
        else:
            return render_to_response(request, 'enduser/registration.html',{'message':'Incorrect username or password'})
    return render(request, 'enduser/registration.html')


def addevent(request):
    if request.method == "POST":
        eename=request.POST.get("eeventname",default='hh')
        eevenue=request.POST.get('evenue')
        eedate=request.POST.get('edate')
        eeregfee=request.POST.get('eregfee')
        eetpm=request.POST.get('etpm')
        eedepartment=request.POST.get('edepartment')
        eedescreption=request.POST.get('edescreption')
        eebrochure=request.POST.get('ebrochure')
        Admin.objects.get_or_create(eventname=eename,venue=eevenue,ddate=eedate,regfee=eeregfee,tpm=eetpm,department=eedepartment,descreption=eedescreption,brochure=eebrochure)
        return render(request,'admin/viewevent.html')
    # else:
    #     return render_to_response(request, 'admin/addevent',{'messge':'Some fields are missing'})
    return render(request, 'admin/addevent.html')

def editevent(request):
    return render(request, 'admin/editevent.html')


def viewevent(request):
    return render(request, 'admin/viewevent.html')