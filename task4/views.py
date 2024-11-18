from django.shortcuts import render

def main(request):
    title = "Главная"
    context = {
        'Title': title,
    }
    return render(request, 'main.html', context)

def second(request):
    title = "Игры"
    games = ["Atomic Heart", "Cyberpunk", "PayDay 2"]
    context = {
        'Title': title,
        'games': games,
    }
    return render(request, 'second.html', context)
 
def third(request):
    title = "Корзина"
    context = {
        'Title': title,
    }
    return render(request, 'third.html', context)