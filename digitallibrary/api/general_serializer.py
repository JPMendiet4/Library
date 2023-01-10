from rest_framework import generics


class GeneralListApiView(generics.ListAPIView):
    """Generic view to read a list of objects from a model and return them as an HTTP response. """
    allowed_methods = ['get']
    serializer_class = None
    # Especifica que serializador se debe usar para convertir los objetos del modelo en datos serializados

    def get_queryset(self):
        """Gets the list of model objects to include in the HTTP response. """
        model = self.get_serializer_class().Meta.model
        # Obtiene el modelo especificado en el serializador a través de su clase anidada Meta y su propiedad model.
        return model.objects.all()