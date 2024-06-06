from time import sleep
from django.contrib import admin

# Register your models here.

from .models import Person, Country, Currency, Rating, HistoricRating, Transaction

admin.site.register(Person)


# class CurrencyInline(admin.TabularInline):
#     model = Currency
#     extra = 1  # Numri i formave të reja që do të shfaqen



@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'created_at', 'updated_at', 'continent')
    search_fields = ('name', 'code')
    list_filter = ('code', 'name')
    ordering = ('code',)
    readonly_fields = ('created_at', 'updated_at', 'continent')
    list_per_page = 80
    list_editable = ('code',)

    # inlines = [
    #     CurrencyInline,
    # ]



@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    list_display = ('name', 'code',)
    search_fields = ('name', 'code')
    list_filter = ('code', 'name')
    ordering = ('code',)
    list_per_page = 80
    list_editable = ('code',)
    autocomplete_fields = ('country',)

    def computed_field(self, obj):
        sleep(5)
        # Replace this with your actual computation
        return len(obj.code) < 3
    
    computed_field.short_description = 'Computed Field'



@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('base_currency', 'to_currency', 'rate', 'inverted_rate')
    search_fields = ('base_currency',)
    ordering = ('rate',)
    list_per_page = 80
    autocomplete_fields = ('base_currency', 'to_currency')

    def inverted_rate(self, obj):
        # Replace this with your actual computation
        return 1 / obj.rate 
    
    inverted_rate.short_description = 'Inverted Rate'


@admin.register(HistoricRating)
class HistoricRatingAdmin(admin.ModelAdmin):
    list_display = ('base_currency', 'to_currency', 'rate',)
    search_fields = ('base_currency',)
    ordering = ('rate',)
    list_per_page = 80
    autocomplete_fields = ('base_currency', 'to_currency')


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('rating', 'amount', 'created_at', 'total')
    search_fields = ('rating',)
    list_per_page = 80
    autocomplete_fields = ('rating',)


    def total(self, obj):
        # Replace this with your actual computation
        return obj.amount * obj.rating.rate
    
    total.short_description = 'Inverted Rate'
