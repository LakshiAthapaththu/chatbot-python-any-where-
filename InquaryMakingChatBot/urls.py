from django.conf.urls import include,url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #if give url like admin/ goto the admin page
    url(r'^useract/',include('useract.urls')),
    url(r'^bot/',include('chatbot.urls')),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
