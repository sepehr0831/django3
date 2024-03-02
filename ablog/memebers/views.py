from django.shortcuts import get_object_or_404, render
# for membershib
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm , PasswordChangeForm 
from django.urls import reverse_lazy
from .forms import SignUpForm , EditProfileFrom , passwordChangedForm , ProfileForm , EditProfilePageFrom
from django.contrib.auth.views import PasswordChangeView
from django.views.generic import  DetailView , CreateView
from theblog.models import profile
# Create your views here.


class CreateProfilePageView(CreateView):
    model = profile
    template_name = "registration/create_profile.html"
    form_class= ProfileForm


    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class EditProfilePageview(generic.UpdateView):
    model = profile
    template_name ="registration/edit_profile_page.html"
    form_class= EditProfilePageFrom
    success_url = reverse_lazy("home")


class ShowProfilePageView(DetailView):
    model = profile
    template_name = "registration/user_profile.html"


    def get_context_data(self,*args,**kwargs):
        users =profile.objects.all()
        context =super(ShowProfilePageView, self).get_context_data(*args,**kwargs)
        page_user = get_object_or_404(profile, id=self.kwargs['pk'])

        context["page_user"] = page_user
        return context




class PasswordsChangeView(PasswordChangeView):

    form_class = passwordChangedForm
    #form_class = PasswordChangeForm
    #success_url = reverse_lazy("home")
    success_url = reverse_lazy("password_success")




def password_success(request):
    return render(request,"registration/password_success.html", {})






class UserRegistrationView(generic.CreateView):
    form_class = SignUpForm
    template_name = "registration/register.html"
    success_url = reverse_lazy("login")

    
class UserEditView(generic.UpdateView):
    form_class = EditProfileFrom
    template_name = "registration/edit_profile.html"
    success_url = reverse_lazy("home")
    #for see information in edit_profile page
    def get_object(self):
        return self.request.user