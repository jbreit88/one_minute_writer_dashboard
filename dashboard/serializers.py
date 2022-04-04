from rest_framework import serializers
from dashboard.models import WritingInfo
from dashboard.models import WritingTotals

# Responsible for serializing dashboard_list POST repsonse
class WritingInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = WritingInfo
        fields = ('writing_id', 'word_count', 'time_spent', 'created_at') #tuple - a finite ordered list


# This class is currently unused, but may be of use at a later date if we would like to serialize a list of writings. Perhaps for chunking data by time period.
class WritingsSerializer(serializers.Serializer):
    writing_id = serializers.CharField()
    total_words = serializers.IntegerField()
    total_time_in_seconds = serializers.IntegerField()

# Responsible for serializing dashboard_list GET response
class DashboardMetricsSerializer(serializers.Serializer):
    total_words_all_time = serializers.IntegerField()
    total_time_all_time = serializers.IntegerField()
    average_words_per_minute = serializers.IntegerField()
