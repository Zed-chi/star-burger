from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import MinValueValidator


class Restaurant(models.Model):
    name = models.CharField("название", max_length=50)
    address = models.CharField("адрес", max_length=100, blank=True)
    contact_phone = models.CharField(
        "контактный телефон",
        max_length=50,
        blank=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "ресторан"
        verbose_name_plural = "рестораны"


class ProductQuerySet(models.QuerySet):
    def available(self):
        return self.distinct().filter(menu_items__availability=True)


class ProductCategory(models.Model):
    name = models.CharField("название", max_length=50)

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField("название", max_length=50)
    category = models.ForeignKey(
        ProductCategory,                
        on_delete=models.CASCADE,
        verbose_name="категория",
        related_name="products",
    )
    image = models.ImageField("картинка", null=True, blank=True)
    special_status = models.BooleanField(
        "спец.предложение",
        default=False,
        db_index=True,
    )
    description = models.TextField("описание", max_length=200, blank=True)
    price = models.DecimalField(
        "цена",
        max_digits=8,
        decimal_places=2,
        validators=[MinValueValidator(0)],
    )

    objects = ProductQuerySet.as_manager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "товар"
        verbose_name_plural = "товары"


class RestaurantMenuItem(models.Model):

    restaurant = models.ForeignKey(
        Restaurant,
        on_delete=models.CASCADE,
        related_name="menu_items",
        verbose_name="ресторан",
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="menu_items",
        verbose_name="продукт",
    )
    availability = models.BooleanField(
        "в продаже", default=True, db_index=True
    )

    def __str__(self):
        return f"{self.restaurant.name} - {self.product.name}"

    class Meta:
        verbose_name = "пункт меню ресторана"
        verbose_name_plural = "пункты меню ресторана"
        unique_together = [["restaurant", "product"]]


class OrderItem(models.Model):
    product = models.ForeignKey(
        "Product",
        on_delete=models.CASCADE,
        related_name="order_items",
    )
    quantity = models.IntegerField("количество", validators=[MinValueValidator(1),])
    order = models.ForeignKey(
        "Order",
        on_delete=models.CASCADE,
        related_name="items",
    )
    price = models.IntegerField("цена", default=0, validators=[MinValueValidator(0),])

    def __str__(self):
        return f"Заказ №{self.order.id}; {self.product.name}; В количестве {self.quantity}"

    class Meta:
        verbose_name = "Позиция заказа"
        verbose_name_plural = "Позиции заказа"


class Order(models.Model):
    STATUS_CHOICES = (
        ("Handled", "Обработано"), 
        ("Unhandled", "Необработано")
    )
    PAYMENT_CHOICES = (
        ("CASH", "Наличными"), 
        ("CARD", "Электронно")
    )
    firstname = models.CharField("имя",max_length=100)
    lastname = models.CharField("фамилия", max_length=100)
    phonenumber = PhoneNumberField(region="RU", verbose_name="номер телефона")
    address = models.CharField("адрес доставки", max_length=255,)
    status = models.CharField(
        "статус",
        choices=STATUS_CHOICES,
        default="Unhandled",
        max_length=125,
        db_index=True,
    )
    comment = models.TextField("комментарий", blank=True)
    registered_at = models.DateTimeField("зарегистрирован", default=timezone.now, db_index=True,)
    called_at = models.DateTimeField("время звонка", null=True, blank=True, db_index=True,)
    delivered_at = models.DateTimeField("доставлено", null=True, blank=True, db_index=True,)
    payment = models.CharField(
        "вид платежа",
        choices=PAYMENT_CHOICES,
        max_length=125,
        db_index=True,
    )
    restaurant = models.ForeignKey("Restaurant", related_name="orders", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.firstname} {self.lastname} -> {self.address}"

    def get_price(self):
        return self.order_items.aggregate(models.Sum("price"))["price__sum"]

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"
