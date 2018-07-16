from django.shortcuts import render,redirect,get_object_or_404
from .forms import SingUpForm,ContactForm
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.
from .models import SignUp
def home(request):
    if request.method=='POST':
        
        form = SingUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = SingUpForm()
        return render(request,'newsletter/home.html',{'form':form})

def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form_email = form.cleaned_data.get('email')
        form_full_name = form.cleaned_data.get('full_name')
        form_message = form.cleaned_data.get('message')
        form_subject = form.cleaned_data.get('subject')
      

        send_mail(f'{form_subject},{form_full_name}',form_message,'tomastorres9807@gmail.com',['tomastorres9807@gmail.com'],fail_silently=False)
    return render(request,'newsletter/contact.html',{'form':form})