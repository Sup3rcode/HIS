from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import UpdateView
from django.views.generic.edit import CreateView
from .forms import *
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import login, authenticate, update_session_auth_hash
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from django.contrib.auth.forms import PasswordChangeForm
# Create your views here.
def signup(request):
    form = SignUpForm()
    if request.method =='POST':

        form = SignUpForm(request.POST)
        f_name = request.POST.get('first_name')
        l_name = request.POST.get('last_name')
        if form.is_valid():
            user = form.save(commit=False)
            user.first_name = f_name
            user.last_name = l_name
            user.save()
            auth_login(request,user)
            return redirect('App_Home:index')

    return render(request,'signup.html',{'form':form})

class EditView(UpdateView):
    model = Profile
    form_class = ProfileForm
    pk_url_kwarg = 'pk'
    template_name = 'my_account.html'
    success_url = reverse_lazy('App_Home:index')
    def form_valid(self, form ):
        profile = form.save(commit=False)
        profile.Active = True
        profile.save()

        messages.success(self.request, 'thank you From Update Your Profile , HelpDesk TEAM') 
        return redirect('App_Home:index') 
    
class UserProfile(TemplateView):
    template_name = "registration/user-profile.html"

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            context = self.get_context_data(**kwargs)
            context['message'] = "Your password was successfully updated!"
            context['form'] = PasswordChangeForm
            return render(request, self.template_name, context)
        context = self.get_context_data(**kwargs)
        context['form'] = form
        return render(request, self.template_name, context)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = PasswordChangeForm(self.request.user)
        context['username'] = self.request.user.username
        context['user_name'] = str(self.request.user)
        context['email'] = self.request.user.email
        return context


# Create your views here.
def login_view(request):
    # future -> ?next=/articles/create/
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('App_Home:index')
    else:
        form = AuthenticationForm(request)
    context = {
        "form": form
    }
    return render(request, "login.html", context)

from django.contrib.auth import logout
def logout_view(request):
    logout(request)
    return redirect('App_Home:index')