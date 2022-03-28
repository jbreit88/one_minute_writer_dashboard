from rest_framework import serializers
from dashboard.models import WritingInfo
from dashboard.models import WritingTotals

class WritingInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = WritingInfo
        fields = ('writing_id', 'word_count', 'time_spent', 'created_at') #tuple - a finite ordered list


class WritingsSerializer(serializers.Serializer):
    writing_id = serializers.CharField()
    total_words = serializers.IntegerField()
    total_time_in_seconds = serializers.IntegerField()

class DashboardMetricsSerializer(serializers.Serializer):
    total_words_all_time = serializers.IntegerField()
    total_time_all_time = serializers.IntegerField()


    # import ipdb; ipdb.set_trace()
