from django.db.models import Manager
from hh_app.querysets import CustomBaseQuerySet


class CustomManager(Manager):
    def get_or_none(self, pk=None):
        try:
            return self.get_queryset().get(pk=pk)
        except self.model.DoesNotExist:
            return None

    def all(self):
        return self.get_queryset().filter(is_public=True)

    def get_queryset(self):
        return CustomBaseQuerySet(self.model, using=self._db)

