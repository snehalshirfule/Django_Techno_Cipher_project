from tkinter import Image
from django.shortcuts import redirect, render
from vendor.forms import AuthForm, DashForm, Registration_Form,ImageForm
from vendor.models import VendorModel
# Create your views here.


def signin(request):

    if request.method == "POST":
        print("form submit-------------------------")
        form = AuthForm(request.POST)
        if form.is_valid():
            print("form valid-------------------------")
            email = request.POST["email_ID"]
            password = request.POST["password"]
            try:
                result = VendorModel.objects.get(
                    email_ID=email, password=password)
                if result:
                    print(result.id)
                    request.session['user_id']=result.id
                    request.session['user_name']=result.username
                    return redirect("/vr/vdashboard")
            except VendorModel.DoesNotExist:
                message = "Invalid email or password"
                return render(request, "vendor/sign-in.html", {'message': message})
    else:
        return render(request, 'vendor/sign-in.html')
    
    

def signup(request):
    if request.method == "POST":
        print("form signup--------------------------")
        form = Registration_Form(request.POST)
        email=request.POST["email_ID"]
        if form.is_valid():
            print("form is valid--------------------------")
            try:
               if VendorModel.objects.get(email_ID=email):
                    message="User already Exists"
                    return render(request,'sign-up.html',{'message':message})
            except VendorModel.DoesNotExist:
                form.save()
                return redirect("/vr/signin")
    else:
        return render(request, 'vendor/sign-up.html')


def vdashboard(request):
    if 'user_id' in request.session:
        id__=request.session['user_id']
        vendor = VendorModel.objects.get(id=id__)
        return render(request,'vendor/vdashboard.html',{'vendor':vendor,'user_name':request.session['user_name'].title()})
    else:
        return redirect("/vr/signin")


def saveprofile(request):
    if 'user_id' in request.session:
        id=request.session['user_id']
        vendor = VendorModel.objects.get(id=id)  
        form = DashForm(request.POST, instance = vendor)
        if form.is_valid():  
            form.save()  
            return redirect("/vr/vdashboard")  
        return render(request, 'vendor/profile.html', {'vendor': vendor, 'user_name':request.session['user_name'].title()})
    else:
        return redirect("/vr/signin")
    

def signout(request):
    print("signout---------------------------------")

    if 'user_id' in request.session :
        print("signout---------------------------------")

        try:
            print("signout---------------------------------")

            del request.session['user_id']
            return redirect('/vr/signin')
        except:
            pass


def mypackage(request):
    if 'user_id' in request.session:
        return render(request,'vendor/package.html')
    else:
        return redirect("/vr/signin")


def addpost(request):
   if request.method == "POST":
       form = ImageForm(request.POST, request.FILES)
       if form.is_valid():
        form.save()
   form = ImageForm()
   return render(request,'vendor/addpost.html',{'form':form})



def allpost(request):
    if request.method == "POST":
       form = ImageForm(request.POST, request.FILES)
       if form.is_valid():
        form.save()
    img = Image.objects.all()
    return render(request,'vendor/allpost.html',{'img':img}) 