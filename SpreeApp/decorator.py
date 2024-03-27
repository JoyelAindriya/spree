from .models import user_data
from .models import Usertoken
from functools import wraps

def authuser(view_fun):
    @wraps(view_fun)
    def wrapper(request,*args,**kwargs):
        print("----------------------")
        print(request.META.get('HTTP_AUTH'))
        r=request.META.get('HTTP_AUTH')
        u=Usertoken.objects.get(token=r)
        request.u=u.user
        return view_fun(request,*args,**kwargs)

    return wrapper
