from django.conf.urls import url,include
from django.conf.urls.static import static
from django.contrib import admin
from DreamsTrack import views
from account.views import connect
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',views.index, name="home"),
    url(r'^accounts/',include('account.urls')),
    url(r'^dreamsgroup/',include('dreamsgroup.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
