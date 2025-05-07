from django.urls import path
from .views import (index,
                    cash_flow_create,
                    cash_flow_update,
                    cash_flow_delete,
                    dictionary_list,
                    status_create,
                    status_update,
                    status_delete,
                    type_create,
                    type_update,
                    type_delete,
                    category_create,
                    category_update,
                    category_delete,
                    subcategory_create,
                    subcategory_update,
                    subcategory_delete,
                    get_categories_by_type,
                    get_subcategories_by_category)

urlpatterns = [
    # Cash Flow CRUD
    path('', index, name='index'),
    path('cash-flow/create/', cash_flow_create, name='cash_flow_create'),
    path('cash-flow/<int:pk>/update/', cash_flow_update, name='cash_flow_update'),
    path('cash-flow/<int:pk>/delete/', cash_flow_delete, name='cash_flow_delete'),

    # Dictionary management
    path('dictionaries/', dictionary_list, name='dictionary_list'),

    # Status CRUD
    path('dictionaries/status/create/', status_create, name='status_create'),
    path('dictionaries/status/<int:pk>/update/', status_update, name='status_update'),
    path('dictionaries/status/<int:pk>/delete/', status_delete, name='status_delete'),

    # Type CRUD
    path('dictionaries/type/create/', type_create, name='type_create'),
    path('dictionaries/type/<int:pk>/update/', type_update, name='type_update'),
    path('dictionaries/type/<int:pk>/delete/', type_delete, name='type_delete'),

    # Category CRUD
    path('dictionaries/category/create/', category_create, name='category_create'),
    path('dictionaries/category/<int:pk>/update/', category_update, name='category_update'),
    path('dictionaries/category/<int:pk>/delete/', category_delete, name='category_delete'),

    # Subcategory CRUD
    path('dictionaries/subcategory/create/', subcategory_create, name='subcategory_create'),
    path('dictionaries/subcategory/<int:pk>/update/', subcategory_update, name='subcategory_update'),
    path('dictionaries/subcategory/<int:pk>/delete/', subcategory_delete, name='subcategory_delete'),

    # AJAX URLs
    path('ajax/get-categories-by-type/', get_categories_by_type, name='get_categories_by_type'),
    path('ajax/get-subcategories-by-category/', get_subcategories_by_category,
         name='get_subcategories_by_category'),
]
