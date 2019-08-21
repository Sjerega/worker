from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
#from django.views.generic.base import TemplateView
from registration.views import IndexView, CategoryView, WorkerView, JobView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view()),
    path('category/<str:slug>/', CategoryView.as_view()),
    path('job/<int:id>/', JobView.as_view()),
    path('worker/<int:id>/', WorkerView.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
