from django.contrib import admin
from django.db.models import Sum
from .models import Status, Type, Category, Subcategory, CashFlow


class SubcategoryInline(admin.TabularInline):
    model = Subcategory
    extra = 1


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'type')
    list_filter = ('type',)
    search_fields = ('name',)
    inlines = [SubcategoryInline]


class CategoryInline(admin.TabularInline):
    model = Category
    extra = 1
    show_change_link = True


class TypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    inlines = [CategoryInline]


class StatusAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')
    list_filter = ('category', 'category__type')
    search_fields = ('name', 'category__name')


class CashFlowAdmin(admin.ModelAdmin):
    list_display = ('date', 'status', 'type', 'category', 'subcategory', 'amount', 'comment')
    list_filter = ('date', 'status', 'type', 'category')
    search_fields = ('comment', 'category__name', 'subcategory__name')
    date_hierarchy = 'date'
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('Основная информация', {
            'fields': ('date', 'status', 'amount', 'comment')
        }),
        ('Категоризация', {
            'fields': ('type', 'category', 'subcategory')
        }),
        ('Служебная информация', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

    def get_queryset(self, request):
        return super().get_queryset(request).select_related('status', 'type', 'category', 'subcategory')

    def changelist_view(self, request, extra_context=None):
        response = super().changelist_view(request, extra_context)

        try:
            cl = response.context_data['cl']
            queryset = cl.get_queryset(request)

            total_amount = queryset.aggregate(total=Sum('amount'))['total'] or 0

            if extra_context is None:
                extra_context = {}

            extra_context['total_amount'] = total_amount
            response.context_data.update(extra_context)
        except (AttributeError, KeyError):
            pass

        return response


admin.site.register(Category, CategoryAdmin)
admin.site.register(Type, TypeAdmin)
admin.site.register(Status, StatusAdmin)
admin.site.register(Subcategory, SubcategoryAdmin)
admin.site.register(CashFlow, CashFlowAdmin)