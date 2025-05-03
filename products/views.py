from django.shortcuts import render
from .models import Product, Category, Tag

def product_list(request):
    query = request.GET.get('q', '')  #to search in descriptions
    category_id = request.GET.get('category', '')  # select category
    tags = request.GET.getlist('tags', [])  #get list of tags selected
    
    #getting all products
    products = Product.objects.all()

    #filter by description
    if query:
        products = products.filter(description__icontains=query)  

    #filter by category and show if category was choseen
    if category_id:
        products = products.filter(category__id=category_id)  

    #filter by tags if any tag was selected 
    if tags:
        products = products.filter(tags__id__in=tags).distinct()  
        
    
        
    #fetch all categories/tags to show in frontend
    categories = Category.objects.all()
    tags_all = Tag.objects.all()

    #passing the filtered products and filters
    return render(request, 'products/product_list.html', {
        'products': products,  
        'categories': categories,  
        'tags': tags_all,  
        'query': query, 
        'selected_category': category_id,   #selected categories to highlight them
        'selected_tags': tags,  #selected tags to highlight them 
    })
    

