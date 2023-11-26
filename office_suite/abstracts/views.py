from rest_framework import filters
from rest_framework import generics
from rest_framework.permissions import BasePermission, IsAdminUser


class ModelPermissionFactory:
    permissions_map = {}

    @staticmethod
    def get_model_permission(model):
        permission = model.__name__.lower()
        if permission in ModelPermissionFactory.permissions_map.keys():
            return ModelPermissionFactory.permissions_map[permission]
        else:
            return ModelPermissionFactory._create_model_permission(permission)

    @staticmethod
    def _create_model_permission(permission):
        class ModelPermission(BasePermission):

            def has_permission(self, request, view):
                return self.has_object_permission(request, view, None)

            def has_object_permission(self, request, view, obj):
                if request.method == 'GET':
                    return request.user.user_permissions.all().filter(codename=f'view_{permission}').exists()
                elif request.method == 'POST':
                    return request.user.user_permissions.all().filter(codename=f'add_{permission}').exists()
                elif request.method in ['PUT', 'PATCH']:
                    return request.user.user_permissions.all().filter(codename=f'change_{permission}').exists()
                elif request.method == 'DELETE':
                    return request.user.user_permissions.all().filter(codename=f'delete_{permission}').exists()
                else:
                    return False

        ModelPermissionFactory.permissions_map[permission] = ModelPermission
        return ModelPermission


class AbstractDetailView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    service_class = None
    model_class = None

    def __init__(self):
        if self.service_class is None:
            raise NotImplementedError(
                'the fields service_class and model_class have to be defined, otherwise it is not possible to initialize the AbstractView')
        self.model_class = self.service_class.get_model_class()

    def get_model_permission(self):
        return ModelPermissionFactory.get_model_permission(self.model_class)

    def get_permissions(self):
        return [p() for p in [self.get_model_permission() | IsAdminUser]]

    def get_queryset(self):
        return self.service_class.get_queryset(self.request)

    def get_serializer_class(self):
        return self.service_class.get_serializer_class(self.request)


class AbstractListCreateView(generics.ListCreateAPIView):
    service_class = None
    model_class = None

    def __init__(self):
        if self.service_class is None:
            raise NotImplementedError(
                'the fields service_class and model_class have to be defined, otherwise it is not possible to initialize the AbstractView')
        self.model_class = self.service_class.get_model_class()
        self.filter_backends = [filters.SearchFilter]
        self.search_fields = list(
            filter(lambda name: name != 'id', map(lambda f: f.name, self.model_class._meta.fields)))

    def get_model_permission(self):
        return ModelPermissionFactory.get_model_permission(self.model_class)

    def get_permissions(self):
        return [p() for p in [self.get_model_permission() | IsAdminUser]]

    def get_queryset(self):
        return self.service_class.get_queryset(self.request)

    def get_serializer_class(self):
        return self.service_class.get_serializer_class(self.request)
