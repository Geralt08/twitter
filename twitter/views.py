from django import views
from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView

from twitter import models
from twitter import forms


# Create your views here.

class MainWebpageView(views.View):
    def get(self, request):
        tweets = models.Tweet.objects.order_by('-creation_date').all()
        ctx = {'tweets': tweets}
        return render(request, 'twitter/index.html', ctx)


class TweetComposeView(LoginRequiredMixin, CreateView):
    model = models.Tweet
    form_class = forms.TweetForm
    success_url = reverse_lazy('twitter:index')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


