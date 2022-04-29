from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse

def decorator_func(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(reverse('home'))
        else:
            return view_func(request, *args, **kwargs)

    return wrapper_func


def decorator(allowed_holes):
    def decorator_funcTwo(view_func):
        def wrapper(request, *args, **kwargs):

            group = request.user.groups.all()[0].name

            if group in allowed_holes:
                return view_func(request, *args, **kwargs)
            else:
                return redirect('user')

        return wrapper
    return decorator_funcTwo
