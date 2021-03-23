from django.shortcuts import render, redirect
from django.core.paginator import Paginator

from .models import Product, News, Materialimodel
from .forms import ObratnayaForm, SvoyaForm, ZakazForm


# Главная страница сайта
def index(request):
    error = ''
    ok = ''

    newsmodels = News.objects.order_by('-id')[:3]
    product_model = Product.objects.order_by('id')[:2]
    product_model_mal = Product.objects.filter(typedoma=1).order_by('-id')[:3]
    product_model_sred = Product.objects.filter(typedoma=2).order_by('-id')[:3]
    product_model_bolsh = Product.objects.filter(typedoma=3).order_by('-id')[:3]

    if request.method == 'POST':
        form = ObratnayaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма плохая'
    form = ObratnayaForm()

    context = {
        'form': form,
        'error': error,
        'ok': ok,
        'newsmodels': newsmodels,
        'product_model': product_model,
        'product_model_mal': product_model_mal,
        'product_model_sred': product_model_sred,
        'product_model_bolsh': product_model_bolsh
    }
    return render(request, 'main/index.html', context)


# О компании
def about(request):
    return render(request, 'main/spasibo.html')


# Шаблон пагинации (запрос, обьект_бд, кол-во начальное на странице)
def paginor_shablon(request, obj, kolvo):
    paginator = Paginator(obj, kolvo)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return page_obj


# Страница со всеми шаблонными моделями
def modelirovanie(request):
    housemodels = Product.objects.order_by('-id')
    page_obj = paginor_shablon(request, housemodels, 6)
    return render(request, 'main/modelirovanie.html', {"page_obj": page_obj})


# Страница со всеми новостями
def news(request):
    news = News.objects.order_by('-id')
    page_obj = paginor_shablon(request, news, 6)
    return render(request, 'main/news.html', {"page_obj": page_obj})


# Страница со всеми материалами
def materials(request):
    material = Materialimodel.objects.order_by('-id')
    page_obj = paginor_shablon(request, material, 6)
    return render(request, 'main/materials.html', {"page_obj": page_obj})


# Полная страница материала
def materialfull(request, slug):
    materialmodels = Materialimodel.objects.get(url=slug)
    return render(request, 'main/full_material.html', {"materialmodels": materialmodels})


# Полная страница новости
def newsfull(request, slug):
    newsmodels = News.objects.get(url=slug)
    return render(request, 'main/full_news.html', {"newsmodels": newsmodels})


# Полная страница продукта(дома)
def productfull(request, slug):
    housemodels = Product.objects.get(url=slug)
    materials = Materialimodel.objects.order_by('-id')

    content = {
        'housemodels': housemodels,
        'materials': materials
    }
    return render(request, 'main/full_model.html', content)


# Рендер только модели GLTF
def render_model_house(request, slug):
    title = "slug"
    name = slug +'.gltf'
    modelname = {
        'title': title,
        'name': name
    }

    return render(request, 'main/model_house1.html', modelname)


# Форма заказа по своему чертежу
def svoyafunk(request):
    error = ''
    if request.method == 'POST':
        form = SvoyaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('spasibo')
        else:
            error = 'Форма плохая'
    form = SvoyaForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/svoyamodel.html', context)


# Страница спасибо
def spasibo1(request):
    return render(request, 'main/spasibo.html')

def spasibo2(request):
    return render(request, 'main/spasibo1.html')


# Форма заказа по шаблону
def zakaz(request, slug):
    error = ''
    housemodels = Product.objects.get(url=slug)
    domtitle = housemodels.title
    domnumber = housemodels.housenumber
    itoginfa = domtitle + ', Дом №' + domnumber
    modeldoma = {'name_house': itoginfa}
    if request.method == 'POST':
        form = ZakazForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('spasibo')
        else:
            error = 'Форма плохая'

    form = ZakazForm(modeldoma, auto_id=False)


    context = {
        'form': form,
        'error': error,
        'housemodels': housemodels,
        'nomerdoma': domnumber
    }
    return render(request, 'main/zakazdoma.html', context)


def kontakti(request):
    error = ''
    if request.method == 'POST':
        form = ObratnayaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('spasibo2')
        else:
            error = 'Форма плохая'
    form = ObratnayaForm()

    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/kontakti.html', context)