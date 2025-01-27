from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import login
from django.shortcuts import render, redirect
from .forms import SignupForm

def index(request):
    return render(request, 'users/index.html')


class LoginView(LoginView):
    # TODO: fix and change back
    redirect_authenticated_user = False

    def get_success_url(self):
        return reverse_lazy('users:index')
    
    def form_invalid(self, form):
        messages.error(self.request, 'Invalid username or password')
        return self.render_to_response(self.get_context_data(form=form))



def SignupView(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('users:index')
    
    form = SignupForm()
    return render(request, 'registration/signup.html', {'form':form})