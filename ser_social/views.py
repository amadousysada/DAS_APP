from ser_medical.views import *
from ser_retraite.views import *
from ser_social.views import *
from core.views import *
from ser_social.models import *
from core.models import *
def action_page(request):
    pel=Pelerinage.objects.order_by('id')
    nbre=0
    somme=0
    i=0
    bar_chart = pygal.Histogram()
    bar_chart.x_labels='STATISTIQUE'
    for pe in pel:
        nbre = nbre+1
        somme = somme+pe.frais
        bar_chart.add(str(pe.date_pel.year), [(pe.frais, i, i+0.5)])
        i = i+0.5
    bar_chart.add('Total Frais', [(somme, i, i+0.5)])
    bar = bar_chart.render()
    # context = {'message': 'Hello Pygal!'}
    # return render(request, 'medical/statistique.html', {'bar_chart': bar})
    return render(request, 'ser_social/sociale_page.html',{'pels':pel, 'bar_chart': bar})

def addPele(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            date = request.POST.get('date')
            myfile = request.FILES['file']
            dt = date.split("-")
            print('la date du jour', dt[0])
            if existePel(int(dt[0])):
                return accueil(request)
            else:
                fs = FileSystemStorage()
                filename = fs.save(myfile.name, myfile)
                chemin = 'media/' + filename
                book = pyexcel.get_book(file_name=chemin)
                frais = 0
                peleringe = Pelerinage(date_pel=date)
                peleringe.save()
                for feuille in book:
                    # chaque feuille a un nom
                    print("feuille: %s" % feuille.name)

                    for ligne in feuille:
                        c1 = ligne[0]
                        c2 = ligne[2]
                        frais = c2+frais
                        emp = Employe.objects.get(matricule=c1)
                        ie = InfoEmploye(employe=emp, pelerin=peleringe, somme=c2)
                        ie.save()
                    peleringe.frais = frais
                    peleringe.save()

            return render(request, 'ser_medical/smedical.html')
        # elif request.is_ajax():
        #     errors = json.dumps(form.errors)
        #     return HttpResponse(errors)
        else:
            return render(request, 'ser_retraite/sretraite.html')
    else:
        form = UploadFileForm()
        return render(request, 'ser_social/nouv_pel.html', {'form':form})


def existePel(year):
    pels = Pelerinage.objects.all()
    for pel in pels:
        if (pel.date_pel.year == year):
            return True
    return False