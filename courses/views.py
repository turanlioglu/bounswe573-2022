from django.shortcuts import render
import datetime
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse
from django.contrib import messages
from django.views import generic
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from users.models import User
from courses.models import Course, Enrollment
from blog.models import Post
from assignments.models import Assignment
from resources.models import Resource
from django.db.models import Q

# Create your views here.

@login_required
def searchCourse(request):
    context = {}
    courses = Course.objects.all()
    if request.method == "GET":
        blog_query = request.GET.get("search_course")
        queryset = courses.filter(Q(course_name__icontains = blog_query))
        context.update({
            'blog_query': blog_query,
            'courses': queryset,
        })
        return render(request, "courses/search_course.html", context)

class CreateCourse(LoginRequiredMixin, generic.CreateView):
    fields = ('course_name', 'course_description')
    model = Course
 
    def get(self, request,*args, **kwargs): 
        self.object = None 
        context_dict = self.get_context_data() 
        context_dict.update(user = self.request.user) 
        return self.render_to_response(context_dict)
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateCourse, self).form_valid(form)
    
    
class CourseDetail(generic.DetailView):
    model = Course

    def get_context_data(self,**kwargs):
        assignments = Assignment.objects.filter(course=self.kwargs['pk'])
        resources = Resource.objects.filter(course=self.kwargs['pk'])
        posts = Post.objects.filter(course = self.kwargs['pk'])
        context = super(CourseDetail, self).get_context_data(**kwargs)
        context['assignments'] = assignments
        context['resources'] = resources
        context['posts'] = posts
        return context

class ListCourse(generic.ListView):
    model = Course
    paginate_by = 3

class EnrollCourse(LoginRequiredMixin, generic.RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        return reverse('courses:detail', kwargs={'pk':self.kwargs.get('pk')})
    
    def get(self, *args, **kwargs):
        course = get_object_or_404(Course, pk=self.kwargs.get('pk'))

        try:
            Enrollment.objects.create(student=self.request.user, course=course)
        except:
            messages.warning(self.request, 'You are already enrolled in the course.')
        else:
            messages.success(self.request, 'You are now enrolled in the course.')
        return super().get(self.request, *args, **kwargs)

class UnenrollCourse(LoginRequiredMixin, generic.RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        return reverse('courses:detail', kwargs={'pk':self.kwargs.get('pk')})

    def get(self, *args, **kwargs):

        try:
            enrollment = Enrollment.objects.filter(
                student=self.request.user,
                course__pk=self.kwargs.get('pk')
            ).get()
        except Enrollment.DoesNotExist:
            messages.warning(self.request, 'You are not enrolled in this course.')
        else:
            enrollment.delete()
            messages.success(self.request, 'You have unenrolled from the course.')
        return super().get(self.request, *args, **kwargs)