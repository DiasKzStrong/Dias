from django.db.models import QuerySet
from django.core.exceptions import ValidationError



class QuerySetMixin:
    queryset = None
    serializer_class = None

    def get_queryset(self):
        if isinstance(self.queryset,QuerySet):
            q = self.queryset.filter(user = self.request.user)
            return q
        raise ValidationError('queryset should be istance of QuerySet class')
