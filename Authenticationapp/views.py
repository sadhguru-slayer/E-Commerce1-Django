from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.views.generic import View
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.conf import settings
from .utils import generate_token
from django.template.loader import render_to_string, get_template
from django.utils.http import urlsafe_base64_decode,urlsafe_base64_encode
from django.utils.encoding import force_bytes,force_str
from django.contrib.auth import login as auth_login
import re
def signup(request):
    context={
        'dis':'inline'
    }
    if request.method=='POST':
        email=request.POST['email']
        passw=request.POST['passw']
        cpassw=request.POST['cpassw']
        if len(passw)<=8:
            messages.warning(request,"Password is not long enough🙂",context)
            return render(request,'Authentication/signup.html')
        if not re.search("[a-z]", passw) :
            messages.warning(request,"Password should contain atleast a lowercase🙂",context)
            return render(request,'Authentication/signup.html')
        if not re.search("[A-Z]", passw) :
            messages.warning(request,"Password should contain atleast an uppercase🙂",context)
            return render(request,'Authentication/signup.html')
        if not re.search("[0-9]", passw) :
            messages.warning(request,"Password should contain atleast a numerical🙂",context)
            return render(request,'Authentication/signup.html')
        if not re.search("[_@$]" , passw) :
            messages.warning(request,"Password should contain atleast a special character🙂",context)
            return render(request,'Authentication/signup.html')
        if re.search("\s" , passw) :
            messages.warning(request,"Password should not contain spaces🙂",context)
            return render(request,'Authentication/signup.html')
        if passw!=cpassw :
            messages.warning(request,"Password is not match☹️",context)
            return render(request,'Authentication/signup.html')
        try:
            if User.objects.get(username=email):
                    messages.warning(request,"User is already there☹️",context)
                    return render(request,'Authentication/signup.html')
        except:
            pass

        user= User.objects.create_user(email,email,passw)
        user.is_active=False
        user.save()
        email_subject='Activate your account'
        message=get_template('activate_acc.html').render({
            'user':user.email,
            'domain':'127.0.0.1:8000',
            'uid':urlsafe_base64_encode(force_bytes(user.pk)),
            'token':generate_token.make_token(user),
        })

        email_message = EmailMessage(email_subject, message, settings.EMAIL_HOST_USER, [user.email])
        email_message.content_subtype='html'
        email_message.send()
        #           )
        return redirect('/auth/login/')

    return render(request,'Authentication/signup.html')

class ActivateAccountView(View):
    def get(self,request,uidb64,token):
        try:
            uid=force_str(urlsafe_base64_decode(uidb64))
            user=User.objects.get(pk=uid)
        except Exception as identifier:
            user=None
        if user is not None and generate_token.check_token(user,token):
            user.is_active=True
            user.save()
            messages.info(request,"Account Activated Successfully")
            return redirect('/auth/login')
        return render(request,'activate.html')

def logins(request):
    context={
                'dis':'inline'
            }
    if request.method=='POST':
        email=request.POST['email']
        passwo=request.POST['password']
        try:
            username = User.objects.filter(email=email).first()
        except User.DoesNotExist:
            username = None
        user = authenticate(username=username, password=passwo)
        if user is not None:
            auth_login(request, user)
            user.is_active=True
            messages.warning(request, "You have successfully logged in as "+email+".", context)
            return redirect('/')
        else:
            messages.warning(request, "Your email "+email+" or password is incorrect", context)
            return render(request,'Authentication/login.html')

    return render(request,'Authentication/login.html')
def logouth(request):
    logout(request)
    return redirect('/')