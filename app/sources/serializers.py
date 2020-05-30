""""Serializers for News"""

from rest_framework import serializers

from .models import Source

class SourceSerializer(serializers.ModelSerializer):
    """Set the fields to be use in the view"""

    class Meta:
        model = Source
        fields = ('name',
                  'url',
                  'feed_url',
                  'feed_type',
                  'disclaimer',
                  'logo')
