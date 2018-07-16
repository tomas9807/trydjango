from django.shortcuts import render,redirect,get_object_or_404
from .forms import SingUpForm,ContactForm
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
        email = form.cleaned_data.get('email')
        print(email)
    return render(request,'newsletter/forms.html',{'form':form})