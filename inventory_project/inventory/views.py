from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test
from .forms import InventoryItemForm
from models import InventoryItem
from django.shortcuts import get_object_or_404
@user_passes_test(lambda u: u.is_superuser)
def add_inventory(request):
    if request.method == 'POST':
        form = InventoryItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inventory_list')
    else:
        form = InventoryItemForm()
    return render(request, 'inventory/add_inventory.html', {'form': form})
def inventory_detail(request, pk):
    item = get_object_or_404(InventoryItem, pk=pk)
    return render(request, 'inventory/inventory_details.html', {'item': item})
@user_passes_test(lambda u: u.is_superuser)
def delete_inventory(request, pk):
    item = get_object_or_404(InventoryItem, pk=pk)
    item.delete()
    return redirect('inventory_list')


