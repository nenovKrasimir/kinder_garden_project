from django.shortcuts import render
from core.models import ParagraphMissionOfKinderGarden, TextVisionGarden, TextValueGarden
# Create your views here.
def home(request):
    return render(request, 'home.html')


def about_us(request):
    mission_garden = ParagraphMissionOfKinderGarden.objects.all()
    vision_garden = TextVisionGarden.objects.first()
    value_garden = TextValueGarden.objects.first()
    content = {
        'paragraphs_mission_garden': mission_garden,
        'text_vision_garden': vision_garden,
        'text_value_garden': value_garden
    }
    return render(request, 'about_us.html', content)


def contacts(request):
    return render(request, 'contacts.html')
