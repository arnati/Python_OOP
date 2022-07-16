class Layer:
    def __init__(self):
        self.next_layer = None
        self.name = 'Layer'

    def __call__(self, *args, **kwargs):
        self.next_layer = args[0]
        return self.next_layer


class Input(Layer):
    def __init__(self, inputs):
        super().__init__()
        self.inputs = inputs
        self.name = 'Input'


class Dense(Layer):
    def __init__(self, inputs, outputs, activation):
        super().__init__()
        self.inputs = inputs
        self.outputs = outputs
        self.activation = activation
        self.name = 'Dense'


class NetworkIterator:
    def __init__(self, link_obj):
        self.link_obj = link_obj

    def __iter__(self):
        current_obj = self.link_obj
        while current_obj.next_layer is not None:
            yield current_obj
            current_obj = current_obj.next_layer
        else:
            yield current_obj



# first_layer = Layer()
# next_layer = first_layer(Layer())
# next_layer = next_layer(Layer())
# next_layer = next_layer(Layer())
# next_layer = next_layer(Layer())
#
# pass

network = Input(128)
layer = network(Dense(network.inputs, 1024, 'linear'))
layer = layer(Dense(layer.inputs, 10, 'softmax'))

for x in NetworkIterator(network):
    print(x.name)

pass
