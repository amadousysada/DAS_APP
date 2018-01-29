from ser_medical.views import *
from ser_retraite.views import *
from ser_social.views import *
from ser_medical.forms import SoinForm,\
    CliniqueForm, PieceComForm, OrdonnanceForm, UploadFileForm, StatsForm
from ser_retraite.forms import EngagementForm
from core import models
from ser_retraite import models as mr

def retraite_page(request):
    return render(request, 'ser_retraite/sretraite.html')


def engagement(request):
    if request.method == 'POST':
        form = EngagementForm(request.POST)
        if form.is_valid():
            matricule = request.POST.get('matricule')
            date = request.POST.get('date_en')

            eng = form.save(commit=False)
            eng.employe = models.Employe.objects.get(matricule=matricule)
            eng.date_en = date
            eng.save()
            if request.is_ajax():
                return HttpResponse(content=json.dumps({'success': '/success'}))
        elif request.is_ajax():
            errors = json.dumps(form.errors)
            return HttpResponse(errors)
    else:
        form = EngagementForm()
        return render(request,'ser_retraite/engagement.html',{'form': form})


def liste_engagement(request):
    engs = mr.Engagement.objects.order_by('-date_en')
    return render(request, 'ser_retraite/ListeEngagement.html', {'engs': engs})


def search_emp(request, par1,par2):
    try:
        emp = models.Employe.objects.get(matricule=par1)
        # eng = models.Engagement.objects(employe = emp)
        statut = "success1"
    except:
        statut = "error1"
        emp = par1
    if par2 == 'a':
        return render(request, 'ser_retraite/info_emp.html', {'text': emp, 'statut': statut, })
    if par2 == 'b':
        engs = mr.Engagement.objects.filter(employe=emp)
        form = EngagementForm()
        return render(request, 'ser_retraite/info_emp.html', {'engs': engs, 'cat': '3', 'form':form})