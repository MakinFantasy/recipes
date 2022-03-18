from django.shortcuts import render, reverse
from django.http import HttpResponse
# Create your views here.
DATA = {
    'omlet': {
        'яйца, шт': '2',
        'молоко, л': '0.1',
        'соль, ч.л.': '0.5',
    },
    'pasta': {
        'макароны, г': '0.3',
        'сыр, г': '0.05',
    },
    'buter': {
        'хлеб, ломтик': '1',
        'колбаса, ломтик': '1',
        'сыр, ломтик': '1',
        'помидор, ломтик': '1',
    },
    # можете добавить свои рецепты ;)
}


def home_view(request):
    
    pages = {
        "Главная страница": reverse('home'),
        "Омлет": reverse('omlet'),
        "Паста": reverse('pasta'),
        "Бутер": reverse('buter'),
    }
    context = {
        'pages': pages
    }
    return render(request, 'home.html', context)


def omlet(request):
    try:
        param = request.GET.get("servings")
        serving = int(param)
        omlet = DATA['omlet']
        omlet_str = str()
        for i in omlet:
            try:
                value = int(omlet.get(i))
                value = str(value * serving)
                omlet_str = omlet_str + i.title() + " " + value + "; "
            except ValueError:
                value = float(omlet.get(i))
                value = str(value * serving)
                omlet_str = omlet_str + i.title() + " " + value + "; "
        return HttpResponse(omlet_str)
    except TypeError:
        omlet = DATA['omlet']
        omlet_str = str()
        for i in omlet:
            try:
                value = int(omlet.get(i))
                value = str(value)
                omlet_str = omlet_str + i.title() + " " + value + "; "
            except ValueError:
                value = float(omlet.get(i))
                value = str(value)
                omlet_str = omlet_str + i.title() + " " + value + "; "
        return HttpResponse(omlet_str)

def pasta(request):
    try:
        param = request.GET.get("servings")
        serving = int(param)
        pasta = DATA['pasta']
        pasta_str = str()
        for i in pasta:
            try:
                value = int(pasta.get(i))
                value = str(value * serving)
                pasta_str = pasta_str + i.title() + " " + value + "; "
            except ValueError: 
                value = float(pasta.get(i))
                value = str(value * serving)
                pasta_str = pasta_str + i.title() + " " + value + "; "
        return HttpResponse(pasta_str)
    except TypeError:
        pasta = DATA['pasta']
        pasta_str = str()
        for i in pasta:
            try:
                value = int(pasta.get(i))
                value = str(value)
                pasta_str = pasta_str + i.title() + " " + value + "; "
            except ValueError:
                value = float(pasta.get(i))
                value = str(value)
                pasta_str = pasta_str + i.title() + " " + value + "; "
        return HttpResponse(pasta_str)


def buter(request):
    try:
        param = request.GET.get("servings")
        serving = int(param)
        buter = DATA['buter']
        buter_str = str()
        for i in buter:
            try:
                value = int(buter.get(i))
                value = str(value * serving)
                buter_str = buter_str + i.title() + " " + value + "; "
            except ValueError:
                value = float(buter.get(i))
                value = str(value * serving)
                buter_str = buter_str + i.title() + " " + value + "; "
        return HttpResponse(buter_str)
    except TypeError:
        buter = DATA['buter']
        buter_str = str()
        for i in buter:
            try:
                value = int(buter.get(i))
                value = str(value)
                buter_str = buter_str + i.title() + " " + value + "; "
            except ValueError:
                value = float(buter.get(i))
                value = str(value)
                buter_str = buter_str + i.title() + " " + value + "; "
        return HttpResponse(buter_str)
