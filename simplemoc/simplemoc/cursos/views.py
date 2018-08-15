from django.shortcuts import render, get_object_or_404

# Create your views here.

from .models import Curso
from .forms import ContactCurso

def index(request):
    cursos = Curso.objects.all()
    template_name = 'cursos/index.html'
    context = {
        'cursos': cursos
    }
    return render(request, template_name, context)

'''def details(request, pk):
    curso = get_object_or_404(Curso, pk=pk)
    context = {
        'curso': curso
    }
    template_name = 'cursos/details.html'
    return render(request, template_name, context)'''

def details(request, slug):
    curso = get_object_or_404(Curso, slug=slug)
    context = {}
    if request.method == 'POST':
        form = ContactCurso(request.POST)
        if form.is_valid():
            context['is_valid']=True
            form = ContactCurso()
    else:
        form = ContactCurso()
    context['form']=form
    context['curso']=curso
    template_name = 'cursos/details.html'
    return render(request, template_name, context)

