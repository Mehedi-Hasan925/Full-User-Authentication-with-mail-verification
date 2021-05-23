from django.shortcuts import redirect, render,HttpResponseRedirect
from django.utils import http
from authentication_app import forms
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse,reverse_lazy
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UserChangeForm,PasswordChangeForm
from django.contrib import messages
from django.utils.encoding import force_bytes,force_text,DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from .utils import generate_token
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
from django.views.generic import View

# Create your views here.
def sign_up(request):
    form = forms.SignupForm()
    has_error = False
    if request.method == 'POST':
        form = forms.SignupForm(data=request.POST)
        if form.is_valid():
            email_acc = form.cleaned_data.get('email')
            username = form.cleaned_data.get('username')

            if User.objects.filter(username=username).exists():
                messages.add_message(request,messages.ERROR,'This Username have already taken. Choose a new one.')
                has_error = True

            if User.objects.filter(email=email_acc).exists():
                messages.add_message(request,messages.ERROR,'This Email have already taken.')
                has_error = True

            if has_error:
                diction = {'has_error':has_error,'form':form}
                return render(request,'authentication_app/register.html',context=diction)
            
            else:
                user = form.save(commit=False)
                user.is_active = False
                user.save()
                messages.add_message(request,messages.SUCCESS,'Check your Email to activate account!')
                # create doamin
                #relative url to verification
                #encode uid 
                #token
                uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
                token = generate_token.make_token(user)
                domain = get_current_site(request).domain
                relative_url = reverse('authentication_app:activate',kwargs={'uidb64':uidb64,'token':token})
                # activate_url ='https://'+domain+relative_url
                activate_url ='http://'+domain+relative_url

                email_body = "Hello"+" "+user.first_name + " "+ user.last_name + ", "+ "Follow the below link to verify your Explore account\n" + activate_url
                email_subject = 'Account activation from explore'
                # message = render_to_string('authentication_app/activate.html',
                # {
                #     'user':user,
                #     'domain':domain,
                #     'uidb64':uidb64,
                #     'token':token
                # }
                # )
                email_message = EmailMessage(
                email_subject,
                email_body,
                settings.EMAIL_HOST_USER,
                [email_acc],
                )
                email_message.send()
                HttpResponseRedirect(reverse('authentication_app:sign_up'))
            
    diction = {'form':form,'has_error':has_error}
    return render(request,'authentication_app/register.html',context=diction)


def log_in(request):
    form = forms.LoginForm()
    if request.method == 'POST':
        form = forms.LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user =  authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return HttpResponseRedirect(reverse('authentication_app:home'))

    diction = {'form':form}
    return render(request,'authentication_app/log_in.html',context=diction)


@login_required
def Home(request):
    diction = {}
    return render(request,'authentication_app/home.html')


class ActivateView(View):
    def get(self,request,uidb64,token):
        try:
            uid = force_text(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        
        except Exception as identifier:
            user=None
        
        if user is not None and generate_token.check_token(user,token):
            user.is_active = True
            user.save()
            messages.add_message(request,messages.INFO, 'Congratualations! Account activated successfully')
            return redirect('authentication_app:log_in')
        
        return render(request,'authentication_app/activate_fail.html')


def Log_out(request):
    logout(request)
    messages.add_message(request,messages.INFO, 'Logout successfully')
    return HttpResponseRedirect(reverse('authentication_app:log_in'))