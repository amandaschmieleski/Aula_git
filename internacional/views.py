from django.shortcuts import render
from faker import Faker #cria textos falsos

# Create your views here.
def info(request):
    fake = Faker()
    context = {
        'paragrafo': fake.paragraph(nb_sentences=11),
        'jogadores': [fake.name() for _ in range(11)]
    }
    return render(request, 'internacional/index.html', context)