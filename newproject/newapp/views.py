from django.shortcuts import render,redirect
from newapp.models import RegisterModel
from newapp.models import hospital_details
from newapp.models import login


# Create your views here.

def viewdetails(request):
    obj = RegisterModel.objects.all()
    return render(request,'viewdetails.html',{'object':obj})
def index(request):
    if request.method=="POST":
        a=request.POST.get('fname')
        print(a)
        b=request.POST.get('lname')
        print(b)
        c=request.POST.get('uid')
        print(c)
        d=request.POST.get('pw')
        print(d)
        e=request.POST.get('number')
        print(e)
        f=request.POST.get('email')
        print(f)
        obj = RegisterModel.objects.create(firstname=a,lastname=b,userid=c,password=d,mobilenum=e,email=f)
        return redirect('login')
    return render(request,'index.html')
def hospital_details1(request):
    if request.method=="POST":
        a1=request.POST.get('ptname')
        print(a1)
        b1=request.POST.get('drname')
        print(b1)
        c1=request.POST.get('pid')
        print(c1)
        d1=request.FILES['ptdata']
        print(d1)
        e1=request.POST.get('admitdate')
        print(e1)
        f1=request.POST.get('disdate')
        print(f1)
        obj = hospital_details.objects.create(Patient_Name=a1,Doctor_Name=b1,Patient_id=c1,Patient_Data=d1,Admit_date=e1,Discharge_date=f1)
        return redirect('admin_hospitaldetails')
    return render(request, 'index1.html')

def login(request):
    if request.method=="POST":
        a2=request.POST.get('uname')
        print(a2)
        b2=request.POST.get('pwd')
        print(b2)
        try:
            obj = RegisterModel.objects.get(userid=a2, password=b2)
            request.session['user_pk']=obj.id
            if obj.userid == 'admin':
                return redirect('viewdetails')
            else:
                request.session['uname']=obj.firstname
                return redirect('hospital1')
        except:
            pass
    return render(request,'login.html')

def mydetails(request):
    uname=request.session['uname']
    user_data=request.session['user_pk']
    obj_details=RegisterModel.objects.get(id=user_data)
    return render(request,'mydetails.html',{'object':obj_details,'uname':uname})
def hospital1(request):
    uname=request.session['uname']
    obj = hospital_details.objects.all()
    return render(request,'viewdetails1.html',{'object':obj,'uname':uname})

def admin_hospitaldetails(request):
    obj = hospital_details.objects.all()
    return render(request,'admin_hospitaldetails.html',{'object': obj})
def delete_viewdetails1(request,pk):
    obj = hospital_details.objects.filter(id=pk).delete()
    return redirect('admin_hospitaldetails')
