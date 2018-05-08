from django.shortcuts import render
from django.http import JsonResponse
from django.template import RequestContext
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_protect, csrf_exempt

@csrf_exempt
@require_http_methods(["GET", "POST"])
def get_webhook_data(request):
    print('request coming in:', request)
    # context_instance = RequestContext(request)
    data = {
        'speech': 'Who is a django expert in cyborg',
        'displayText': 'Who is a django expert in cyborg'
    }

    return JsonResponse(data)
