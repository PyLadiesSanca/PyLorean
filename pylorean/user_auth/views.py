from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect
from django.views.generic import RedirectView
from django.views.generic.edit import FormView


class LoginView(FormView):
    template_name = 'user_auth/login.html'
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
            context = self.get_context_data()
            context['errors'] = 'Usuario ou senha invalidos!'
            return self.render_to_response(context=context)


class LogoutView(RedirectView):
    url = '/login'

    def get(self, request, *args, **kwargs):
        logout(request)
        return super(LogoutView, self).get(request, *args, **kwargs)
