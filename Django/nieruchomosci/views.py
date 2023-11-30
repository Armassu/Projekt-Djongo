from django.shortcuts import render
from .models import nieruchomosci  # Zmieniłem 'YourModel' na 'nieruchomosci'

def home(request):
    # Pobierz wszystkie obiekty z modelu
    all_objects = nieruchomosci.objects.all()  # Zmieniłem 'YourModel' na 'nieruchomosci'

    # Pobierz obiekt po konkretnej wartości pola (zmień 'nazwa_pola' na rzeczywistą nazwę pola)
    specific_object = nieruchomosci.objects.get(nazwa_pola='wartość')  # Zmieniłem 'YourModel' na 'nieruchomosci'

    # Dodaj te dane do kontekstu
    dane = {
        'nazwa_zmiennej': 'Wartość zmiennej',
        'all_objects': all_objects,
        'specific_object': specific_object,
    }

    # Renderuj widok, przekazując dane w kontekście
    return render(request, 'nieruchomosci/home.html', context=dane)
