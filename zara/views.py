from django.shortcuts import render
from .models import Parent,Admin,Staff,Attendance,PhotoGallery
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')


def preg(request):
    if request.method == "POST":
        kname = request.POST["username"]
        password = request.POST["password"]
        email = request.POST['email']
        register1 = Parent(KidName=kname, Password=password, Email=email)
        register1.save()

        return HttpResponse("SUCCESSFUL")
    return render(request, 'register.html')


def login(request):
    try:
        if not (request.session['member_id'] is None):
            # m = Parent.objects.get(id=request.session['member_id'])
            # return render(request, 'profile.html', {'user': m})
            parent = Parent.objects.all()
            for i in parent:
                if request.session['name'] == i.KidName:
                    return render(request,'parent/index.html',{'user':i})
            staff = Staff.objects.all()
            for i in staff:
                if(request.session['name'] == i.StaffName):
                    return render(request,'staff/index.html',{'user':i})
                
            admin = Admin.objects.all()
            for i in admin:
                if request.session['name'] in i.Username:
                    return render(request,'dashboard/dashboard.html',{'user':1})
    except:
        pass
    try:
        if request.method == "POST":
            if request.POST['login'] == 'p':
                name = request.POST['username']
                m = Parent.objects.get(KidName=name)
                if m.Password == request.POST['password']:
                    request.session['member_id'] = m.id
                    request.session['name'] = m.KidName
                    return render(request, 'parent/index.html', {'user': m})
            elif request.POST['login'] =='s':
                name = request.POST['username']
                m = Staff.objects.get(StaffName=name)
                if m.Password == request.POST['password']:
                    request.session['member_id'] = m.id
                    request.session['name'] = m.StaffName
                    return render(request, 'staff/index.html', {'user': m})
            elif request.POST['login'] =='a':
                name = request.POST['username']
                m = Admin.objects.get(Username=name)
                print (m)
                if m.Password == request.POST['password']:
                    request.session['member_id'] = m.id
                    request.session['name'] = m.Username
                    return render(request, 'dashboard/dashboard.html', {'user': m})
            else:
                return HttpResponse("Your username and password didn't match.")
    except:
        return HttpResponse('Enter All the Fields')
    return render(request, "login.html")


def logout(request):
    try:
        request.session.flush()
    except KeyError:
        pass
    return render(request, 'index.html')


def edit(request):
    try:
        print (request.session['member_id'])
        if not (request.session['member_id'] is None):
            if request.method == "POST":
                m = Parent.objects.get(id=request.session['member_id'])
                print(m)
                m.ProfileImage = request.FILES["profilepic"]
                fathername = request.POST["fathername"]
                m.FatherName = fathername
                print(m.FatherName)
                m.MotherName = request.POST['mothername']
                m.Age = request.POST['age']
                m.Address = request.POST['address']
                m.Phone = request.POST['phone']
                m.save()
                return render(request, 'profile.html', {'user': m})
            m = Parent.objects.get(id=request.session['member_id'])
            return render(request, 'profileedit1.html', {'user': m})
    except:
        pass
    # if request.method =="POST":
    #      FatherName = request.POST["fathername"]
    #      print(FatherName)
    return render(request,'login.html')


def dashboard(request):
    return render(request,'dashboard/dashboard.html')

def contact(request):
    return render(request,'contact.html')

def adminregister(request):
    if request.method == "POST":
        adname = request.POST['name']
        adpassword = request.POST["password"]
        adimage = request.FILES["images"]
        email = request.POST['email']
        register3 = Admin(Username=adname,  Password=adpassword, profileimage=adimage, Email=email)
        register3.save()
        a = Admin.objects.get(Username=adname, Email=email)
        # register1 = Login(Username=adname, Password=adpassword, Userid=a.id, Type=2)
        # register1.save()
        return render(request, 'dashboard.html',{''})
    return render(request, 'dashboard/register.html')

def staffregister(request):
    try:
        if request.method == "POST":
            name = request.POST['name']
            image = request.FILES["images"]
            email = request.POST['email']
            address = request.POST['address']
            age = request.POST['age']
            phone = request.POST['phone']
            salary = request.POST['salary']
            register3 = Staff(StaffName=name,  Age=age, profileimage=image, Email=email,Salary=salary,Phoneno=phone,Address=address)
            register3.save()
            # a = Staff.objects.get(Username=adname, Email=email)
            # register1 = Login(Username=adname, Password=adpassword, Userid=a.id, Type=2)
            # register1.save()
            return HttpResponse('Successful')
    except:
        pass
    
    return render(request, 'dashboard/dashboard.html')


def adminlogin(request):
    # try:
    #     if not (request.session['member_id'] is None):
    #         m = Parent.objects.get(id=request.session['member_id'])
    #         return render(request, 'profile.html', {'user': m})
    # except:
    #     pass
    if request.method == "POST":

        name = request.POST['name']
        m = Admin.objects.get(Username=name)
        if m.Password == request.POST['password']:
            request.session['member_id'] = m.id
            request.session['adminname'] = m.Username
            return render(request, 'dashboard/dashboard.html', {'user': m})
        else:
            return HttpResponse("Your username and password didn't match.")

    return render(request, "dashboard/login.html")
def pprofile(request):
    try:
        if not (request.session['member_id'] is None):
                m = Parent.objects.get(id=request.session['member_id'])
                return render(request, 'parent/index.html', {'user': m})
    except:
        pass            
    return render(request,'login.html')

def pedit(request):
    try:
        if not (request.session['name'] is None):
            if request.method == "POST":
                m = Parent.objects.get(id=request.session['member_id'])
                m.FatherName = request.POST['fathername']
                m.MotherName = request.POST['mothername']
                m.Age = request.POST['age']
                m.Address = request.POST['address']
                m.Phone = request.POST['phone']
                m.ProfileImage = request.FILES["image"]
                m.save()
                return render(request,'parent/index.html',{'user':m})
            m = Parent.objects.get(id=request.session['member_id'])
            return render(request, 'parent/edit.html', {'user': m})
    except:
        pass
            
    return render(request,'login.html')
def sprofile(request):
    try:
        if not (request.session['member_id'] is None):
                m = Staff.objects.get(id=request.session['member_id'])
                return render(request, 'staff/index.html', {'user': m})
    except:
        pass            
    return render(request,'login.html')
def sedit(request):

    if not (request.session['name'] is None):
        if request.method == "POST":
            m = Staff.objects.get(id=request.session['member_id'])
            m.Age = request.POST['age']
            m.Address = request.POST['address']
            m.Password = request.POST['password']
            m.Phoneno = request.POST['phone']
            m.profileimage = request.FILES["image"]
            m.save()
            return render(request,'staff/index.html',{'user':m})
        m = Staff.objects.get(id=request.session['member_id'])
        return render(request, 'staff/edit.html', {'user': m})

        
    return render(request,'login.html')
def Attend(request):
    if request.method == "POST":
        ids= request.POST['ids']
        Attendance = request.POST['attendance']
        m= Parent.objects.get(id=ids)
        m.attendance = Attendance
        m.save()
        return HttpResponse("successful")
    m = Parent.objects.all()
    return render(request,'staff/attendance.html',{'users':m})
def payfee(request):
    if request.method == "POST":
        print(request.session['member_id'])
        m = Parent.objects.get(id=request.session['member_id'])
        print(m.KidName)
        m.status = 1
        m.save()
        print(m.status)
        status = m.status
        return render(request, 'parent/payfee.html', {'user': m, 'status': status})
    m = Parent.objects.get(id=request.session['member_id'])
    status = m.status
    return render(request, 'parent/payfee.html', {'user': m,'status':status})
def payment(request):
    if request.method == "POST":
        print(request.session['member_id'])
        m = Staff.objects.get(id=request.session['member_id'])
        m.Status = 1
        m.save()
    m = Staff.objects.get(id=request.session['member_id'])
    return render(request, 'staff/paymet.html', {'user': m})
def payfeeadmin(request):
    if request.method == "POST":
        z = request.POST['received']
        m = Parent.objects.get(id=z)
        m.status = "2"
        m.save()
        return HttpResponse('sucessful')
    m = Parent.objects.all()
    return render(request,'dashboard/payfee.html',{'user':m})
def paymentadmin(request):
    if request.method == "POST":
        z = request.POST['pay']
        m = Staff.objects.get(id=z)
        print(m.StaffName)
        m.Status = "1"
        m.save()
        return HttpResponse('Succesful')
    m = Staff.objects.all()
    return render(request,'dashboard/salary.html',{'user':m})
    
def photogallery(request):
    m = PhotoGallery.objects.all()
    return render(request,'photogallery.html',{'user':m})

def photoupload(request):
    if request.method == "POST":
        image = request.FILES['photos']
        images = PhotoGallery(Image = image)
        images.save()
        return render(request,'index.html')
    return render(request,'dashboard/photoupload.html')