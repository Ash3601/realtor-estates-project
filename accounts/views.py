from django.shortcuts import render, redirect
from django.contrib import messages, auth
from accounts.FormValidation import FormValidation
from django.contrib.auth.models import User
from contacts.models import Contact


def register(request):

    # ? Know if the request is for form submission then do ->
    if request.method == "POST":
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        password2 = request.POST["password2"]

        validation = FormValidation()
        print(
            validation.nameValidation(first_name)
            and validation.nameValidation(last_name)
        )
        #! Check if the Names are Valid
        if (
            validation.nameValidation(first_name)
            and validation.nameValidation(last_name)
        ) == False:
            messages.error(request, "Incorrect Name Fields!")
            return redirect("register")

        #! Check if the User already exists?
        if User.objects.filter(username=username).exists():
            messages.error(request, "That Username is taken.")
            return redirect("register")
        else:
            pass

        #! Check if the Email already exists?
        if User.objects.filter(email=email).exists():
            messages.error(request, "That Email is already used.")
            return redirect("register")
        else:
            pass

        #! Check if the Password is Strong
        if validation.checkPasswordStrength(password) == False:
            messages.error(request, "Password is Weak choose a strong password!")
            return redirect("register")

        #! Check if both the passwords are same
        if validation.checkPasswords(password, password2) == False:
            messages.error(request, "Passwords do not match!")
            return redirect("register")

        # ? Means all validations are passed
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
        )
        user.save()
        messages.success(request, "Account Created, Login!")
        return redirect("login")
    # ? Simply render the page
    context = {"register_active": "active"}
    return render(request, "accounts/register.html", context)


def login(request):

    # ? Know if the request is for form submission then do ->
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(request, username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, "You are now logged in")
            return redirect("dashboard")
        else:
            messages.error(request, "Invalid username or password!")
            return redirect("login")
    # ? Simply render the page
    context = {"login_active": "active"}
    return render(request, "accounts/login.html", context=context)


def dashboard(request):
    user_contacts = Contact.objects.order_by("-contact_date").filter(
        user_id=request.user.id
    )
    context = {"contacts": user_contacts}
    return render(request, "accounts/dashboard.html", context)


def logout(request):
    if request.method == "POST":
        auth.logout(request)
        messages.success(request, "You are now logged out.")
        return redirect("index")
    return redirect("index")

