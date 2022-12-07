# Django
from django.http.request import HttpRequest
from django.shortcuts import (
    HttpResponse,
    render
)


def simple(request: HttpRequest) -> HttpResponse:
    return HttpResponse(
        '<h1>Что нибудь</h1>'
    )


def index(request: HttpRequest) -> HttpRequest:
    """index view."""

    numbers: list[int] = []
    i: int
    for i in range(1, 11):
        numbers.append(i)

    ctx_data: dict[str, str | list[int]] = {
        'ctx_title': 'Заголовок главной страницы',
        'ctx_numbers': numbers
    }
    return render(
        request,
        template_name='main/index.html',
        context=ctx_data
    )
