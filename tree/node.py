class Node:
    """
    """

    # Name -
    # Childs -
    # Resource -

    def __init__(self, name, childs, resource):
        self._name = name
        self._childs = childs
        self._resource = resource

    @property
    def name(self): pass

    @name.setter
    def name(self, name): pass

    @property
    def childs(self): pass

    @child.setter
    def childs(self, childs = None): pass

    @property
    def resource(self): pass

    @resource.setter
    def resource(self, obj = None): pass

    def add_childs(self, childs): pass
