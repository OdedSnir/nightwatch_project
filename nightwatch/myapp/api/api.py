from django.http import JsonResponse, HttpRequest
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def sample(request: HttpRequest) -> JsonResponse:
    message = ''
    if request.method == 'GET':
        message = 'Hello World!'
    elif request.method == 'POST':
        message: 'Post response received!'
    data = {'message': message}
    return JsonResponse(data)
