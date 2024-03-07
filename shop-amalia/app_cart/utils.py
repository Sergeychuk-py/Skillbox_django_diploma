from django.http import HttpRequest


def is_ajax(request: HttpRequest) -> bool:
    """
    The method checks the type request на ajax
    :param request:
    :return:
    """
    return request.headers.get("x-requested-with") == "XMLHttpRequest"
