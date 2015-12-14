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

    def form_valid(self, form):
        username = form.data['username']
        password = form.data['password']
        user = authenticate(username=username, password=password)        
        if user is not None:
            if user.is_active:
                login(self.request, user)
                # Redirect to a success page.
                return HttpResponseRedirect(self.success_url)
        else:
            context = self.get_context_data()  # pega o contexto atual
            context['errors'] = 'Usuario ou senha invalidos!'  # atualiza o contexto e coloca o erro
            return self.render_to_response(context=context)
        

class LogoutView(RedirectView):
    url = '/login'
    def get(self, request, *args, **kwargs):
        logout(request)
        return super(LogoutView, self).get(request, *args, **kwargs)