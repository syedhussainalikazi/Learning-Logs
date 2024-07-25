from django.shortcuts import render,reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import logout,login,authenticate
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('learning_logs:index'))
def register(request):
    if request.method != 'POST':
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            print('user created')
            new_user = form.save()
            authentiated_user = authenticate(username=new_user.username,password=request.POST['password1'])
            login(request,authentiated_user)
            return HttpResponseRedirect(reverse('learning_logs:index'))
    context = {'form':form}
    return render(request,'users/register.html',context)