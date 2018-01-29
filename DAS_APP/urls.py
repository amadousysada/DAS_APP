"""DAS_APP URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from DAS_APP import settings
from django.conf.urls import url, include
from django.contrib import admin
from core import views
# from django.views import static
from django.conf.urls.static import static

admin.autodiscover()

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', views.login_page,name='login_page'),
    url(r'^logout/$', views.logout_page, name='logout_page'),
    url(r'^accueil/$', views.accueil, name='accueil'),
    url(r'^pdf/(?P<type>[a-z]{2})/(?P<val>[0-9]{0,9})/$', views.fleet_report_pdf, name='fleet_report_pdf'),

    # SERVICE MEDICAL URLS
    url(r'^accueil/addCharge/$', views.addCharge, name='addCharge'),
    url(r'^accueil/addOrdonnance/$', views.nouv_ordonnance, name='addOrdonnance'),
    url(r'^accueil/listeclinique/$', views.liste_clinique, name='liste_clinique'),
    url(r'^accueil/listePieces/$', views.liste_piece, name='liste_piece'),
    url(r'^accueil/ajouterclinique/$', views.ajouter_clinique, name='ajouter_clinique'),
    url(r'^accueil/ordonnance/$', views.nouv_ordonnance, name='nouv_ordonnance'),
    url(r'^accueil/info_charge/$', views.info_charge, name='info_charge'),
    url(r'^ajouterPieceCom/$', views.nouv_piece_compt, name='nouv_piece_compt'),
    url(r'^accueil/medicale/$', views.medicale_page, name='medicale_page'),
    url(r'^accueil/medicale/delete/(?P<type>[a-z]{2,3})/(?P<val>[0-9]{0,9})/$', views.delete, name='delete'),
    # SERVICE RETRAITE URLS
    url(r'^accueil/retraite/$', views.retraite_page, name='retraite_page'),
    url(r'^accueil/engagement/$', views.engagement, name='addEng'),
    url(r'^accueil/retraite/etat/$', views.addEtat, name='addEtat'),
    url(r'^accueil/retraite/add/$', views.addPele, name='addPele'),
    url(r'^accueil/retraite/search/(?P<par1>[a-z0-9]{5,9})/(?P<par2>[a-z])/$', views.search_emp, name='search_emp'),
    url(r'^teste/$', views.statistique, name='str'),

    # SERVICE SOCIAL URLS
    url(r'^accueil/sociale/$', views.action_page, name='action_page'),



    url(r'^accueil/search/$', views.search_page, name='search_page'),
    url(r'^accueil/loadpage/(?P<par1>[a-z0-9]{2,9})/$', views.loadpage, name='loadpage'),
    url(r'^accueil/service2/(?P<par1>[a-z0-9]{2,9})/(?P<par2>[a-z])/$', views.search_page, name='search_page'),
    url(r'^accueil/stats/(?P<varM>[a-z0-9]{1,9})/(?P<varA>[a-z0-9]{2,9})/(?P<MA>[a-z]{2,9})/$', views.stats_med, name='stats_med'),
    url(r'^accueil/pdf/$', views.pdf, name='pdf'),
    #url(r'^admin/', include(admin.site.urls)),
    #url(r'^explorer/', include('explorer.urls')),
]
urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)