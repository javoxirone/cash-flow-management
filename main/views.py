from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib import messages
from .models import CashFlow, Status, Type, Category, Subcategory
from .forms import (
    CashFlowForm, StatusForm, TypeForm, CategoryForm, SubcategoryForm, CashFlowFilterForm
)


def index(request):
    """Отображает список записей о движении денежных средств, с возможностью фильтрации по дате, статусу, типу, категории и подкатегории."""

    cash_flows = CashFlow.objects.all().order_by('-date')

    filter_form = CashFlowFilterForm(request.GET)

    if filter_form.is_valid():
        if filter_form.cleaned_data['start_date']:
            cash_flows = cash_flows.filter(date__gte=filter_form.cleaned_data['start_date'])
        if filter_form.cleaned_data['end_date']:
            cash_flows = cash_flows.filter(date__lte=filter_form.cleaned_data['end_date'])
        if filter_form.cleaned_data['status']:
            cash_flows = cash_flows.filter(status=filter_form.cleaned_data['status'])
        if filter_form.cleaned_data['type']:
            cash_flows = cash_flows.filter(type=filter_form.cleaned_data['type'])
        if filter_form.cleaned_data['category']:
            cash_flows = cash_flows.filter(category=filter_form.cleaned_data['category'])
        if filter_form.cleaned_data['subcategory']:
            cash_flows = cash_flows.filter(subcategory=filter_form.cleaned_data['subcategory'])

    return render(request, 'main/cash_flow_list.html', {
        'cash_flows': cash_flows,
        'filter_form': filter_form
    })


def cash_flow_create(request):
    """Обрабатывает создание новой записи о движении денежных средств через форму."""

    if request.method == 'POST':
        form = CashFlowForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Запись о движении денежных средств успешно создана.')
            return redirect('main:index')
    else:
        form = CashFlowForm()

    return render(request, 'main/cash_flow_form.html', {
        'form': form,
        'title': 'Создать запись о движении денежных средств'
    })


def cash_flow_update(request, pk):
    """Обрабатывает обновление существующей записи о движении денежных средств."""

    cash_flow = get_object_or_404(CashFlow, pk=pk)

    if request.method == 'POST':
        form = CashFlowForm(request.POST, instance=cash_flow)
        if form.is_valid():
            form.save()
            messages.success(request, 'Запись о движении денежных средств успешно обновлена.')
            return redirect('main:index')
    else:
        form = CashFlowForm(instance=cash_flow)

    return render(request, 'main/cash_flow_form.html', {
        'form': form,
        'title': 'Редактировать запись о движении денежных средств'
    })


def cash_flow_delete(request, pk):
    """Обрабатывает удаление записи о движении денежных средств после подтверждения пользователя."""

    cash_flow = get_object_or_404(CashFlow, pk=pk)

    if request.method == 'POST':
        cash_flow.delete()
        messages.success(request, 'Запись о движении денежных средств успешно удалена.')
        return redirect('main:index')

    return render(request, 'main/cash_flow_confirm_delete.html', {
        'cash_flow': cash_flow
    })


def dictionary_list(request):
    """Отображает все словарные сущности: статусы, типы, категории и подкатегории."""

    statuses = Status.objects.all()
    types = Type.objects.all()
    categories = Category.objects.all()
    subcategories = Subcategory.objects.all()

    return render(request, 'main/dictionary_list.html', {
        'statuses': statuses,
        'types': types,
        'categories': categories,
        'subcategories': subcategories
    })


def status_create(request):
    """Обрабатывает создание новой записи словаря "Статус"."""

    if request.method == 'POST':
        form = StatusForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Статус успешно создан.')
            return redirect('main:dictionary_list')
    else:
        form = StatusForm()

    return render(request, 'main/dictionary_form.html', {
        'form': form,
        'title': 'Создать статус'
    })


def status_update(request, pk):
    """Обрабатывает обновление записи словаря "Статус"."""

    status = get_object_or_404(Status, pk=pk)

    if request.method == 'POST':
        form = StatusForm(request.POST, instance=status)
        if form.is_valid():
            form.save()
            messages.success(request, 'Статус успешно обновлен.')
            return redirect('main:dictionary_list')
    else:
        form = StatusForm(instance=status)

    return render(request, 'main/dictionary_form.html', {
        'form': form,
        'title': 'Редактировать статус'
    })


def status_delete(request, pk):
    """Обрабатывает удаление записи словаря "Статус", отображая ошибки, если удаление невозможно из-за ограничений."""

    status = get_object_or_404(Status, pk=pk)

    if request.method == 'POST':
        try:
            status.delete()
            messages.success(request, 'Статус успешно удален.')
        except Exception as e:
            messages.error(request, f'Невозможно удалить статус:{str(e)}')
        return redirect('main:dictionary_list')

    return render(request, 'main/dictionary_confirm_delete.html', {
        'object': status,
        'title': 'Удалить статус'
    })


def type_create(request):
    """Обрабатывает создание новой записи словаря "Тип"."""

    if request.method == 'POST':
        form = TypeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Тип успешно создан.')
            return redirect('main:dictionary_list')
    else:
        form = TypeForm()

    return render(request, 'main/dictionary_form.html', {
        'form': form,
        'title': 'Создать тип'
    })


def type_update(request, pk):
    """Обрабатывает обновление записи словаря "Тип"."""

    type_obj = get_object_or_404(Type, pk=pk)

    if request.method == 'POST':
        form = TypeForm(request.POST, instance=type_obj)
        if form.is_valid():
            form.save()
            messages.success(request, 'Тип успешно обновлен.')
            return redirect('main:dictionary_list')
    else:
        form = TypeForm(instance=type_obj)

    return render(request, 'main/dictionary_form.html', {
        'form': form,
        'title': 'Редактировать тип'
    })


def type_delete(request, pk):
    """Обрабатывает удаление записи словаря "Тип", отображая ошибки, если удаление невозможно."""

    type_obj = get_object_or_404(Type, pk=pk)

    if request.method == 'POST':
        try:
            type_obj.delete()
            messages.success(request, 'Тип успешно удален.')
        except Exception as e:
            messages.error(request, f'Невозможно удалить тип: {str(e)}')
        return redirect('main:dictionary_list')

    return render(request, 'main/dictionary_confirm_delete.html', {
        'object': type_obj,
        'title': 'Удалить тип'
    })


def category_create(request):
    """Обрабатывает создание новой записи словаря "Категория"."""

    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Категория успешно создана.')
            return redirect('main:dictionary_list')
    else:
        form = CategoryForm()

    return render(request, 'main/dictionary_form.html', {
        'form': form,
        'title': 'Создать категорию'
    })


def category_update(request, pk):
    """Обрабатывает обновление записи словаря "Категория"."""

    category = get_object_or_404(Category, pk=pk)

    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            messages.success(request, 'Категория успешно обновлена.')
            return redirect('main:dictionary_list')
    else:
        form = CategoryForm(instance=category)

    return render(request, 'main/dictionary_form.html', {
        'form': form,
        'title': 'Редактировать категорию'
    })


def category_delete(request, pk):
    """Обрабатывает удаление записи словаря "Категория", отображая ошибки, если удаление невозможно."""

    category = get_object_or_404(Category, pk=pk)

    if request.method == 'POST':
        try:
            category.delete()
            messages.success(request, 'Категория успешно удалена.')
        except Exception as e:
            messages.error(request, f'Невозможно удалить категорию: {str(e)}')
        return redirect('main:dictionary_list')

    return render(request, 'main/dictionary_confirm_delete.html', {
        'object': category,
        'title': 'Удалить категорию'
    })


def subcategory_create(request):
    """Обрабатывает создание новой записи словаря "Подкатегория"."""

    if request.method == 'POST':
        form = SubcategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Подкатегория успешно создана.')
            return redirect('main:dictionary_list')
    else:
        form = SubcategoryForm()

    return render(request, 'main/dictionary_form.html', {
        'form': form,
        'title': 'Создать подкатегорию'
    })


def subcategory_update(request, pk):
    """Обновляет существующую подкатегорию."""

    subcategory = get_object_or_404(Subcategory, pk=pk)

    if request.method == 'POST':
        form = SubcategoryForm(request.POST, instance=subcategory)
        if form.is_valid():
            form.save()
            messages.success(request, 'Подкатегория успешно обновлена.')
            return redirect('main:dictionary_list')
    else:
        form = SubcategoryForm(instance=subcategory)

    return render(request, 'main/dictionary_form.html', {
        'form': form,
        'title': 'Редактировать подкатегорию'
    })


def subcategory_delete(request, pk):
    """Удаляет подкатегорию."""

    subcategory = get_object_or_404(Subcategory, pk=pk)

    if request.method == 'POST':
        try:
            subcategory.delete()
            messages.success(request, 'Подкатегория успешно удалена.')
        except Exception as e:
            messages.error(request, f'Невозможно удалить подкатегорию: {str(e)}')
        return redirect('main:dictionary_list')

    return render(request, 'main/dictionary_confirm_delete.html', {
        'object': subcategory,
        'title': 'Удалить подкатегорию'
    })


# AJAX views for dynamic forms
def get_categories_by_type(request):
    """
    Возвращает список категорий по заданному типу (type_id).
    Используется для динамического обновления формы через AJAX.
    """

    type_id = request.GET.get('type_id')
    categories = Category.objects.filter(type_id=type_id).values('id', 'name')
    return JsonResponse(list(categories), safe=False)


def get_subcategories_by_category(request):
    """
    Возвращает список подкатегорий по заданной категории (category_id).
    Используется для динамического обновления формы через AJAX.
    """

    category_id = request.GET.get('category_id')
    subcategories = Subcategory.objects.filter(category_id=category_id).values('id', 'name')
    return JsonResponse(list(subcategories), safe=False)