from django.contrib import auth
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse
from django.views.generic import FormView
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView

from blogs.models import Blog, Post
from comments.models import Comment
from core.forms import CreateUserForm

from core.models import User

from django.http import HttpResponseRedirect




class HomePageView(TemplateView):
    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context["BlogCount"] = Blog.objects.all().count()
        context["PostCount"] = Post.objects.all().count()
        context["CommentCount"] = Comment.objects.all().count()
        context["UserCount"] = User.objects.all().count()
        return context

    template_name = "core/home.html"


class RegisterView(CreateView):
    form_class = CreateUserForm
    template_name = 'registration/registration_form.html'

    def upload_file(request):
        if request.method == 'POST':
            form = CreateUserForm(request.POST, request.FILES)
            if form.is_valid():
                instance = User(avatar=request.FILES['file'])
                instance.save()
                return redirect('home')
        else:
            form = CreateUserForm()
        return render(request, 'registration/registration_form.html', {'form': form})

    def get_success_url(self):
        login(self.request, self.object)
        return reverse('home')

    def form_valid(self, form):
        return super(RegisterView, self).form_valid(form)


