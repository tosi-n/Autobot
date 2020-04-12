from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()
# Create your models here.
# STATUS = (
#     (0,"Draft"),
#     (1,"Publish")
# )

# def post_image_path(instance, filename):
#     return "post/images/{}/{}".format(instance.title, filename)

# def category_image_path(instance, filename):
#     return "category/icons/{}/{}".format(instance.name, filename)


class Bitron(models.Model):
    eligible_text = models.TextField()
    # slug = models.SlugField(max_length=200, unique=True, default=0)
    # created_on = models.DateTimeField(auto_now_add=True)
    # modified = models.DateTimeField(auto_now=True)

    # class Meta:
    #     verbose_name_plural = "eligibles"

    def __str__(self):
        return self.eligible_text

# class Post(models.Model):
#     title = models.CharField(max_length=200, unique=True)
#     icon = models.ImageField(upload_to=post_image_path, blank=True)
#     category = models.ForeignKey(Category, related_name='product_category', on_delete=models.CASCADE)
#     slug = models.SlugField(max_length=200, unique=True)
#     author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
#     updated_on = models.DateTimeField(auto_now= True)
#     content = models.TextField()
#     created_on = models.DateTimeField(auto_now_add=True)
#     status = models.IntegerField(choices=STATUS, default=0)

#     class Meta:
#         ordering = ['-created_on']

#     def __str__(self):
#         return self.title

# class PostViews(TimeStampedModel):
#     ip = models.CharField(max_length=250)
#     product = models.ForeignKey(Post, related_name='product_views', on_delete=models.CASCADE)