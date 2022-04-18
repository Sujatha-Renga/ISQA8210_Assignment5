from django.contrib.auth.mixins import LoginRequiredMixin
from django import forms
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from workorder.forms import WorkOrderForm, ItemForm
# #from workorder.models import WorkOrder, WorkOrderItem
# from django.db.models import Count

# import csv
# from django.shortcuts import render
# from django.http import HttpResponse
from .models import WorkOrder, WorkOrderItem


# from django.contrib.admin.views.decorators import staff_member_required

class WorkOrderList(ListView):
    template_name = "workorder/workorder_list.html"
    model = WorkOrder

    def get_context_data(self, **kwargs):
        context = super(WorkOrderList, self).get_context_data(**kwargs)
        context["orders"] = WorkOrder.objects.all()
        return context


class CreateWorkOrder(CreateView):
    template_name = "workorder/create_workorder.html"
    model = WorkOrder
    form_class = WorkOrderForm
    success_url = reverse_lazy("workorder_list")


class UpdateWorkOrder(UpdateView):
    template_name = "workorder/update_workorder.html"
    model = WorkOrder
    form_class = WorkOrderForm
    success_url = reverse_lazy("workorder_list")


class WorkOrderDetail(DetailView):
    template_name = "workorder/workorder_detail.html"
    model = WorkOrder

    def get_context_data(self, **kwargs):
        context = super(WorkOrderDetail, self).get_context_data(**kwargs)
        context["items"] = WorkOrderItem.objects.filter(work_order=self.object)
        return context


class DeleteWorkOrder(DeleteView):
    template_name = "workorder/delete_workorder.html"
    model = WorkOrder
    fields = "__all__"
    success_url = reverse_lazy("workorder_list")


class CreateWorkOrderItems(CreateView):
    template_name = "workorder/items/create.html"
    model = WorkOrderItem
    form_class = ItemForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'request': self.request, 'work_id': self.kwargs['work_order_id']})
        return kwargs

    def get_success_url(self, **kwargs):
        return reverse_lazy('order_detail', kwargs={'pk': self.kwargs['work_order_id']})


class UpdateWorkOrderItems(UpdateView):
    template_name = "workorder/items/update.html"
    model = WorkOrderItem
    fields = ('item_name', 'item_cost', 'item_quantity')
    success_url = reverse_lazy("home")

    def get_success_url(self, **kwargs):
        return reverse_lazy('order_detail', kwargs={'pk': self.object.work_order_id})


class DeleteWorkOrderItems(DeleteView):
    template_name = "workorder/items/delete.html"
    model = WorkOrderItem
    fields = "__all__"

    def get_success_url(self, **kwargs):
        return reverse_lazy('order_detail', kwargs={'pk': self.object.work_order.id})
