from django.db import models




class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)  #category name
    
    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)  
    
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200)  
    description = models.TextField()  
    category = models.ForeignKey(Category, related_name="products", on_delete=models.CASCADE)  
    tags = models.ManyToManyField(Tag, related_name="products")  #many-to-many
    
    def __str__(self):
        return self.name

    def short_description(self):
        """Returns short version"""
        if len(self.description) > 100:
            return self.description[:100] + "..."
        else:
            return self.description
