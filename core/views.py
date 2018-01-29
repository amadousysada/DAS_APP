from django.shortcuts import render
# from weasyprint import HTML, CSS
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from ser_medical import models
from datetime import datetime
import json
from django.core.files.storage import FileSystemStorage
import pygal
import django_excel as excel
import os
import pyexcel
from ser_medical.views import *
from ser_retraite.views import *
from ser_social.views import *
from core.forms import LoginForm, UploadFileForm

# Create your views here.


def login_page(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            login = form.cleaned_data['login']
            password = form.cleaned_data['password']
            user = auth.authenticate(username=login, password=password)
            if user is not None and user.is_active:
                auth.login(request, user)
                if request.is_ajax():
                    return HttpResponse(content=json.dumps({'success': 'accueil'}))
                # return redirect('accueil')  # Redirect after POST
            else:
                if request.is_ajax():
                    return HttpResponse(content=json.dumps({'error': '/'}))
                    # return HttpResponse(content=json.dump({'success': 'login_page','errors': form.errors}))
        elif request.is_ajax():
            errors = json.dumps(form.errors)
            return HttpResponse(errors)

    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def logout_page(request):
    auth.logout(request)
    return HttpResponseRedirect("/")


def accueil(request):
    if request.user.groups.filter(name="dgen").exists():
        print("utilisateur Directeur")
        return render(request, 'admin.html')
    if request.user.groups.filter(name="c_ser").exists():
        print("utilisateur chef service")
        return render(request, 'accueil.html')
    if request.user.groups.filter(name="c_sec").exists():
        print("utilisateur chef section")
        return render(request, 'accueil.html')
    return render(request, 'accueil.html')


def loadpage(request, par1):
    if request.is_ajax():
        if par1 == 'sm':
            return render(request, 'ser_medical/smedical.html')
        if par1 == 'sr':
            return retraite_page(request)
        if par1 == 'smpcm':
            return addCharge(request)
        if par1 == 'smpc':
            return nouv_piece_compt(request)
        if par1 == 'lc':
            return liste_clinique(request)
        if par1 == 'ajc':
            return ajouter_clinique(request)
        if par1 == 'smlpc':
            return liste_piece(request)
        if par1 == 'aor':
            return nouv_ordonnance(request)
        if par1 == 'lor':
            return liste_ordo(request)
        if par1 == 'lpcm':
            return liste_prise(request)
        if par1 == 'stats':
            return statistique(request)
        if par1 == 'feng':
            return engagement(request)
        if par1 == 'leng':
            return liste_engagement(request)
        if par1 == 'sajnp':
            return addPele(request)


def addEtat(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            filehandle = request.FILES['file']
            # return excel.make_response(filehandle.get_sheet(), "csv")
            # filename = request.FILES.get('file').filename
            content = request.files['file'].read()
            # extension = filename.split(".")[-1]
            if os.version_info[0] > 2:
                # in order to support python 3
                # have to decode bytes to str
                content = content.decode('utf-8')
            # sheet = excel.get_sheet(file_type=extension, file_content=content)
            sheet = excel.get_sheet(file_content=content)
            # sheet.name_columns_by_row(0)
            # date = request.POST.get('date')
            # peleringe = models.Pelerinage(date_pel=date)
            # # peleringe.save()
            # # book = xlrd.open_workbook(file)
            # sheet = pyexcel.get_sheet(file_name=file)
            # handle file upload
            # Obtain the file extension and content
            # pass a tuple instead of a file name

            # then use it as usual
            frais=0
            # for row_index in (sheet):
            #     row = ""
            #     # c1 = sheet.cell(rowx=row_index, colx='frais').value
            #     c1=(row_index['frais'])
            #     # frais=(frais+21)
            #     # for col_index in (sheet.ncols):
            #     # c2 = sheet.cell(rowx=row_index, colx='matricule').value
            #     c2=row_index['matricule']
            #     emp=models.Employe.objects.get(matricule=int(c2))
            #     ie=models.InfoEmploye(employe=emp,pelerin=peleringe,somme=int(c1))
            #     ie.save()
                    # if type(value) is unicode:
                #         value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore')
                #     row += "{0} - ".format(value)

            # request.FILES.get('file').save_book_to_database(
            #     models=[models.InfoEmploye],
            #     mapdicts=[
            #         ['matricule', 'somme', 'slug'],
            #         ['question', 'choice_text', 'votes']]
            # )
            # eng = form.save(commit = False)
            # eng.employe = models.Employe.objects.get(matricule = matricule)
            # eng.date_en = date
            # eng.save()
            # if request.is_ajax():
            #     return HttpResponse(content=json.dumps({'success': '/success'}))
            # else:
            # return render(request, 'medical/smedical.html')
        # elif request.is_ajax():
        #     errors = json.dumps(form.errors)
        #     return HttpResponse(errors)
        else:
            return render(request, 'ser_retraite/sretraite.html')
    else:
        form = UploadFileForm()
        return render(request,'ser_retraite/etat.html',{'form': form})