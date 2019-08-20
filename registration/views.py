from django.shortcuts import render
from django.views.generic import View
from .models import Category


class IndexView(View):
    template_name = 'index.html'

    def get(self, request):
        context = {'categories': Category.objects.all()}
        return render(request, self.template_name, context=context)
