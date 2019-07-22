from  sys import intern

class Node:
    """
    """

    # Name     - str
    # Childs   - List of dict object
    # Resource - Rest_Resource

    def __init__(self, name, childs, resource):
        self._name = name
        self._childs = childs
        self._resource = resource

    @property
    def childs(self):
        return self._childs

    @property
    def name(self):
        return self._name

    @property
    def resource(self):
        return self._resource

    @child.setter
    def childs(self, childs = None):
        if isinstance(childs, list) & self._is_all_dict(childs):
            self._childs = childs
        else:
            raise ValueError(f"Received a {type(childs)} but expecting a list of dict(s)")

    @name.setter
    def name(self, name):
        if isinstance(name, str):
            self._name = intern(name) # TODO: optimization for comparison?
        else:
            raise ValueError(f"Received a {type(name)} but expecting a str")

    @resource.setter
    def resource(self, obj = None):
        pass

    def _is_all_dict(dict_list):
        result = True

        for i in dict_list:
            if isinstance(i, dict):
                result = false
                break

        return result

    def add_child(self, child):
        pass

    def get_child(self child):
        pass
