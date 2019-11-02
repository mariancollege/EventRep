

from django.shortcuts import render, render_to_response
from EventApp.models import User
# Create your views here.


def log(request):
    if request.method == "POST":
        u = request.POST['txtemail']
        p = request.POST['txtpassword']
        if User.objects.all().filter(username=u).filter(password=p).exists():
            return render_to_response('enduser/event.html', {'message': 'Login Successfull'})
        else:
            return render_to_response('enduser/log.html', {'message': 'Incorrect Email or Password!'})
    return render(request, 'enduser/log.html')




def index(request):
    return render(request, 'enduser/index.html')


def forget(request):
    return render(request, 'enduser/forget-pass.html')


def event(request):
    return render(request, 'enduser/event.html')


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
        # genderr=request.POST['gender']
        # photoo=request.POST['photo']
        contacto=request.POST['contactno']
        yop=request.POST['yop']
        if password1 == password2:
            User.objects.get_or_create(username=email,password=password2,regno=uregno,name=uname,collegeid=collegee,departmentid=department,courseid=coursee,contactno=int(contacto),yop=int(yop))
            return render_to_response('enduser/event.html',{'message':'Registration Successfull'})
        else:
            return render_to_response(request, 'enduser/registration.html',{'message':'Incorrect username or password'})
    return render(request, 'enduser/registration.html')


def addevent(request):
    if request.method == "POST":
        ename=request.POST['en']
        evenue=request.POST['venue']
        edate=request.POST['venue']
        eregfee=request.POST['regfee']
        etpm=request.POST['tpm']
        # edepartment=request.POST['department']
        edescreption=request.POST['descreption']
        # ebrochure=request.POST['brochure']
        if User.objects.all().exists():
            User.objects.get_or_create(venue=evenue,date=edate,regfee=eregfee,tpm=etpm,descreption=edescreption,eventname=ename)
            return render_to_response(request, 'admin/viewevent.html',{'message':'Event uploaded sucessfully'})
        else:
            return render_to_response(request, 'admin/addevent',{'messge':'Some fields are missing'})
    return render(request, 'admin/addevent.html')


def editevent(request):
    return render(request, 'admin/editevent.html')


def viewevent(request):
    return render(request, 'admin/viewevent.html')