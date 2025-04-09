from rest_framework import serializers
from app.activity.models import Activity

class ActivityCardSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(source='title_obj')
    description = serializers.CharField(source='description_obj')
    location = serializers.CharField(source='place')
    image = serializers.SerializerMethodField()

    class Meta:
        model = Activity
        fields = ['id', "link", 'image', 'date', 'title', 'description', 'location']


    def get_image(self, obj):
        request = self.context.get('request')
        if obj.image and hasattr(obj.image, 'url'):
            return request.build_absolute_uri(obj.image.url)
        return None
