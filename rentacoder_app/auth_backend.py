from django.contrib.auth.backends import ModelBackend


class UserModelBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        user = super().authenticate(request, username, password, **kwargs)
        return user if user and not user.deleted else None


def processor(request):
    if request.user.is_authenticated():
        return {
            'authenticated': True,
            'username': request.user.username,
            'email': request.user.email,
        }
    else:
        return {
            'authenticated': False
        }
