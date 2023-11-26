from rest_framework.views import exception_handler,Response
from rest_framework import exceptions,status


def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)

    # Now add the HTTP status code to the response.
    if response is not None:
        response.data['status_code'] = response.status_code
    
    
    other_response = add_custom_error(exc,response)

    return other_response if other_response else response

def add_custom_error(exc,response):
    if not exc or not response:
        return
    
    elif isinstance(exc,exceptions.AuthenticationFailed):
        data = set_res_data(
            exceptions.AuthenticationFailed.status_code,
            '憑證有誤',
            'auth_fail'
        )
        return Response(data, status=exc.status_code)
    
    elif isinstance(exc,exceptions.NotAuthenticated):
        data = set_res_data(
            exceptions.NotAuthenticated.status_code,
            '未登入',
            'not_login'
        )
        return Response(data, status=exc.status_code)
    
    elif isinstance(exc,exceptions.PermissionDenied):
        data = set_res_data(
            exceptions.PermissionDenied.status_code,
            '無權限',
            'no_permission'
        )
        return Response(data, status=exc.status_code)


    return None


def set_res_data(status_code,default_detail,default_code):
    data = {
        "status_code": status_code,
        "default_detail": default_detail,
        "default_code": default_code
    }
    return data
