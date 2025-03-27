from django.template.context_processors import request
from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import redirect

class AuthMiddleware(MiddlewareMixin):

    def process_request(self, request):
        # 设置一个白名单
        if request.path in ['/login/', '/register/', '/judge/']:
            return

        # if request.user.is_authenticated:
                # 登录成功
                # return
            # else:
                # 登录失败
                # return redirect('/login/')

        if not request.user.is_authenticated:
            return redirect('/login/')