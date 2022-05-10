from unicodedata import category
from django.db import models
from django.contrib.auth.models import AbstractUser
# from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.



class CustomUser(AbstractUser):
    is_lock = models.BooleanField(default=False, blank=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=11, blank=True, null=True)
    
    created_at = models.DateTimeField(auto_now=True)
    update_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = '01. Danh sách người dùng'


class Brand(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    code = models.CharField(max_length=11, blank=True, null=True)
    
    class Meta:
        verbose_name_plural = '02. Thương hiệu'

    def __str__(self):
        return self.name


class Gift(models.Model):
    name = models.CharField(max_length=255,blank=True, null=True )
    product = models.ManyToManyField(to='Product')
    class Meta:
        verbose_name_plural = '03. Quà tặng'


    def __str__(self):
        return self.name


class Percent(models.Model):
    number_percent = models.IntegerField()

    class Meta:
        verbose_name_plural = '04. Phần trăm'

    def __str__(self):
        return str(self.number_percent)


class Event(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField()
    date_start = models.DateField()
    date_stop = models.DateField()
    product = models.ManyToManyField(to='Product')

    created_at = models.DateTimeField(auto_now=True)
    update_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = '05. Sự kiện'

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    code = models.CharField(max_length=11, blank=True, null=True)
    description = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        verbose_name_plural = '06. Danh mục'
    @property
    def get_list_products(self):
        return Product.objects.filter(categories__code=self.code)


    def __str__(self):
        return self.name


class Size(models.Model):
    name = models.CharField(max_length=10)
    description = models.CharField(max_length=255, null=True, blank=True)
    class Meta:
        verbose_name_plural = '07. Kích thước'

    def __str__(self):
        return self.name


class Color(models.Model):
    name = models.CharField(max_length=25)
    description = models.CharField(max_length=255, blank=True, null=True)
    class Meta:
        verbose_name_plural = '08. Màu'

    def __str__(self):
        return self.name


class DiscountCode(models.Model):
    code = models.CharField(max_length=11, blank=False, null=False)
    description = models.CharField(max_length=1024, null=True)
    product = models.ManyToManyField(to="Product")
    created_at = models.DateTimeField(auto_now=True)
    update_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = '09. Mã giảm giá'

    def __str__(self):
        return str(self.code)


class Insurance(models.Model):
    time_insurance = models.CharField(max_length=10)
    product = models.ManyToManyField(to="Product")
    
    class Meta:
        verbose_name_plural = '10. Bảo hành'

    def __str__(self):
        return str(self.time_insurance)

class Product(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(default='')
    detail = models.TextField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, null=True)
    price = models.IntegerField(default=0)
    
    size = models.ManyToManyField(Size)
    color = models.ManyToManyField(Color)
    amount = models.IntegerField(default=0)
    time_insurance = models.DateTimeField()
    image_link = models.FileField(upload_to='image-product', null=True)
    image_detail = models.FileField(upload_to='image-detail', null=True)
    views = models.IntegerField(default=0)
    
    created_at = models.DateTimeField(auto_now=True)
    update_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = '11. Sản phẩm'


    def __str__(self):
        return str(self.name)

class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=255,blank=True, null=True )
    phone = models.CharField(max_length=11, blank=False, null=False)
    email = models.CharField(max_length=255, blank=True, null=True)
    rate = models.IntegerField(default=0,)
    comment = models.CharField(max_length=1024, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = '12. Đánh giá'

    def __str__(self):
        return self.name

class OrderItem(models.Model):
    product= models.ForeignKey(Product,on_delete=models.SET_NULL, null=True )
    order = models.ForeignKey(to='Order',on_delete=models.SET_NULL, null=True )
    quantity = models.IntegerField(default=1)

    class Meta:
        verbose_name_plural = '13. Chi tiết đơn hàng'

    def __str__(self):
        return '{} - {} - {}'.format(self.order.user, self.product, self.quantity)


class Order(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    product = models.ManyToManyField(Product,through='OrderItem')
    address_ship = models.CharField(max_length=1024)
    note = models.CharField(max_length=255, null=True, blank=True)
    code = models.ForeignKey(DiscountCode, on_delete=models.CASCADE, null=True, blank=True)
    choice_status = (
                    ('In Process','In Process'),
                    ('Shipped','Shipped'),
                    ('Delivered','Delivered')
                    )
    status = models.CharField(max_length=255, choices=choice_status, default='In Process')
    
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = '13. Đơn hàng'

    def __str__(self):
        return self.user.username
        

class Cart(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    order = models.ManyToManyField(Order)
    
    class Meta:
        verbose_name_plural = '14. Giỏ hàng'

    def __str__(self):
        return str(self.order.user)


    


    
