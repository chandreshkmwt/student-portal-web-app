from django.shortcuts import render, get_object_or_404, redirect
from student_marks.models import Marks
from django.views.generic import TemplateView, CreateView, DetailView, ListView
# Create your views here.

class HomePage(TemplateView):
    template_name = 'home.html'

class Success(DetailView):
    model = Marks

class EnterMarksView(CreateView):
    fields = ('rollno', 'name', 'maths', 'physics', 'chemistry',)
    redirect_field_name = 'student_marks/marks_detail.html'
    model = Marks

class MarksListView(ListView):
    model = Marks

    def get_queryset(self):
        return Marks.objects.filter().order_by('-percentage')