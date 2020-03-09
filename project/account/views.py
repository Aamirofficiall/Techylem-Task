from django.shortcuts import render,redirect,HttpResponseRedirect,HttpResponse
from .forms import UserRegistration,UserProfileForm
from django.contrib.auth import login as auth_login,authenticate
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import LoginForm,CreatePost
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from .models import Profile,Post
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
  model=Post  
  template_name='post_form.html'
  fields=['title','content']

  def form_valid(self,form): 
    id=User(self.request.user.id)
    form.instance.author=id
    return super().form_valid(form)
  def  test_func(self):
     post=self.get_object()
     if self.request.user==post.author:
       return True
     return False

class PostDetailView(DetailView):
  template_name='post_detail.html'
  model=Post  


class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
  model=Post
  template_name='post_confirm_delete.html'
  success_url='/'

  def  test_func(self):
     post=self.get_object()
     if self.request.user==post.author:
       return True
     return False


@login_required
def home(request):
    # is_ceo=False
    
    # obj=User.objects.filter(profile__rank='ceo').count()
    # obj1=User.objects.filter(profile__rank='cto').count()
    # if obj==1:
    #     posts=Post.objects.all()
    #     is_ceo==True
    # if obj1==1:
    #     user=User.objects.filter(Q(profile__rank='cto')|Q(profile__rank='hr'))
    #     id=[p.id for p in user]
    #     post=Post.objects.filter(author__in=id)
    #     posts=Post(post)
    
    #     # if rank=='cto':
    # #     # user=Profile.objects.filter(Q(rank='cto'))
    # #     # id=[p.id for p in user]
    # #     # posts=Post.objects.filter(author__in=id)
    # #     posts=Post.objects.filter(Profile__rank=='cto')
    is_ceo=False
    is_cto=False
    is_hr=False
    is_sd=False
    is_jd=False
    posts=Post.objects.all()
    if (User.objects.filter(Q(profile__rank='ceo') & Q(profile__user=request.user.id)).count())==1 :
        is_ceo=True        
    if (User.objects.filter(Q(profile__rank='cto') & Q(profile__user=request.user.id)).count())==1 :
        is_cto=True        
    if (User.objects.filter(Q(profile__rank='hr') & Q(profile__user=request.user.id)).count())==1 :
        is_hr=True        
    if (User.objects.filter(Q(profile__rank='sd') & Q(profile__user=request.user.id)).count())==1 :
        is_sd=True        
    if (User.objects.filter(Q(profile__rank='jd') & Q(profile__user=request.user.id)).count())==1 :
        is_jd=True        
    role={'posts':posts,'ceo':is_ceo,'cto':is_cto,'hr':is_hr,'sd':is_sd,'jd':is_jd}
    return render(request,'home.html',role)

def login(request):

   
   form=LoginForm(request.POST or None)
   if request.method=="POST":
    if form.is_valid():   
     
     username=form.cleaned_data.get('username')
     password=form.cleaned_data.get('password')
     u=authenticate(username=username,password=password)
   
     if u is not None:
      rank=Profile.objects.filter(user=u.id)
      rank="".join([p.rank for p in rank])
      auth_login(request,u)
      return redirect('home',)
     else:
       messages.success(request,"username or email is invalid..!")
       return redirect('login')
   return render(request,'login.html',{'form':form}) 
    

def register(request):

    if request.method=="POST":
       form=UserRegistration(request.POST)
       profile_form=UserProfileForm(request.POST)
       if form.is_valid() and profile_form.is_valid():
           
           user=form.save()
           profile=profile_form.save(commit=False)
           profile.user=user
           profile=profile_form.save()
           profile.save()
           messages.success(request,'User created Successfully Login Here....!')
           return redirect('login')
       else:
           messages.success(request,' Invalid Cradentials....!')
    form=UserRegistration(request.POST)
    profile_form=UserProfileForm()
    return render(request,'registration.html',{'form':form,'profile_form':profile_form})



class PostCreateView(LoginRequiredMixin,CreateView):
  model=Post  
  template_name='post_form.html'
  fields=['title','content']
  def form_valid(self,form): 
    id=User(self.request.user.id)
    form.instance.author=id
    return super().form_valid(form)





# def createPost(request,id):
    

