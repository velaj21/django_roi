from typing import Any, Iterable
from django.db import models
from django.core.validators import MaxLengthValidator

# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    # paga = models.DecimalField(max_digits=10, decimal_places=2) # 10.01
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    
    def __str__(self):
        return self.name + " - " + self.email


    def save(self, force_insert: bool = ..., force_update: bool = ..., using: str | None = ..., update_fields: Iterable[str] | None = ...) -> None:
        return super().save(force_insert, force_update, using, update_fields)


class Currency(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=3, validators=[MaxLengthValidator(3)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    country = models.ManyToManyField('Country', related_name='countries')
    

    def __str__(self):
        return self.name + " - " + self.code

    class Meta:
        verbose_name_plural = "Currencies"
        unique_together = ['name', 'code']


class Country(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=3, validators=[MaxLengthValidator(3)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    continent = models.CharField(max_length=100, default='Africa')

    def __str__(self):
        return self.name + " - " + self.code
    
    class Meta:
        verbose_name_plural = "Countries"
        unique_together = ['name', 'code']



class HistoricRating(models.Model):
    base_currency = models.ForeignKey(Currency, on_delete=models.PROTECT, related_name='historic_base_currency')
    to_currency = models.ForeignKey(Currency, on_delete=models.PROTECT, related_name='historic_to_currency')
    rate = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.base_currency.name + " - " + self.to_currency.name

    class Meta:
        unique_together = ['base_currency', 'to_currency']


class Rating(models.Model):
    base_currency = models.ForeignKey(Currency, on_delete=models.PROTECT, related_name='base_currency')
    to_currency = models.ForeignKey(Currency, on_delete=models.PROTECT, related_name='to_currency')
    rate = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.base_currency.name + " - " + self.to_currency.name
    
    def save_base(self, raw: bool = ..., force_insert: bool = ..., force_update: bool = ..., using: str | None = ..., update_fields: Iterable[str] | None = ...) -> Any:
        HistoricRating.objects.create(
            base_currency=self.base_currency,
            to_currency=self.to_currency,
            rate=self.rate
        )
        return super().save_base(raw, force_insert, force_update, using, update_fields)

    class Meta:
        unique_together = ['base_currency', 'to_currency']

class Transaction(models.Model):
    # person = models.ForeignKey(Person, on_delete=models.PROTECT)
    rating = models.ForeignKey(Rating, on_delete=models.PROTECT)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.amount) + " - " + self.rating.base_currency.name + " - " + self.rating.to_currency.name 
