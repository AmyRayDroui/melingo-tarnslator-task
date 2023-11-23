from django.http import  JsonResponse
from .models import Entry

def get_word(request):
    try: 
        word = request.GET['word']
    except KeyError:
        return JsonResponse({'message': 'Invalid query'}, status=400)
    if not word:
        return JsonResponse({})
    try: 
        entry = Entry.objects.get(Entry=word)
    except Entry.DoesNotExist:
        return JsonResponse({'message': 'This word doesn\'t have a translation '}, status=404)
    
    examples = [example.Text for example in entry.examples.all()]
    return JsonResponse({
        'originalWord': word,
        'translation': entry.TranslationFull,
        'examples': examples
    })
