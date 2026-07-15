from django.db import models

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.name} - {self.subject}"

from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200, verbose_name="عنوان کتاب")
    author = models.CharField(max_length=200, verbose_name="نویسنده")
    description = models.TextField(null=True, blank=True, verbose_name="توضیحات")
    price = models.IntegerField(verbose_name="قیمت (تومان)")
    cover_image = models.ImageField(upload_to='book_covers/', null=True, blank=True, verbose_name="تصویر کاور")
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title



    class Meta:
        verbose_name = "کتاب"
        verbose_name_plural = "کتاب‌ها"

    def __str__(self):
        return self.title
