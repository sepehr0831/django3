from django.shortcuts import render  , get_object_or_404 , redirect
from django.urls import reverse_lazy
from django.views.generic import ListView , DetailView , CreateView , UpdateView , DeleteView
from .models import Post , Category , Comment
from .forms import PostForm , EditCommentForm
from django.http import HttpResponseRedirect
# for delete a post
from django.urls import reverse_lazy , reverse

# Create your views here.


#def home(request):
 #   return render(request, "home.html",{})





class HomeView(ListView):
    model = Post
    template_name = "home.html"
    ordering =[ "-post_date" ]


    # for categry menu
    def get_context_data(self,*args,**kwargs):
        cat_menu =Category.objects.all()
        context =super(HomeView, self).get_context_data(*args,**kwargs)
        context["cat_menu"] = cat_menu
        return context


class ArticleDetailView(DetailView):
    model = Post
    form_class = PostForm
    template_name = "article_details.html"


   # for categry menu
    def get_context_data(self,*args,**kwargs):
        #for likes  
        cat_menu =Category.objects.all()
        context =super(ArticleDetailView, self).get_context_data(*args,**kwargs)

        stuff = get_object_or_404(Post, id = self.kwargs['pk'])
        total_likes = stuff.total_likes()
        #un like
        liked = False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked = True
        
        context["cat_menu"] = cat_menu
        context["total_likes"] = total_likes
        context["liked"] = liked

        return context


class AddPostView(CreateView):
    
    model = Post
    form_class = PostForm

    template_name = "add_post.html"
    #puts all fileds on page
    #fields = "__all__"
    #fields = ("title","body")

       # for categry menu
    def get_context_data(self,*args,**kwargs):
        cat_menu =Category.objects.all()
        context =super(AddPostView, self).get_context_data(*args,**kwargs)
        context["cat_menu"] = cat_menu
        return context

class UpdateView(UpdateView):
    model = Post
    form_class = PostForm

    template_name = "update_post.html"



       # for categry menu
    def get_context_data(self,*args,**kwargs):
        cat_menu =Category.objects.all()
        context =super(UpdateView, self).get_context_data(*args,**kwargs)
        context["cat_menu"] = cat_menu
        return context

class DeletePostView(DeleteView):
    model = Post
    template_name = "delete_post.html"
    success_url =reverse_lazy("home")


       # for categry menu
    def get_context_data(self,*args,**kwargs):
        cat_menu =Category.objects.all()
        context =super(DeletePostView, self).get_context_data(*args,**kwargs)
        context["cat_menu"] = cat_menu
        return context


class AddCategoryView(CreateView):
    
    model = Category

    template_name = "add_category.html"
    fields = "__all__"



       # for categry menu
    def get_context_data(self,*args,**kwargs):
        cat_menu =Category.objects.all()
        context =super(AddCategoryView, self).get_context_data(*args,**kwargs)
        context["cat_menu"] = cat_menu
        return context


def Categoryview(request, cats):
    posts = Post.objects.filter(category = cats)
    return render(request,"categories.html",{"posts":posts})


def Authorview(request, username):
    posts = Post.objects.filter(author__username = username)
    return render(request,"authors.html",{"posts":posts})



def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get("post_id"))

    liked = False

    if post.likes.filter(id= request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True


    return HttpResponseRedirect(reverse("article-detail", args=[str(pk)]))



class AddCommentView(CreateView):

    form_class = EditCommentForm
    
    model = Comment

    template_name = "add_comment.html"

    success_url = reverse_lazy("home")


    def form_valid(self, form):
        form.instance.post_id = self.kwargs["pk"]
        return super().form_valid(form)

    #puts all fileds on page
    #fields = ("title","body")


    


    


    




