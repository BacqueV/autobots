class Container:
    def __init__(self):
        self._registry = {}

    def register(self, name, obj):
        self._registry[name] = obj

    def get(self, name):
        return self._registry.get(name)


container = Container()
