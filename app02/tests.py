from django.test import TestCase

# Create your tests here.
from django.core.servers.basehttp import run
from rest_framework.mixins import CreateModelMixin
from rest_framework.serializers import Serializer
from rest_framework import viewsets
viewsets.GenericViewSet
s = ''
with open('a') as f:
    for l in f:
        table_name = l.split(',')[0].split()[1]
        s+=''' drop table {0} purge ;\n'''.format(table_name)


with open('b','w') as f:
    f.write(s)