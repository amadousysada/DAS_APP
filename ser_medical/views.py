import json
from datetime import datetime

import pygal
from django.http import HttpResponse
from django.shortcuts import render
from django.template import RequestContext
from django.template.loader import get_template
from weasyprint import HTML

from core.fusioncharts import FusionCharts
from ser_medical.forms import SoinForm,\
    CliniqueForm, PieceComForm, OrdonnanceForm, StatsForm
from ser_medical.models import Soins,Clinique,PieceComptable,Ordonnances
from core.models import Employe
from ser_retraite.models import *


# Create your views here.



def search_page(request, par1, par2):
    if len(par1) < 1:
        return render(request, 'ser_medical/infos.html', {'text': ""})
        # except:
        #     return render(request, 'medical/infos.html', {'cat': '3'})


    try:
        ob = Employe.objects.get(matricule=par1)
        if ob is not None:
            emp = ob
            year = ob.date_emb.date()
            today = datetime.today().date()
            daty = year
            datm = 0
            datd = 0
            dico = {'daty': daty, 'datm': datm, 'datd': datd}
            statut = 'success'
    except:
        emp = 'aucune correspondance'
        statut = 'error'
        daty = 0
        datm = 0
        datd = 0
        dico = {'daty': daty, 'datm': datm, 'datd': datd}
    if par2 == 'a':
        return render(request, 'ser_medical/infos.html', {'text': emp, 'cat': '1', 'statut': statut, 'liste': dico})
    if par2 == 'b':
        try:
            eng = Engagement.objects(employe = emp)
            return render(request, 'ser_medical/infos.html', {'text': emp, 'statut': statut, 'liste': dico, 'cat': '2', 'eng':eng})
        except:
            return render(request, 'ser_medical/infos.html', {'text': emp, 'statut': statut, 'liste': dico, 'cat': '2'})

    # else:
    #     return render(request, 'medical/infos.html', {'text': 'aucune correspondance'})


def addCharge(request):
    if request.method == 'POST':
        form = SoinForm(request.POST)
        if form.is_valid():
            matricule = request.POST.get("matricule")
            chef_sec=request.POST.get("chef_sec")
            soin = form.save(commit=False)
            soin.Matricule =Employe.objects.get(matricule=matricule)
            soin.chef_sec=chef_sec
            soin.save()
            if request.is_ajax():
                return HttpResponse(content=json.dumps({'success': '/success'}))
        elif request.is_ajax():
            errors = json.dumps(form.errors)
            return HttpResponse(errors)

    else:
        print("inavlide form")
        form = SoinForm()  # An unbound form
        return render(request, 'ser_medical/nouv_charge_med.html', {'form': form})


def liste_clinique(request):
    cliniques = Clinique.objects.order_by('code')
    return render(request, 'ser_medical/liste_cliniques.html', {'cliniques': cliniques})


def ajouter_clinique(request):
    if request.method == 'POST':
        form = CliniqueForm(request.POST)
        if form.is_valid():
            if request.is_ajax():
                form.save()
                return HttpResponse(content=json.dumps({'success': '/success'}))
        elif request.is_ajax():
            errors = json.dumps(form.errors)
            return HttpResponse(errors)
    else:
        form = CliniqueForm()
        return render(request, 'ser_medical/ajouterClinique.html', {'form': form})


def nouv_piece_compt(request):
    if request.method == 'POST':
        form = PieceComForm(request.POST)
        if form.is_valid():
            matricule = request.POST.get("matricule")
            piece = form.save(commit=False)
            piece.beneficiaire = Employe.objects.get(matricule=matricule)
            piece.save()
            if request.is_ajax():
                return HttpResponse(content=json.dumps({'success': '/success'}, RequestContext(request)))
        elif request.is_ajax():
            errors = json.dumps(form.errors)
            return HttpResponse(errors)
    else:
        form = PieceComForm()
        return render(request, 'ser_medical/ajouter_pCompt.html', {'form': form})


def liste_piece(request):
    pieces = PieceComptable.objects.order_by('id')
    return render(request, 'ser_medical/liste_piece.html', {'pieces': pieces})


def liste_prise(request):
    prises = Soins.objects.order_by('id')
    return render(request, 'ser_medical/liste_prise.html', {'prises': prises})


def nouv_ordonnance(request):
    if request.method == 'POST':
        form = OrdonnanceForm(request.POST)
        if form.is_valid():
            type = request.POST.get('type')
            assure = request.POST.get('assure')
            montant = int(request.POST.get('montant'))
            matricule = request.POST.get('matricule')
            ord = form.save(commit = False)
            ord.employe = Employe.objects.get(matricule=matricule)
            if type == '0':
                if assure == '0':
                    rem = (montant*80)/100
                    if rem >= 70000:
                        ord.montant_rem = 105000
                    else:
                        ord.montant_rem = rem+35000

                else:
                    ord.montant_rem = 30000
                ord.save()
            if type == '1':
                if assure == '0':
                    rem = (montant*80)/100
                    if rem >= 70000:
                        form.montant_rem = 105000
                    else:
                        form.montant_rem = rem
                else:
                    ord.montant_rem = 30000
                ord.save()
            if request.is_ajax():
                return HttpResponse(content=json.dumps({'success': '/success'}))
        elif request.is_ajax():
            errors = json.dumps(form.errors)
            return HttpResponse(errors)
    else:
        form = OrdonnanceForm()
        return render(request, 'ser_medical/nouv_ordonnance.html', {'form': form})

# def allocation(request):


def info_charge(request):
    datd = datetime.today().day
    datm = datetime.today().month
    daty = datetime.today().year
    dico = {'daty': daty, 'datm': datm, 'datd': datd}
    return render(request, 'ser_medical/info_charge.html', {'liste': dico})


def liste_ordo(request):
    ordos = Ordonnances.objects.order_by('reference')
    return render(request, 'ser_medical/liste_ordonnance.html', {'ordos': ordos})

def stats_med(request,varM,varA,MA):
    form=StatsForm()
    pie_chart = pygal.Bar()
    bar_chart1 = pygal.Bar()
    if MA == 'mois':

        pie_chart.title = 'STATISTIQUE DES ORDONNANCES 0'+varM+'/'+varA

        pcs=chercher_pc(varM,varA)
        print(pcs)
        ordos=chercher_ordo(varM,varA)
        # print(ordos)

        bar_chart1.title='teste'
        nbre=len(pcs)
        nbre2=0
        smt=0
        smR=0


        for ordo in ordos:
            nbre2=nbre2+1
            smt=smt+ordo.montant
            smR=smR+ordo.montant_rem
        bar_chart1.add("PC",nbre)


        pie_chart.add('ORDONNANCE', nbre2)
        pie_chart.add('TAUX', smt)
        pie_chart.add('REMBOURSE', smR)
        # pie_chart.add('Safari', 4.5)
        # pie_chart.add('Opera', 2.3)
        bar2=pie_chart.render()
        bar1 = bar_chart1.render()

        return render(request, 'ser_medical/statistique.html', {'form':form,'bar_chart1': bar1, 'bar_chart2': bar2, 'ordo':nbre2, 'taux':smt, 'rem':smR, 'pc':nbre})
    if MA == "annee":
        ordos = chercher_ordo('00',varA)
        pcs = chercher_pc('00',varA)
        nbre = len(ordos)
        nbre2 = len(pcs)
        smt = 0
        smR = 0
        for ordo in ordos:
            smt = smt + ordo.montant
            smR = smR + ordo.montant_rem
        bar_chart1.add("PC", nbre2)
        pie_chart.add('ORDONNANCE', nbre)
        pie_chart.add('TAUX', smt)
        pie_chart.add('REMBOURSE', smR)
        bar2 = pie_chart.render()
        bar1 = bar_chart1.render()
        return render(request, 'ser_medical/statistique.html',
                      {'form': form, 'bar_chart1': bar1, 'bar_chart2': bar2, 'ordo': nbre, 'taux': smt, 'rem': smR,
                       'pc': nbre2})

    if MA == "tous" or MA=='accu':
        ordos = Ordonnances.objects.all()
        pcs = Soins.objects.all()
        nbre = len(ordos)
        nbre2 = len(pcs)
        smt = 0
        smR = 0
        for ordo in ordos:
            smt = smt+ordo.montant
            smR = smR+ordo.montant_rem
        bar_chart1.add("PC",nbre2)
        pie_chart.add('ORDONNANCE', nbre)
        pie_chart.add('TAUX', smt)
        pie_chart.add('REMBOURSE', smR)
        bar2 = pie_chart.render()
        bar1 = bar_chart1.render()
        if MA == "accu":
            return render(request, 'ser_medical/statistique_home.html',
                          {'form': form, 'bar_chart1': bar1, 'bar_chart2': bar2, 'ordo': nbre, 'taux': smt, 'rem': smR,
                           'pc': nbre2})
        return render(request, 'ser_medical/statistique.html', {'form':form,'bar_chart1': bar1, 'bar_chart2': bar2, 'ordo':nbre, 'taux':smt, 'rem':smR, 'pc':nbre2})



def statistique(request):
    form = StatsForm()
    ordos = Ordonnances.objects.all()
    pcs = Soins.objects.all()
    year=datetime.today().year
    ordosdic=[]
    ordoj = 0
    ordof = 0
    ordom = 0
    ordoa = 0
    ordomai = 0
    ordojui = 0
    ordojuil = 0
    ordoaou = 0
    ordosep = 0
    ordooc = 0
    ordono = 0
    ordod = 0
    for ordo in ordos:
        if  (str(ordo.date_soum.month)=="1"):
            ordoj=ordoj+ordo.montant_rem
        if (str(ordo.date_soum.month) == "2"):
            ordof = ordof + ordo.montant_rem
        if (str(ordo.date_soum.month) == "3"):
            ordom = ordom + ordo.montant_rem
        if (str(ordo.date_soum.month) == "4"):
            ordoa = ordoa + ordo.montant_rem
        if (str(ordo.date_soum.month) == "5"):
            ordomai = ordomai + ordo.montant_rem
        if (str(ordo.date_soum.month) == "6"):
            ordojui = ordojui + ordo.montant_rem
        if (str(ordo.date_soum.month) == "7"):
            ordojuil = ordojuil + ordo.montant_rem
        if (str(ordo.date_soum.month) == "8"):
            ordoaou = ordoaou + ordo.montant_rem
        if (str(ordo.date_soum.month) == "9"):
            ordosep = ordosep + ordo.montant_rem
        if (str(ordo.date_soum.month) == "10"):
            ordooc = ordooc + ordo.montant_rem
        if (str(ordo.date_soum.month) == "11"):
            ordono = ordono + ordo.montant_rem
        if (str(ordo.date_soum.month) == "12"):
            ordod = ordod + ordo.montant_rem
                # ord={"value":ordo.montant_rem}
        # print(ordo.montant_rem)
        # ordosdic.append(ord)
    # print(ordosdic)
    datasource = {}
    datasource["chart"] = {
        "caption": "Actual Revenues, Targeted Revenues & Profits",
        "subcaption": "Last year",
        "xaxisname": "Month",
        "yaxisname": "Amount (In MRO)",
        "numberprefix": "",
        "theme": "ocean"
    }
    datasource["categories"] = [{
        "category": [
            {"label": "Jan"},
            {"label": "Feb"},
            {"label": "Mar"},
            {"label": "Apr"},
            {"label": "May"},
            {"label": "Jun"},
            {"label": "Jul"},
            {"label": "Aug"},
            {"label": "Sep"},
            {"label": "Oct"},
            {"label": "Nov"},
            {"label": "Dec"}
        ]
    }]
    datasource["dataset"] = [
        {

            "seriesname": "Ordonnances en "+str(year),
            # "renderas": "area",
            # "showvalues": "0",
            # "data":ordosdic
            "data":[
                {"value": ordoj},
                {"value": ordof},
                {"value": ordom},
                {"value": ordoa},
                {"value": ordomai},
                {"value": ordojui},
                {"value": ordojuil},
                {"value": ordoaou},
                {"value": ordosep},
                {"value": ordooc},
                {"value": ordono},
                {"value": ordod}
            ]

        },
        {

            "seriesname": "Ordo",
            # "renderas": "area",
            # "showvalues": "0",
            "data": ordosdic

        }
    ]
    mscombi2dChart = FusionCharts("mscombi2d", "ex3", "100%", 400, "chart-1", "json", datasource)
    return render(request, 'ser_medical/statistique.html', {'output': mscombi2dChart.render()})






def medicale_page(request):
    datasource = {}
    datasource["chart"] = {
        "caption": "Actual Revenues, Targeted Revenues & Profits",
        "subcaption": "Last year",
        "xaxisname": "Month",
        "yaxisname": "Montant (En Ouguiya)",
        "numberprefix": "UM",
        "theme": "ocean"
    }
    datasource["categories"] = [{
        "category": [
            {"label": "Jan"},
            {"label": "Feb"},
            {"label": "Mar"},
            {"label": "Apr"},
            {"label": "May"},
            {"label": "Jun"},
            {"label": "Jul"},
            {"label": "Aug"},
            {"label": "Sep"},
            {"label": "Oct"},
            {"label": "Nov"},
            {"label": "Dec"}
        ]
    }]

    datasource["dataset"] = [{
        "seriesname": "Actual Revenue",
        "data": [
            {"value": "16000"},
            {"value": "20000"},
            {"value": "18000"},
            {"value": "19000"},
            {"value": "15000"},
            {"value": "21000"},
            {"value": "16000"},
            {"value": "20000"},
            {"value": "17000"},
            {"value": "25000"},
            {"value": "19000"},
            {"value": "23000"}
        ]
    }, {
        "seriesname": "Projected Revenue",
        "renderas": "line",
        "showvalues": "0",
        "data": [
            {"value": "15000"},
            {"value": "16000"},
            {"value": "17000"},
            {"value": "18000"},
            {"value": "19000"},
            {"value": "19000"},
            {"value": "19000"},
            {"value": "19000"},
            {"value": "20000"},
            {"value": "21000"},
            {"value": "22000"},
            {"value": "23000"}
        ]
    }, {
        "seriesname": "Profit",
        "renderas": "area",
        "showvalues": "0",
        "data": [
            {"value": "4000"},
            {"value": "5000"},
            {"value": "3000"},
            {"value": "4000"},
            {"value": "1000"},
            {"value": "7000"},
            {"value": "1000"},
            {"value": "4000"},
            {"value": "1000"},
            {"value": "8000"},
            {"value": "2000"},
            {"value": "7000"}
        ]
    }
    ]

    # Create an object for the mscombi2d chart using the FusionCharts class constructor
    mscombi2dChart = FusionCharts("mscombi2d", "ex3", "100%", 400, "chart-1", "json", datasource)

    # returning complete JavaScript and HTML code, which is used to generate chart in the browsers.
    return render(request, 'ser_medical/smedical.html',{'output': mscombi2dChart.render()})


def chercher_pc(mois,annee):
    pcs=Soins.objects.all()
    list=[]
    if mois=='00':
        for pc in pcs:
            if (str(pc.date_soin.year) == annee):
                list.append(pc)
        return list
    for pc in pcs:
        if (str(pc.date_soin.year)==annee and str(pc.date_soin.month)==mois):
            list.append(pc)
    return list


def chercher_ordo(mois,annee):
    ordos=Ordonnances.objects.all()
    list = []
    if mois=='00':
        for ordo in ordos:
            if (str(ordo.date_soum.year) == annee):
                list.append(ordo)
        return list

    for ordo in ordos:
        if (str(ordo.date_soum.year)==annee and str(ordo.date_soum.month)==mois):
            list.append(ordo)
    return list


def pdf(request):
    form = PieceComForm()
    # prises = models.Soins.objects.order_by('id')
    # html_string = render_to_string('ser_medical/liste_prise.html', {'prises': prises})
    # html = HTML(string=html_string)
    # html.write_pdf(target='media/mypdf.pdf',stylesheets=[CSS(settings.STATIC_URL+'css/accueil.css')])
    #
    # fs = FileSystemStorage()
    # with fs.open('mypdf.pdf') as pdf:
    #     response = HttpResponse(pdf, content_type='application/pdf')
    #     response['Content-Disposition'] = 'attachment; filename="mypdf.pdf"'
    #     return response
    #
    # return HttpResponse(response)

def delete(request,type,val):
    if (type == 'pc'):
        Soins.objects.get(id=val).delete()
        prises = Soins.objects.order_by('id')
        return render(request, 'ser_medical/liste_prise.html', {'prises': prises})


def fleet_report_pdf(request,type,val):
    if (type == 'fc'):
        piece = Soins.objects.get(id=val)
        template = get_template("ser_medical/fiche_circulaire.html")
        context = {
            'piece': piece
        }
    if (type == 'pc'):
        piece = Soins.objects.get(id=val)
        template = get_template("ser_medical/info_charge.html")
        context = {
            'piece': piece
        }
    if (type == 'lp'):
        prises = Soins.objects.order_by('id')
        template = get_template("ser_medical/liste_prise.html")
        context = {
            'prises': prises
        }

    html = template.render(RequestContext(request, context))
    response = HttpResponse(content_type="application/pdf")
    HTML(string=html, base_url=request.build_absolute_uri(), url_fetcher=request).write_pdf(response)
    return response