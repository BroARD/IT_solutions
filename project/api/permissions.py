from rest_framework import permissions

#Доступ только для владельца(Для редактирования авто)
class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user == obj.owner
