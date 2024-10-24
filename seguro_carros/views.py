from django.shortcuts import render
from faker import Faker

# Create your views here
def info(request):
    fake = Faker()
    context = {
        'paragrafo': fake.paragraph(nb_sentences=11),
        'segurados': [fake.name() for _ in range(11)]
    }
    return render(request, 'seguro_carros/index.html', context)