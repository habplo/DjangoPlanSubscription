from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, DeleteView
from plans.models import UserPlan
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND, HTTP_200_OK
from rest_framework.authtoken.models import Token
from django.shortcuts import render
from .forms import NotesForm
from .models import notes, custnote
from .serializers import NoteSerializer
from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
from django.contrib.auth import login as auth_login
from django.urls import reverse
from .decorators import subscription_plan_permission

# get all notes api
@api_view(['GET'])
def getAllNotes(request):
    if request.method == 'GET':
        notes_dt = notes.objects.filter(is_active=1)
        serializer = NoteSerializer(notes_dt, many=True)
        return Response(serializer.data)

# rest-framework default authToken login api
@csrf_exempt
@api_view(['POST'])
@permission_classes((AllowAny,))
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'}, status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'}, status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key},
                    status=HTTP_200_OK)


# Knox-jwt login api
class LoginView(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        auth_login(request._request, user)
        return super(LoginView, self).post(request._request, format=None)


class NotesListView(ListView):
    model = notes

    def get_queryset(self):
        return super(NotesListView, self).get_queryset().all()


@subscription_plan_permission
def notesAdd(request):
    if request.POST:
        form = NotesForm(request.POST)
    else:
        form = NotesForm()
    if form.is_valid():
        notes = form.save(commit=False)
        notes.save()
        userPlan = UserPlan.objects.get(user_id=request.user.id)
        notes_dt = custnote.objects.create(User=request.user, notes=notes, Plan=userPlan)
        return HttpResponseRedirect(reverse('notes_list'))
    return render(request, 'notes/notes_form.html', {'form': form})

class NotesCreateView(CreateView):
    model = notes
    form_class = NotesForm

    def get_initial(self):
        initial = super(NotesCreateView, self).get_initial()
        initial['user'] = self.request.user
        return initial

    def get_success_url(self):
        return reverse('notes_list')

    def get_queryset(self):
        return super(NotesCreateView, self).get_queryset().filter()


class NotesDeleteView(DeleteView):
    model = notes

    def get_queryset(self):
        return super(NotesDeleteView, self).get_queryset().filter()

    def get_success_url(self):
        return reverse('notes_list')

    def delete(self, request, *args, **kwargs):
        pk = self.kwargs['pk']
        notes_dt = notes.objects.filter(id=pk)
        notes_dt.delete()
        return HttpResponseRedirect(reverse('notes_list', kwargs={'pk': pk}))
