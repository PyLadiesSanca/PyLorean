from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect, HttpRequest, HttpResponsePermanentRedirect, HttpResponseGone
from django.views.generic import RedirectView, TemplateView
from django.views.generic.edit import FormView


class IndexView(TemplateView):
    template_name = 'core/index.html' 


class LoginView(FormView):
    template_name = 'core/login.html'
    form_class = AuthenticationForm
    success_url = '/'
    def my_view(request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                # Redirect to a success page.
                sucess_url = '/' 
        

class LogoutView(RedirectView):
    url = '/login'
    def get(self, request, *args, **kwargs):
        logout(request)
        url = self.get_redirect_url(*args, **kwargs)
        if url:
            if self.permanent:
                return HttpResponsePermanentRedirect(url)
            else:
                return HttpResponseRedirect(url)
        return HttpResponseGone()