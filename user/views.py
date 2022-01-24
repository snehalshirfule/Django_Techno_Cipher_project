from django.shortcuts import render,redirect
from django.http import HttpResponse
from user.forms import SignupForm, SigninForm
from user.models import UserModel

# Create your views here.


def signup(request):
    if request.method == "POST":
        print("signup form-------------------")
        form = SignupForm(request.POST)
        email=request.POST["email"]
        if form.is_valid():
            print("form is valid-------------------")
            try:
               if UserModel.objects.get(email=email):
                    message="User already Exists"
                    return render(request,'user/signup.html',{'message':message})
            except UserModel.DoesNotExist:
                form.save()
                return redirect('/us/signin')
    else:
        return render(request, 'user/signup.html')



def signin(request):
    if request.method == "POST":
        print("form submit--------------------------")
        form = SigninForm(request.POST)
        if form.is_valid():
            print("form is valid--------------------")
            email = request.POST["email"]
            password = request.POST["password"]
            try:
                result = UserModel.objects.get(
                    email=email, password=password)
                if result:
                    print(result.id)
                    request.session['email']=result.id
                    request.session['username']=result.username                    
                    return redirect('/us/home')
            except UserModel.DoesNotExist:
                message = "Invalid email or password"
                return render(request, "user/signin.html", {'message': message})
    else:
        return render(request, 'user/signin.html')


def home(request):
    id = request.session['email']
    user = UserModel.objects.get(id=id)
    return render(request,'user/home.html',{'user':user,'username':request.session['username'].title()})