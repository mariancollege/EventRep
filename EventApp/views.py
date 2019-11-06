

from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.contrib.auth import logout as auth_logout
from EventApp.models import *
# from .forms import PostForm
from django.http import HttpResponse

def eevent(request):
    ob = Admin.objects.all()
    ob1 = departmentn.objects.all()
    ob2 = months.objects.all()
    ob3 = week.objects.all()
    usersession=User.objects.get(username=(request.session['email']))
    return render(request, 'admin/eevent.html', context={'data': ob,'data1':ob1,'data2':ob2,'data3':ob3,'usersession':usersession})

def testttable(request):
    context = {
        'posts': 'asdasdsa'
        if request.user.is_authenticated else []
    }
    #obj=User2.objects.raw("select * from EventApp_user inner join EventApp_user2 on EventApp_user.username=EventApp_user2.username2_id")
    return render(request, 'enduser/testttable.html', context={'msg':request.session['email']})


def logout_google(request):
    auth_logout(request)
    return render(request, 'enduser/index.html', {}, RequestContext(request))

def log(request):
    if request.method == "POST":
        u = request.POST['txtemail']
        p = request.POST['txtpassword']
        if User.objects.all().filter(username=u).filter(password=p).exists():
            obj=User.objects.get(username=u)
            request.session['email']=u
            if obj.usertype=='student':
                return render(request,'enduser/index.html')
            elif obj.usertype=='admin':
                return render(request,'admin/home.html')
            else:
                return render(request,'enduser/log.html')
        else:
            return render(request, 'enduser/log.html', context={'loginmessage': 'Incorrect Email or Password!'})
    # if request.method == "GET":
    #     return render_to_response('enduser/log.html', {'loginmessage': ' '})
    return render_to_response('enduser/log.html', {'loginmessage': ' '})



def index(request):
    usersession=User.objects.get(username=(request.session['email']))
    ob=Admin.objects.all()
    return render(request, 'enduser/index.html',context={'data':ob,'usersession':usersession})


def forget(request):
    return render(request, 'enduser/forget-pass.html')

def home(request):
    usersession = User.objects.get(username=(request.session['email']))
    ob=Admin.objects.all()
    ob1=User.objects.all()
    return render(request, 'admin/home.html', context={'data':ob,'data1':ob1,'usersession':usersession})

def event(request):
    usersession = User.objects.get(username=(request.session['email']))
    ob=Admin.objects.all()
    ob1=departmentn.objects.all()
    ob2=months.objects.all()
    ob3=week.objects.all()
    return render(request, 'enduser/event.html', context={'data': ob,'data1':ob1,'data2':ob2,'data3':ob3,'usersession':usersession})

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
    usersession = User.objects.get(username=(request.session['email']))
    if request.method == "POST":

        eename=request.POST.get("eeventname")
        eevenue=request.POST.get('evenue')
        eedate=request.POST.get('datetext')
        eeregfee=request.POST.get('eregfee')
        eetpm=request.POST.get('etpm')
        eedepartment=request.POST.get('edepartment')
        eedescreption=request.POST.get('edescreption')
        ecat=request.POST.get('ecategory')
        nop=request.POST.get('eparti')
        # Admin.objects.get_or_create(eventname=eename, venue=eevenue)
        eebrochure = request.FILES['ebrochure']
        Admin.objects.get_or_create(edate=eedate,eventname=eename,venue=eevenue,regfee=eeregfee,tpm=eetpm,ddepartment=eedepartment,descreption=eedescreption,eventcategory=ecat ,parti=nop,brochure=eebrochure)
        return render(request, 'admin/home.html',context={'usersession':usersession})

    return render(request, 'admin/addevent.html',context={'usersession':usersession})

def editevent(request):
    usersession = User.objects.get(username=(request.session['email']))
    ob=Admin.objects.all()
    return render(request, 'admin/editevent.html',context={'data':ob,'usersession':usersession})


def about(request):
    usersession=User.objects.get(username=(request.session['email']))
    return render(request,'enduser/about.html',context={'usersession':usersession})

def contact(request):
    usersession=User.objects.get(username=(request.session['email']))
    return render(request,'enduser/contact.html',context={'usersession':usersession})


def candidate_view(request):
    usersession = User.objects.get(username=(request.session['email']))
    ob=User.objects.all()
    return render(request,'admin/candidate_view.html',context={'userdata':ob,'usersession':usersession})



def eventpub(request):
    usersession=User.objects.get(username=(request.session['email']))
    return render(request,'enduser/eventpub.html',context={'usersession':usersession})

