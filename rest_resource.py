class Rest_Resource:
    """
    An endpoint is a rest resource (noun).
    """

    def __init__(self, name, description, data_model):
        self._name = name
        self._description = description
        self._data_model = data_model

    def __str__(self):
        return f"Name: {self.name}\
        \nDescription: {self.description}\
        \nData Model: {self.data_model}"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description):
        self._description = description

    @property
    def data_model(self):
        return self._data_model

    @data_model.setter
    def model(self, model):
        self._data_model = data_model

def __main__():
    # Test me
    name = "Template"
    description = "Template of something"
    model = "some data structure"

    # Create an instance
    my_res = Rest_Resource(name, description, model)

    # Test the class dunder __str__
    print("#"*40)
    print("my_res using str() = see next line")
    print(str(my_res))

    # Test the property setter, .name does not exist.
    print("#"*40)
    my_res.name = "Template 2"

    #Verify setter works by accessing the property getter and the _name
    print(f"my_res.name = {my_res.name}")
    print(f"my_res._name = {my_res._name}")
    print("#"*40)


if __name__ == '__main__':
    __main__()
    print("DONE")
