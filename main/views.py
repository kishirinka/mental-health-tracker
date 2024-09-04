from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2306226864',
        'name': 'Irma Nia Alwijah',
        'class': 'PBP B'
    }

    return render(request, "main.html", context)