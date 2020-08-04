from django.contrib.auth.models import User
from django.contrib.messages.views import SuccessMessageMixin
from django.http import StreamingHttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template.loader import render_to_string
from django.urls import reverse_lazy, reverse
from django.views.decorators.cache import never_cache
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from rest_framework.viewsets import ModelViewSet
from .serializers import RubricSerializer
from .forms import BbForm, RegisterForm
from .models import Bb, Rubric


def redirect(request):
    return HttpResponseRedirect(reverse('index'))


def index(request):
    bbs = Bb.objects.all()
    rubrics = Rubric.objects.all()
    context = {'bbs': bbs, 'rubrics': rubrics}
    return render(request, "main/index.html", context)


# def by_rubric(request, rubric_id):
#     bbs = Bb.objects.filter(rubric=rubric_id)
#     rubrics = Rubric.objects.all()
#     current_rubric = Rubric.objects.get(pk=rubric_id)
#     context = {'bbs': bbs, 'rubrics': rubrics, 'current_rubric': current_rubric}
#     return StreamingHttpResponse(render_to_string("main/by_rubric.html", context, request))


def detail_view(request, pk):
    bb = Bb.objects.get(pk=pk)
    context = {'bb': bb}
    return StreamingHttpResponse(render_to_string("main/bb_detail.html", context, request))


def by_detail(request, pk):
    bb = Bb.objects.filter(pk=pk)
    context = {'bb': bb}
    return StreamingHttpResponse(render_to_string('main/bb_detail.html', context, request))


def redirect_auth_user(request):
    return HttpResponseRedirect(reverse(index))


class BbCreateView(SuccessMessageMixin, CreateView):
    template_name = 'main/create.html'
    form_class = BbForm
    success_url = reverse_lazy('index')
    success_message = 'Объявление о продаже товара "%(title)s" создано.'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = Rubric.objects.all()
        return context


class BbDetailView(DetailView):
    model = Bb

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['rubrics'] = Rubric.objects.all()
        return context


class BbEditView(UpdateView):
    model = Bb
    form_class = BbForm
    success_url = reverse_lazy('index')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['rubrics'] = Rubric.objects.all()
        return context


class BbDeleteView(DeleteView):
    model = Bb
    form_class = BbForm
    success_url = "/"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['rubrics'] = Rubric.objects.all()
        return context


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(username=form.cleaned_data['username'],
                                            password=form.cleaned_data['password'],
                                            email=form.cleaned_data['email'])
            user.save()
            return HttpResponseRedirect(reverse(index))
        else:
            context = {'form': form}
            return render(request, 'main/register_form.html', context)
    else:
        form = RegisterForm()
        context = {'form': form}
        return render(request, 'main/registration/register_form.html', context)


class RubricModelViewSet(ModelViewSet):
    queryset = Rubric.objects.all()
    serializer_class = RubricSerializer
