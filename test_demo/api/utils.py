from django.http import JsonResponse

def handler(exc, context=None):
    if exc.default_code == 'authentication_failed' or exc.default_code == 'not_authenticated':
        return JsonResponse({'error': {'code': 403, 'message': 'Login failed'}})
    elif exc.default_code == 'permission_denied':
        return JsonResponse({'error': {'code': 403, 'message': 'Forbidden for you'}})
