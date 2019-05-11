from django import views
from django.shortcuts import render

from twitter import models


# Create your views here.

class MainWebpageView(views.View):
    def get(self, request):
        tweets = models.Tweet.objects.all().order_by('-creation_date')
        ctx = {'tweets': tweets}
        return render(request, 'twitter/index.html', ctx)
