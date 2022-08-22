from django.shortcuts import render ,redirect
from django.views import View
from .forms import RegisterUserForm ,LoginUserForm
from .models import CustomUser
from django.contrib import messages  # to ge messages
from django.contrib.auth import authenticate ,login, logout



# The USER can not go to the login page again after registeration :
class RegisterUserView(View) :
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('main:index')
        return super().dispatch(request , *args, **kwargs)

# To show Registe Form to the User :
    def get(self, request,*args, **kwargs):
        form = RegisterUserForm()
        # context ={"form":form} Also one method to use context
        return render(request, 'account_app/register.html',{ "form":form })



    def post(self, request,*args, **kwargs):
        # sourcery skip: remove-unnecessary-else, swap-if-else-branches,get , inquire data
        form=RegisterUserForm(request.POST)
        if  form.is_valid():
            user=form.cleaned_data
            CustomUser.objects.create_user(
                email = user['email'],
                name = user['name'],
                family = user['family'],
                mobile_number =user['mobile_number'],
                gender = user['gender'],
                password = user['password']
                # is_active = True during Registeration we can active it
            )
            messages.success(request, 'Registeration Successfully Done','success')
            return redirect('main:index')
        else:
            messages.error(request,'Information Invalid','ERROR')
            return render(request, 'account_app/register.html',{ "form":form })


class LoginUserView(View) :
     def get(self, request,*args, **kwargs):
        form = LoginUserForm()
        return render(request, 'account_app/login.html',{ "form":form })


     def post(self, request,*args, **kwargs):  # sourcery skip: assign-if-exp
        form=LoginUserForm(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            user=authenticate( username=cd.get('email'),password=cd.get('password'))
            if user is not None:
                db_user=CustomUser.objects.get(email=user.email)#use.email is all datas discoverd by authenticate
                if not db_user.is_admin:
                    messages.success(request,'Successfully DONE')
                    login(request,user)
                    next_url = request.GET.get('next') # keeps next URL !
                    if next_url is not None:
                        return redirect(next_url)
                    else:
                        return redirect('main:index')
                else:
                    messages.warning(request,'User Admin can not enter from here ')
                    return render(request, 'account_app/login.html',{ "form":form })
            else:
                messages.warning(request,'USER wasnot found !')
                return render(request, 'account_app/login.html',{ "form":form })
        else:
            messages.warning(request,'Invalid Information ')
            return render(request, 'account_app/login.html',{ "form":form })



class LogoutUserView(View):
    # if I am log out , I can not call logout
    def dispatch(self, request, *args, **kwargs):
        # sourcery skip: assign-if-exp, reintroduce-else, swap-if-expression
        if not request.user.is_authenticated:
             return redirect('main:index')
        return super().dispatch(request , *args, **kwargs)

    def get(self, request , *args, **kwargs):
        messages.success(request,'Thanks ')
        return redirect('main:index')




