from django.shortcuts import redirect
from django.urls import reverse

# verifies if the user is authenticated; if so, redirect the user to the home;
# this decorator is used to not allow logged users to access the login page or the register page;
def decorator_func(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(reverse('home'))
        else:
            return view_func(request, *args, **kwargs)

    return wrapper_func

# verifies if the user is in the allowed groups to access the current view;
# this decorator is used to deny users to have admin privileges; 
# used also to customers see only their home page, and only admin see their home page;
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
