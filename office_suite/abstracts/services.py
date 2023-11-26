import abc


class Service(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'get_serializer_class') and
                callable(subclass.get_serializer_class) and
                hasattr(subclass, 'get_queryset') and
                callable(subclass.get_queryset) and
                hasattr(subclass, 'get_model_class') and
                callable(subclass.get_model_class))
