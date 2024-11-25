class MyClass:
    pass


def introspection_info(obj):
    info = {"type": str(type(obj)),
            "attributes": [attr for attr in dir(obj) if not callable(getattr(obj, attr))
                           and not attr.startswith('__')],
            "methods": [method for method in dir(obj) if not callable(getattr(obj, method))
                        and not method.startswith('__')],
            "module": (obj,'__module__')}
    return info


number_info = introspection_info(42)
print(number_info)
class_info = introspection_info(MyClass)
print(class_info)
