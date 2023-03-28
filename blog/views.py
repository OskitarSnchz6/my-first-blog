from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm
from rest_framework import generics
from .serializers import PostSerializer
import xlsxwriter
from django.http import HttpResponse

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

def export_posts_to_excel(request):
    # Obtener todos los posts
    posts = Post.objects.all()

    # Crear un archivo Excel y una hoja
    workbook = xlsxwriter.Workbook('posts.xlsx')
    worksheet = workbook.add_worksheet()

    # Escribir los encabezados de las columnas
    headers = ['Title', 'Text', 'Created date', 'Published date', 'Author']
    for i, header in enumerate(headers):
        worksheet.write(0, i, header)

    # Escribir los datos de los posts
    for i, post in enumerate(posts):
        worksheet.write(i+1, 0, post.title)
        worksheet.write(i+1, 1, post.text)
        worksheet.write(i+1, 2, post.created_date.strftime("%d/%m/%Y %H:%M:%S"))
        if post.published_date is not None:
            published_date_str = post.published_date.strftime("%d/%m/%Y %H:%M:%S")
        else:
            published_date_str = ""
        worksheet.write(i+1, 3, published_date_str)

        worksheet.write(i+1, 4, post.author.username)

    # Cerrar el archivo
    workbook.close()

    return HttpResponse('Exported to Excel') # retorna una respuesta al navegador

class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class NewPost(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class EditPost(generics.UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer