from django.urls import path, include
from django.views.generic import TemplateView

app_name = "blog"

urlpatterns = [
    path('api/', include('blog.api.urls')),
    path('', TemplateView.as_view(template_name="blog/index.html"))
]
