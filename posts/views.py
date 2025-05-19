from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound,HttpResponseRedirect
from django.urls import reverse

# Create your views here.

posts = [
       {
"id":0,
"title" : 'Lets Explore Python',
"content": 'Python is a high-level interpreted programming language known for its readability and versatility. It supports multiple programming paradigms.'}, 

   
   
   
   
   
    {
"id":1,
"title" : 'Lets Explore JavaScript',
"content": 'JavaScript is a high-level interpreted programming language known for its readability and versatility. It supports multiple programming paradigms.'}, 

    {
"id": 2,
"title": "Lets Explore Django",
"content": "Django is a high-level Python web framework that simplifies the development of web applications."},

]







def home(request):
    html = ""
    for post in posts:
        html += f'''
        <div>
        
        <h1>{post['id']} - {post['title']}</h1>
        <p> {post['content']}</p>
        
        </div>'''
        
    return render(request,'posts/index.html', {'posts': posts, 'username':'Hameed'})
    
def post(request, id):
    valid_id = False
    for post in posts:
        
        if post['id'] == id:
            post_dict = post
            valid_id = True
            break
    if valid_id:
        
        return render(request, 'posts/post.html', {'post_dict': post_dict})
    else:
        return HttpResponseNotFound('Post not Available😣')
def google(request, id):
    url = reverse ('post', args=[id]) 
    return HttpResponseRedirect(url)

