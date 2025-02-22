from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


# Importação das views

from home.views import home, adote_pet
from cadastro_pet.views import criar_pet
from detalhes_pet.views import detalhes_pet


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('cadastrar-pet/', criar_pet),
     path('detalhes/<uuid:id>/', detalhes_pet, name='detalhes_pet'),
    #Formulário de Adoção
    #Sobre => espaço para apresentação da Squad
    #Página que mostra todos os animais + barra de pesquisa
    path('adote/', adote_pet, name = 'adote'), #junto com a listagem dos bicinhos disponiveis e a barra de pesquisa
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)