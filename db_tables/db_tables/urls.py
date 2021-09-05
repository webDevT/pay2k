from django.contrib import admin
from django.urls import path, include, re_path
from _site.views import landing
from django.conf.urls.i18n import i18n_patterns
from django.conf import settings
from django.contrib import admin
from django.views.generic import TemplateView
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'^i18n/', include('django.conf.urls.i18n')),
]

urlpatterns += i18n_patterns(

    re_path(r'^$', landing, name='landing'),
    re_path(r'^catalogue/', TemplateView.as_view(template_name='site/catalogue.html')),
    re_path(r'^company/$', TemplateView.as_view(template_name='site/company.html')),
    # re_path(r'^terms/$', TemplateView.as_view(template_name='site/terms.html')),
    re_path(r'^policy/$', TemplateView.as_view(template_name='site/policy.html')),
    re_path(r'^recent-payouts/$', TemplateView.as_view(template_name='site/recent-payouts.html')),
    re_path(r'^contact/$', TemplateView.as_view(template_name='site/contact.html')),
    re_path(r'^download/$', TemplateView.as_view(template_name='site/download.html')),
    re_path(r'^game/$', TemplateView.as_view(template_name='site/game.html')),
)+ static('/static/', document_root=settings.STATIC_ROOT)