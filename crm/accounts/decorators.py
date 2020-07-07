from django.http import HttpResponse
from django.shortcuts import redirect 

def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        #to avoid logged in users from viewing the login page
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func

#this have extra layer just to be able to pass a parameter (allowed_roles)
def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):

            group = None
            #to check if user is part of a group
            if request.user.groups.exists():
                #get the first group of the group list
                group = request.user.groups.all()[0].name
            
            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse('You are not authorized to view this page')
        return wrapper_func
    return decorator

#this to decorate home page,becuase login directs to it,
#before home page gets rendered we checl if user is admin then
#he can gain access for it, else (means he is customer) he will
#get directed to the user-page
def admin_only(view_func):
    def wrapper_function(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name

        if group == 'customer':
            return redirect('user-page')

        if group == 'admin':
            return view_func(request, *args, **kwargs)
    
    return wrapper_function

