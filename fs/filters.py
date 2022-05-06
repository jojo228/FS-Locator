
from django.db.models import fields
import django_filters
from django_filters import DateFilter, CharFilter
from .models import *

  

class ClientFilter(django_filters.FilterSet):
    nom = CharFilter(field_name ="nom_client", lookup_expr="icontains", label="Nom")
    prenom = CharFilter(field_name ="Prénoms_client", lookup_expr="icontains", label="Prénoms")
    start_date = DateFilter(field_name ="date_created", lookup_expr="gte", label="Clients ajouté entre le")
    end_date = DateFilter(field_name ="date_created", lookup_expr="lte", label="et le")

    class Meta:
        model = Client
        fields =  ('agent', 'zone')
        


class ClientFilter2(django_filters.FilterSet):
    nom = CharFilter(field_name ="nom_client", lookup_expr="icontains", label="Nom")
    prenom = CharFilter(field_name ="Prénoms_client", lookup_expr="icontains", label="Prénoms")
    start_date = DateFilter(field_name ="date_created", lookup_expr="gte", label="Clients ajouté entre le")
    end_date = DateFilter(field_name ="date_created", lookup_expr="lte", label="et le")

    class Meta:
        model = Client
        fields =  ('zone',)


