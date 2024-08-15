from django.shortcuts import render

# Create your views here.
# views.py
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Card
import json



@csrf_exempt
def delete_card(request, card_id):
    if request.method == 'POST':
        try:
            card = Card.objects.get(id=card_id)
            card.delete()
            return JsonResponse({'success': True})
        except Card.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Card not found'})
    return JsonResponse({'success': False, 'error': 'Invalid request method'})










# views.py
from django.shortcuts import render
from .models import Card

def card_history(request):
    title_filter = request.GET.get('title', '')
    if title_filter:
        cards = Card.objects.filter(title__icontains=title_filter).order_by('-date_updated')
    else:
        cards = Card.objects.all().order_by('-date_updated')
    
    return render(request, 'card_history.html', {'cards': cards, 'title_filter': title_filter})


# views.py
from django.http import JsonResponse
from .models import Card

def get_cards(request):
    cards = Card.objects.all().values('id', 'title', 'subheading_1', 'subheading_2')
    return JsonResponse(list(cards), safe=False)





# views.py
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Card
import json

# views.py
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Card
import json

@csrf_exempt
def save_card(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            card_id = data.get('cardId')
            title = data.get('title')
            subheading_1 = data.get('subheading_1')
            subheading_2 = data.get('subheading_2')

            if card_id and card_id.isdigit():
                card = Card.objects.filter(id=int(card_id)).first()
                if card:
                    card.title = title
                    card.subheading_1 = subheading_1
                    card.subheading_2 = subheading_2
                    card.save()
                    return JsonResponse({'status': 'success'})
                else:
                    return JsonResponse({'status': 'error', 'message': 'Card not found'}, status=404)
            else:
                # Create new card if no valid cardId is provided
                card = Card.objects.create(
                    title=title,
                    subheading_1=subheading_1,
                    subheading_2=subheading_2
                )
                return JsonResponse({'status': 'success', 'card_id': card.id})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=400)














# @csrf_exempt
# def save_card(request):
#     if request.method == 'POST':
#         data = json.loads(request.body)
#         title = data.get('title')
#         subheading_1 = data.get('subheading_1')
#         subheading_2 = data.get('subheading_2')

#         # Check if card already exists by title, otherwise create a new one
#         card, created = Card.objects.update_or_create(
#             title=title,
#             defaults={'subheading_1': subheading_1, 'subheading_2': subheading_2}
#         )

#         return JsonResponse({'status': 'success', 'card_id': card.id})
#     return JsonResponse({'status': 'error'}, status=400)




def card_manager(request):

    return render(request, 'card_manager.html')


def card_manager(request):
    cards = Card.objects.all()  # Fetch all card instances from the database
    return render(request, 'card_manager.html', {'cards': cards})