from django.db import models as foo_models
from attr import attrs, attrib


@attrs
class AnotherAttribDataModel:
    a = attrib()
    b = attrib()


class NotDataModel:
    pass


class FooDataModel(foo_models.Model):
    name = foo_models.CharField(max_length=100)
    last_name = foo_models.CharField(max_length=100)
