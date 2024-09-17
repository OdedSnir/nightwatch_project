from django.http import JsonResponse, HttpRequest
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response

@csrf_exempt
@api_view(['GET'])
def sample(request: HttpRequest) -> JsonResponse:
    message = ''
    print(request.headers)
    print(request.body)
    user = request.user
    if request.method == 'GET':
        message = f'Hello {user}'
    elif request.method == 'POST':
        message: 'Post response received!'
    data = {'message': message}
    return Response(data)


