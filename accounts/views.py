from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from accounts.form import RegisterForm, AccountsForm


from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .form import RegisterForm, AccountsForm

def User_register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        acc_form = AccountsForm(request.POST, request.FILES)

        if form.is_valid() and acc_form.is_valid():
            email = form.cleaned_data['email'].lower()
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            
            if password != repeat_password:
                messages.error(request, "Passwords do not match!")
                return redirect('register')

            if User.objects.filter(email=email).exists():
                messages.error(request, "Email already exists!")
                return redirect('register')

            if User.objects.filter(username=email).exists():
                messages.error(request, "Username already exists!")
                return redirect('register')
            
            phone = acc_form.cleaned_data['phone_number']
            if Account.objects.filter(phone_number=phone).exists():
                messages.error(request, "Phone number already exists!")
                return redirect('register')
            
            # User үүсгэх
            user = User.objects.create_user(
                username=email,
                email=email,
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                password=password
            )

            # Account үүсгэх
            account = acc_form.save(commit=False)
            account.user = user
            account.save()

            messages.success(request, "Your account has been created successfully!")
            return redirect('signin')

        else:
            messages.error(request, "Form validation failed!")

    else:
        form = RegisterForm()
        acc_form = AccountsForm()

    return render(request, 'register.html', {
        'form': form,
        'acc_form': acc_form,
    })


from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from accounts.models import Account

def User_login(request):
    if request.method == 'POST':
        identifier = request.POST.get('email').lower()  # email эсвэл phone input
        password = request.POST.get('password')

        user = None

        if User.objects.filter(email=identifier).exists():
            user_obj = User.objects.get(email=identifier)
            user = authenticate(request, username=user_obj.username, password=password)

        elif Account.objects.filter(phone_number=identifier).exists():
            account_obj = Account.objects.get(phone_number=identifier)
            user = authenticate(request, username=account_obj.user.username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, f"Welcome, {user.first_name}!")
            return redirect('/')
        else:
            messages.error(request, "Email/Phone or password is incorrect!")

    return render(request, 'signin.html')


def User_logout(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('signin')
