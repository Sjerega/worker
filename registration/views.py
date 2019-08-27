from django.shortcuts import render
from django.views.generic import View
from .models import Category, User, Job, Photo


# class CategoriesMixin():
#    pass


class IndexView(View):
    template_name = 'index.html'

    def get(self, request):
        context = {'categories': Category.objects.all(), 'jobs': Job.objects.all()}
        return render(request, self.template_name, context=context)


class CategoryView(View):
    template_name = 'category.html'

    def get(self, request, slug=None):
#        jobs = Job.objects.filter(category=Category.objects.get(slug=slug)) if slug else Job.objects.all()
        category = Category.objects.get(slug=slug)
#        jobs = Job.objects.filter(category=category)
        context = {
            'categories': Category.objects.all(),
            'category': category,
            'jobs': Job.objects.filter(category=category)
        }
        return render(request, self.template_name, context=context)


class WorkerView(View):
    template_name = 'worker.html'

    def get(self, request, id=None):
        user = User.objects.get(id=id)
        context = {
            'categories': Category.objects.all(),
            'worker': user,
            'jobs': Job.objects.filter(user=user)
        }
        return render(request, self.template_name, context=context)


class JobView(View):
    template_name = 'job.html'

    def get(self, request, id=None):
        # if id:
            context = {
                'categories': Category.objects.all(),
                'job': Job.objects.get(id=id),
                'photos': Photo.objects.filter(job=id),
            }
            return render(request, self.template_name, context=context)
        # else:
        #     redirect
