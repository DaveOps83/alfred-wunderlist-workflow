from peewee import (BooleanField, CharField, IntegerField, PeeweeException,
                    PrimaryKeyField, TextField)

from wunderlist.models import DateTimeUTCField
from wunderlist.models.base import BaseModel
from wunderlist.util import workflow

class List(BaseModel):
    id = PrimaryKeyField()
    title = TextField(index=True)
    list_type = CharField()
    public = BooleanField()
    completed_count = IntegerField(default=0)
    uncompleted_count = IntegerField(default=0)
    order = IntegerField(index=True)
    revision = IntegerField()
    created_at = DateTimeUTCField()

    @classmethod
    def sync(cls, lists_data=None):
        instances = []

        try:
            instances = cls.select()
        except PeeweeException:
            pass

        if not lists_data:
            from wunderlist.api import lists
            lists_data = lists.lists()

        cls._perform_updates(instances, lists_data)

        return None

    @classmethod
    def prepare_sync_data(cls):
        from wunderlist.api import lists

        lists_data = lists.lists()
        workflow().store_data('lists', lists_data)

        return lists_data

    @classmethod
    def _populate_api_extras(cls, info):
        from wunderlist.api.lists import update_list_with_tasks_count

        update_list_with_tasks_count(info)

        return info

    def _sync_children(self):
        from wunderlist.models.task import Task

        Task.sync_tasks_in_list(self)

    class Meta:
        order_by = ('order', 'id')
