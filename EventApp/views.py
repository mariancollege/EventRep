

from django.shortcuts import render, render_to_response
from EventApp.models import *
# from .forms import PostForm
from django.http import HttpResponse


def testttable(request):
    return render(request,'enduser/testttable.html', context={'data': User.objects.all()})


def eevent(request):
    ob = Admin.objects.all()
    ob1 = departmentn.objects.all()
    ob2 = months.objects.all()
    ob3 = week.objects.all()
    return render(request, 'admin/eevent.html', context={'data': ob,'data1':ob1,'data2':ob2,'data3':ob3})

def testttable(request):
    obj=User2.objects.raw("select * from EventApp_user inner join EventApp_user2 on EventApp_user.username=EventApp_user2.username2_id")
    return render(request, 'enduser/testttable.html', context={'data': obj})

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
    ob=Admin.objects.all()
    return render(request, 'enduser/index.html',context={'data':ob})


def forget(request):
    return render(request, 'enduser/forget-pass.html')

def home(request):
    ob=Admin.objects.all()
    return render(request, 'admin/home.html', context={'data':ob})

def event(request):
    ob=Admin.objects.all()
    ob1=departmentn.objects.all()
    ob2=months.objects.all()
    ob3=week.objects.all()
    return render(request, 'enduser/event.html', context={'data': ob,'data1':ob1,'data2':ob2,'data3':ob3})

# gender= models.CharField(widget=models.RadioSelect(name))
# def post_new(request):
#     form = PostForm()
#     return render(request, 'enduser/event.html', {'form': form})

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

        contacto=request.POST['contactno']
        yop=request.POST['yop']

        if password1 == password2:
            if User.objects.all().filter(username=email).exists():
                return render(request, 'enduser/registration.html', {'regmessage': 'Email already exist'})
            else:
                p = request.FILES['photo']
                User.objects.get_or_create(username=email,password=password2,regno=uregno,gender=genderr,name=uname,collegeid=collegee,departmentid=department,courseid=coursee,contactno=int(contacto),yop=int(yop),profilepic=p)
                return render_to_response('enduser/event.html',{'message':'Registration Successfull'})
        else:
            return render(request, 'enduser/registration.html',{'regmessage':'Password Doesnt Match'})
    return render(request, 'enduser/registration.html')


def addevent(request):

    if request.method == "POST":

        eename=request.POST.get("eeventname")
        eevenue=request.POST.get('evenue')
        eedate=request.POST.get('edate')
        eeregfee=request.POST.get('eregfee')
        eetpm=request.POST.get('etpm')
        eedepartment=request.POST.get('edepartment')
        eedescreption=request.POST.get('edescreption')
        # eebrochure=request.POST.get('ebrochure')
        ecat=request.POST.get('ecategory')
        nop=request.POST.get('eparti')
        # Admin.objects.get_or_create(eventname=eename, venue=eevenue)

        Admin.objects.get_or_create(eventname=eename,venue=eevenue,edate=date.today(),regfee=eeregfee,tpm=eetpm,ddepartment=eedepartment,descreption=eedescreption,eventcategory=ecat ,parti=nop)
        return render(request, 'admin/home.html')

    return render(request, 'admin/addevent.html')

def editevent(request):
    ob=Admin.objects.all()
    return render(request, 'admin/editevent.html',context={'data':ob})

