
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from django.urls import path
from django.urls import include, re_path
from appPractica4SvmCnn.View import views

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from appPractica4SvmCnn.View.views import Clasificacion

app_name = 'appPractica4SvmCnn'

schema_view = get_schema_view(
   openapi.Info(
      title="",
      default_version='v1',
      description="",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email=""),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path("admin/", admin.site.urls),
    path('principal/', Clasificacion.vistaPrincipal, name='vistaPrincipal'),
    path('resultado/', Clasificacion.subir_imagen, name='subir_imagen'),
    path('', Clasificacion.subir_imagen, name='vistaPrincipal'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



