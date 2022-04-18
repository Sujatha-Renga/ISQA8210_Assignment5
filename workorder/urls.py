from django.urls import path
# from . import views
from workorder.views import WorkOrderList, CreateWorkOrder, UpdateWorkOrder, WorkOrderDetail, DeleteWorkOrder, \
    CreateWorkOrderItems, UpdateWorkOrderItems, DeleteWorkOrderItems

urlpatterns = [
    path('create_workorder.html', CreateWorkOrder.as_view(), name='create_workorder'),
    path('workorder_list.html', WorkOrderList.as_view(), name='workorder_list'),
    path('view/<int:pk>/', WorkOrderDetail.as_view(), name='order_detail'),
    path('edit/<int:pk>/', UpdateWorkOrder.as_view(), name='order_update'),
    path('delete/<int:pk>/', DeleteWorkOrder.as_view(), name='order_delete'),
    path('item/<int:work_order_id>/create/', CreateWorkOrderItems.as_view(), name='item_create'),
    path('item/edit/<int:pk>/', UpdateWorkOrderItems.as_view(), name='item_update'),
    path('item/delete/<int:pk>/', DeleteWorkOrderItems.as_view(), name='item_delete')
]
