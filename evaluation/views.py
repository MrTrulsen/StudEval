from django.shortcuts import render
from django.http import HttpResponse

tests = [
    {
        'question': '1',
        'text': 'Hvor mange sure agurker er det i en 1kg kasse når den faller 50 km/t',
        'teacherDifficulity': 50,
        'teacherImportance': 90
    },
    {
        'question': '2',
        'text': 'Hvor mange sure agurker er det i en 90kg kasse når den faller 10 km/t',
        'teacherDifficulity': 90,
        'teacherImportance': 30
    }
]

# Create your views here.

def main(request):
    context = {
        'tests': tests
    }
    return render(request, 'evaluation/main.html', context)

