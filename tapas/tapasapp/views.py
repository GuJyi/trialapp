from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Dish, Account

# Create your views here.

useraccount = Account.objects.get(pk=1)

def login(request):
    if(request.method == "POST"):
        uname = request.POST.get('username')
        pword = request.POST.get('password')

        accountlist = Account.objects.filter(username = uname)

        if(len(accountlist) > 0):
            
            authenticateuser = Account.objects.get(username = uname)
            
            if(authenticateuser.getPassword() == pword):
                global useraccount
                useraccount = authenticateuser
                messages.info(request, 'Login Successful')
                return redirect('view_menu')

            else:
                messages.info(request, 'Invalid Login')
                return render(request, 'tapasapp/login.html')

        else:
            messages.info(request, 'Invalid Login')
            return render(request, 'tapasapp/login.html')

    else:
        return render(request, 'tapasapp/login.html')

def signup(request):
    if(request.method == "POST"):
        uname = request.POST.get('username')
        pword = request.POST.get('password')

        accountlist = Account.objects.filter(username = uname)
        
        if(len(accountlist) > 0):
            messages.info(request, 'Account already exists!')
            return render(request, 'tapasapp/signup.html')

        else:
            Account.objects.create(username = uname, password = pword)
            messages.info(request, 'Account created successfully!')
            return redirect('login')
    
    else:
        return render(request, 'tapasapp/signup.html')

def manage_account(request, pk):
    lia = get_object_or_404(Account, pk=pk)
    return render(request, 'tapasapp/manage_account.html', {'lia': lia})

def delete_account(request, pk):
    Account.objects.filter(pk=pk).delete()
    return redirect('login')

def change_password(request, pk):
    loggedin_user = Account.objects.get(pk=pk)
    lia = get_object_or_404(Account, pk=pk)
    
    if(request.method == "POST"):
        current = request.POST.get('currentpassword')
        new = request.POST.get('newpassword')
        newconfirm = request.POST.get('confirmnewpassword')

        if(loggedin_user.getPassword() == current):
            if(new == newconfirm):
                Account.objects.filter(pk=pk).update(password=newconfirm)
            
            else:
                messages.info(request, 'New Password does not match')
                return render(request, 'tapasapp/change_password.html', {'lia':lia})
        
        else:
            messages.info(request, 'Wrong Password')
            return render(request, 'tapasapp/change_password.html', {'lia':lia})

        return redirect('manage_account', pk=pk)

    else:
        return render(request, 'tapasapp/change_password.html', {'lia':lia})

def view_basic_list(request):
    dish_objects = Dish.objects.all()
    return render(request, 'tapasapp/basic_list.html', {'dishes':dish_objects})

def view_menu(request):
    dish_objects = Dish.objects.all()
    global useraccount
    return render(request, 'tapasapp/list.html', {'dishes':dish_objects, 'lia':useraccount})

def add_menu(request):
    if(request.method=="POST"):
        dishname = request.POST.get('dname')
        cooktime = request.POST.get('ctime')
        preptime = request.POST.get('ptime')
        Dish.objects.create(name=dishname, cook_time=cooktime, prep_time=preptime)
        return redirect('view_menu')
    else:
        return render(request, 'tapasapp/add_menu.html')

def view_detail(request, pk):
    d = get_object_or_404(Dish, pk=pk)
    return render(request, 'tapasapp/view_detail.html', {'d':d})

def update_dish(request, pk):
    if(request.method == "POST"):
        cooktime = request.POST.get('ctime')
        preptime = request.POST.get('ptime')

        Dish.objects.filter(pk=pk).update(cook_time=cooktime, prep_time=preptime)

        return redirect('view_detail', pk=pk)

    else:
        d = get_object_or_404(Dish, pk=pk)
        return render(request, 'tapasapp/update_dish.html', {'d':d})

def delete_dish(request, pk):
    Dish.objects.filter(pk=pk).delete()
    return redirect('view_menu')