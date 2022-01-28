
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('', views.showRegHTML, name="reg"),
                  path('signUpUser/', views.signUpUser, name="signUp"),
                  path('encrypter', views.showEncrypterHTML, name="encrypter"),
                  path('Encr', views.Encr, name="Encr"),
                  path('CheckMessages/', views.showCheckMessagesHTML, name="CheckMessages"),
                  path('CheckMessages/CheckMessagesInDB', views.CheckMessagesInDB, name="checkMessagesInDB")
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

