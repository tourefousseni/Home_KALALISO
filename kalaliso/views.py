from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from kalaliso.models import Person, Depense, Mesure, Commande, Commande_Detail, Produit
from kalaliso.form import PersonForm, MesureForm, DepenseForm, Depense_DetailForm, \
    CommandeForm, Commande_DetailForm, ProductForm


# Create your views here.

# def loop(request):
#     template = loader.get_template('folders_html/index.html')
#     return HttpResponse(template.render({}, request))

def look(request):
    return render(request, 'folders_html/home.html')

def indexpage(request):
    return render(request, 'folders_html/index.html')

# def newPage(request):
#
#     sta  = request.POST.get("radio1")
#     pre  = request.POST.get("prenom1")
#     no   = request.POST.get("nom1")
#     se   = request.POST.get("radio")
#     cont = request.POST.get("Contact")
#
#     data = Person(status=sta, prenom=pre, nom=no, sex=se, contact_1=cont)
#     data.save()
#     return HttpResponse(request, {})


# def command_client(request):
#     return render(request, 'folders_html/command.html')

# def mesure_client(request):
#     return render(request, 'folders_html/mesure.html')

def thanks(request):
    return HttpResponse('Thanks, your form has been processed')

def get_person(request):
    if request.method == 'POST':

            sta  = request.POST.get("status")
            se   = request.POST.get("sex")
            pre  = request.POST.get("prenom")
            no   = request.POST.get("nom")
            cont = request.POST.get("contact_1")
            ema = request.POST.get("email")
            cat = request.POST.get("categorie")
            dom = request.POST.get("domicile")
            al = request.POST.get("alias")
            pro = request.POST.get("profession")
            cont2 = request.POST.get("contact_2")
            dtna = request.POST.get("date_naissance")
            nat  = request.POST.get("nationalité")
            tut = request.POST.get("tutuelle")
            telep = request.POST.get("telephone_fix")
            nref = request.POST.get("numero_reference")
            nin = request.POST.get("nina")

            data = Person(status=sta, prenom=pre, nom=no,
                          sex=se, contact_1=cont, email=ema,
                          categorie=cat, domicile=dom, alias=al,
                          profession=pro, contact_2=cont2, date_naissance=dtna,
                          nationalite=nat, tutuelle=tut, telephonique_fix=telep,
                          numero_reference=nref, nina=nin,)

            data.save()
            return HttpResponseRedirect(reverse('thanks'))
    else:
       form = PersonForm()
    return render(request, '../templates/form.html', {'form':form})


def list_person(request):
     model = Person
     list_p = Person.objects.all()

# context = {'year': year, 'article_list': a_list}
     return render(request, '../templates/list_person.html')


# def merci(request):
#     return HttpResponse('Thanks, your mesure had well added')


def product(request):
    if request.method == 'POST':

        pro = request.POST.get("produit")
        data = Produit(produit=pro)

        data.save()
        return HttpResponseRedirect(reverse('thanks to select ours products'))
    else:
        form = ProductForm()
    return render(request, 'folders_html/product.html', {'form': form})


def mesure_client(request):
    if request.method == 'POST':
            coud      = request.POST.get("coude")
            epau      = request.POST.get("epaule")
            ma        = request.POST.get("manche")
            to_ma     = request.POST.get("tour_manche")
            tail      = request.POST.get("taille")
            poitr     = request.POST.get("pointrine")
            lo_bo     = request.POST.get("longueur_boubou")
            lo_pa     = request.POST.get("longueur_patanlon")
            fes       = request.POST.get("fesse")
            cei       = request.POST.get("ceinture")
            cui       = request.POST.get("cuisse")
            pat       = request.POST.get("patte")

            data = Mesure(coude=coud, epaule=epau, manche=ma,
                          tour_manche=to_ma, taille=tail, poitrine=poitr,
                          longueur_boubou=lo_bo, longueur_patanlon=lo_pa,
                          fesse=fes, ceinture=cei, cuisse=cui, patte=pat,)
            data.save()
            return HttpResponseRedirect(reverse('merci'))
    else:
       form = MesureForm()
    return render(request, 'folders_html/mesur.html', {'form':form})


def depenses(request):
    if request.method == 'POST':

            mont  = request.POST.get("montant_total")
            isv   = request.POST.get("is_valide")
            cre  = request.POST.get("created_at")

            data = Depense(montant_total=mont,
                           is_valide=isv,
                           created_at=cre)
            data.save()
            return HttpResponseRedirect(reverse('thanks'))
    else:
        form = DepenseForm()
    return render(request, 'folders_html/depense.html', {'form': form})


def depenses_detail(request):
    if request.method == 'POST':

            tyd  = request.POST.get("type_depense")
            de   = request.POST.get('depense')
            tym  = request.POST.get("type_materiel")
            qte   = request.POST.get("quantite")
            pr_un   = request.POST.get("prix_unitaire")
            mont_un   = request.POST.get("montant_unitaire")
            des   = request.POST.get("description")
            cre  = request.POST.get("created_at")

            data = Depense(type_depense=tyd, depense=de, type_materiel=tym,
                           quantite=qte, prix_unitaire=pr_un, montant_unitaire= mont_un,
                           description= des, created_at=cre)
            data.save()
            return HttpResponseRedirect(reverse('thanks for added new depense'))
    else:
        form = Depense_DetailForm()
    return render(request, 'folders_html/depense_detail.html', {'form': form})


def new_command(request):
    if request.method == 'POST':

        recep = request.POST.get("reception")
        mont = request.POST.get("montant_total")
        rendv = request.POST.get("rendez_vous")
        liv = request.POST.get("livre")
        cre  = request.POST.get("created_at")

        data = Commande(reception=recep,
                        montant_total=mont,
                        rendez_vous=rendv,
                        livre=liv,
                        created_at=cre)
        data.save()
        return HttpResponseRedirect(reverse('thanks for new command'))
    else:
        form = CommandeForm()
    return render(request, 'folders_html/command.html', {'form': form})


def commande_details(request):
        if request.method == 'POST':

            img  = request.POST.get("image")
            cout = request.POST.get("couture")
            tis  = request.POST.get("tissu")
            cou  = request.POST.get("couloir")
            qte  = request.POST.get("quantite")
            pri  = request.POST.get("price")
            ava  = request.POST.get("avance")
            rel  = request.POST.get("reliquat")
            rem  = request.POST.get("remise")
            cre  = request.POST.get("created_at")

            data = Commande_Detail(image=img, couture=cout, tissu=tis,
                                   couloir=cou, quantite=qte, price=pri,
                                   avance=ava, reliquat=rel, remise=rem, created_at=cre)
            data.save()
            return HttpResponseRedirect(reverse('thanks for new command detail'))
        else:
            form = Commande_DetailForm()
        return render(request, 'folders_html/command_detail.html', {'form': form})


