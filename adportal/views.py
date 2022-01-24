from django.shortcuts import render, redirect
from adportal.forms import AdportalForm, SignupForm, SigninForm, AddCategoryForm,SubCategoryForm 
from adportal.models import AdportalModel, AddCategoryModel,SubCategoryModel
from django.core.exceptions import ObjectDoesNotExist
from vendor.models import VendorModel
from user.models import UserModel

# Create your views here.


# Admin Signin Code Start Here
def signin(request):
    if request.method == "POST":
        print("form post-----------------------------------")
        form = SigninForm(request.POST)
        if form.is_valid():
            print("form is valid---------------------")
            email = request.POST["email"]
            password = request.POST["password"]
            try:
                result = AdportalModel.objects.get(
                    email=email, password=password)
                if result:
                    print(result.id)
                    request.session['admin_id']=result.id
                    request.session['admin_name']=result.username
                    return render(request,"adminportal/profile1.html",{'message':'succesfully login!'})
            except AdportalModel.DoesNotExist:
                message = "Invalid email or password"
                return render(request, "adminportal/signin.html", {'message': message})
    else:
        return render(request, "adminportal/signin.html")
# ADMIN SIGNIN CODE END HERE


# Vendor Table Code Start Here 
def vendortable(request):
    if 'admin_id' in request.session:
        vendors = VendorModel.objects.all()
        return render(request,"adminportal/Vendor.html",{'vendors':vendors})
    else:
        return redirect("/ad/signin")
# VENDOR TABLE CODE END HERE


# User Table Code Start Here
def usertable(request):
    if 'admin_id' in request.session:
        users = UserModel.objects.all()      
        return render(request,"adminportal/user.html",{'users':users})
    else:
        return redirect("/ad/signin")

# USER TABLE CODE END HERE


# Admin Profile Page Code Start Here
def profile1(request):
    if 'admin_id' in request.session:
        print("profile1---------------------")    
        return render(request,"adminportal/profile1.html")
    else:
        return redirect("/ad/signin")
# ADMIN PROFILE PAGE CODE END HERE


# Admin Table Page Code Start Here
def table(request):
    if 'admin_id' in request.session:
        return render(request,"adminportal/table.html")
    else:
        return redirect("/ad/signin")
# ADMIN TABLE PAGE CODE END HERE


# Category Page Code Start Here
def category(request):
    if 'admin_id' in request.session:
        categorytb = AddCategoryModel.objects.all()
        return render(request, "adminportal/category.html", {'categorytb':categorytb})
    else:
        return redirect("/ad/signin")
# CATEGORY PAGE CODE END HERE
 

# AddCategory Page Code Start Here
def addcategory(request):
    if 'admin_id' in request.session:
        if request.method == 'POST':
            form = AddCategoryForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect("/ad/addcat")
            else:
                print("form error------------------")
        else:
            return render(request,"adminportal/addcat.html")
    else:
        return redirect("/ad/signin")

# ADDCATEGORY PAGE CODE END HERE


# Admin Signout Code Start Here
def signout(request):
    print("signout---------------------------------")
    if 'admin_id' in request.session :
        print("signout---------------------------------")
        try:
            print("signout---------------------------------")
            del request.session['admin_id']
            return redirect('/ad/signin')
        except:
            pass
    
# ADMIN SIGNOUT CODE END HERE


# Delete Category Code Here
def delete(request, id):  
    print("click on delete-----------")
    if 'admin_id' in request.session:
        category = AddCategoryModel.objects.get(id=id)
        print("get id------------")
        category.delete()
        return redirect("/ad/category")
    else:
        return redirect("/ad/signin")

# DELETE CATEGORY CODE END HERE


# Edit Category Code Start Here
def edit(request, id):
    if 'admin_id' in request.session:
        categorytb = AddCategoryModel.objects.get(id=id)
        return render(request, "adminportal/edit.html", {'categorytb':categorytb})  
    else:
        return redirect("/ad/signin")

# EDIT CATEGORY CODE END HERE


# Subcategory Page Code Start Here
def subcategory(request):
    if 'admin_id' in request.session:
        category =AddCategoryModel.objects.all()
        return render(request, "adminportal/subcategory.html",{'categories':category})
    else:
        return redirect("/ad/signin")

# SUBCATEGORY PAGE CODE END HERE


# AddSubcategory Page Code Start Here

def addsubcat(request):
    if 'admin_id' in request.session:
        return render(request, "adminportal/addsubcat.html")
    else:
        return redirect("/ad/signin")