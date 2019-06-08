from rest_framework.views import APIView  # normal view can return a api data
from rest_framework.response import Response
from . models import Registration
from . serializers import RegistrationSerialiser
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.utils.safestring import mark_safe  # string can be display safely witht escaping in html
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
import jwt,json


def index(request):
    return render(request, 'chat/index.html', {})  # Combines a template with a context dictionary and returns an HttpResponse object


def room(request, room_name):
    return render(request, 'chat/room.html', {
        'room_name_json': mark_safe(json.dumps(room_name))  # mark_safe will explicitly mark a string as safe for (HTML) output purposes.
    })


class SignUp(generic.CreateView):
    form_class = UserCreationForm  # it will create user creation form
    success_url = reverse_lazy('login')  # to load url later when they’re available.
    template_name = 'signup.html'


class RegistrationList(APIView):

    def get(self, request):
            Registration1 = Registration.objects.all()
            serializer = RegistrationSerialiser(Registration1, many=True)
            return Response(serializer.data)

    def post(self):
        pass

    def user_login(request):
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    payload = {
                        'id': user.id,
                        'email': user.email,
                    }
                    jwt_token = {'token': jwt.encode(payload, "SECRET_KEY")}
                    print("dd", jwt_token)
                    login(request, user)
                    return HttpResponseRedirect(reverse('chat/index'))
                    decode_jwt_token
                else:
                    return HttpResponse("Your account was inactive.")

            else:
                print("Someone tried to login and failed.")
                print("They used username: {} and password: {}".format(username, password))
                return HttpResponse("Invalid login details given")
        else:
            return render(request, 'chat/login.html', {})





