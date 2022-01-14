from django.contrib.auth import login
from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView, ListView

from polls.forms import SignUpForm, LogInForm, CreateLinkForm
from polls.models import Link


class MainPageView(TemplateView):
    template_name = 'pages/main_page.html'
    extra_context = {'title': 'Main page'}


class SignUpUserView(FormView):
    template_name = 'pages/bootstrap_form.html'
    form_class = SignUpForm
    success_url = reverse_lazy('main_page')
    extra_context = {'title': 'Sign Up: user'}

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)


class LogInView(FormView):
    template_name = 'pages/bootstrap_form.html'
    form_class = LogInForm
    success_url = reverse_lazy('main_page')
    extra_context = {'title': 'Login'}

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super().form_valid(form)


class LogOutView(LogoutView):
    next_page = reverse_lazy('main_page')


class CreateLinkView(FormView):
    template_name = 'pages/create_order.html'
    form_class = CreateLinkForm
    success_url = reverse_lazy('list_my_links')
    extra_context = {'title': 'Create link'}


class ListMyLinkView(ListView):
    template_name = 'pages/list_my_orders.html'
    extra_context = {'title': 'List my short-link', 'order_model': Link}
