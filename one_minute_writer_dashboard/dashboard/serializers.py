from rest_framework import serializers
from dashboard.models import WritingInfo
from dashboard.models import WritingTotals

class WritingInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = WritingInfo
        fields = ('writing_id', 'word_count', 'time_spent', 'created_at') #tuple - a finite ordered list


class WritingsSerializer(serializers.Serializer):
    class Meta:
        model = WritingTotals
        fields = ('writing_id', 'total_words', 'total_time_in_seconds')

    # import ipdb; ipdb.set_trace()
