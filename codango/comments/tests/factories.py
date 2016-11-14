import factory

from comments import models
from community.tests.factories import UserFactory
from datetime import datetime, timedelta
from freezegun import freeze_time
from resources.tests.factories import ResourceFactory


@freeze_time("2016-09-14 12:00:01")
class CommentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Comment

    author = factory.RelatedFactory(UserFactory)
    resource = factory.RelatedFactory(ResourceFactory)
    content = 'This is a sample comment'
    date_created = datetime.now()
    date_modified = date_created + timedelta(hours=1)
