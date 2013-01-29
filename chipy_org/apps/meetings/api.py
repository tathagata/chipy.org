from tastypie import fields
from tastypie.resources import ModelResource
from meetings.models import Meeting, Venue, Presentor, Topic

class VenueResource(ModelResource):
    class Meta:
        queryset = Venue.objects.all()


class PresentorResource(ModelResource):
    class Meta:
        queryset = Presentor.objects.all()


class TopicResource(ModelResource):
    class Meta:
        queryset = Topic.objects.all()


class MeetingResource(ModelResource):
    where = fields.ForeignKey(VenueResource, 'where', full = True)
    date = fields.DateTimeField()
    
    def dehydrate(self, bundle):
        # Include the request IP in the bundle.
        bundle.data['date'] = bundle.data['when']
        del bundle.data['when']
        return bundle

    
    class Meta:
        queryset = Meeting.objects.all()
        fields = ['when', 'id']
