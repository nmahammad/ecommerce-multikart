from django.shortcuts import redirect, render
from accounts.forms import RegisterForm

# Create your views here.
def register(request):
    register_form = RegisterForm()
    if request.method == 'POST' and "register" in request.POST:
        register_form = RegisterForm(data=request.POST)
        if register_form.is_valid():
            user = register_form.save(request)
            user.username = 'user_' + str(user.id)
            user.set_password(register_form.cleaned_data['password'])
            user.save()
            return redirect('/')
    
    context = {
        'register_form' : register_form
    }
    return render(request , 'register.html' , context)




def login(request):
    return render(request,'login.html',)


def forget_password(request):
    return render(request, 'forget_pwd.html' )

