from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from django.core import serializers

from dashboard.models import WritingInfo
from dashboard.models import WritingTotals
from dashboard.serializers import WritingInfoSerializer
from dashboard.serializers import WritingsSerializer
from rest_framework.decorators import api_view
from django.db.models import Sum

@api_view(['GET', 'POST'])
def dashboard_list(request):
    # import ipdb; ipdb.set_trace()

    if request.method == 'GET':
        #receive array of writing_ids associated with user as writing_ids
        writing_ids = request.GET.get('writing_ids', '').split(',')

        # make empty array to fill with nested hashes of necessary information
        writings = []

        for id in writing_ids:
            w = WritingInfo.objects.filter(writing_id=id)
            total_words = w.aggregate(Sum('word_count'))
            total_time = w.aggregate(Sum('time_spent'))

            writing_total = WritingTotals(writing_id=id, total_words=total_words, total_time_in_seconds=total_time)

            writings.append(writing_total)

        writings_serializer = WritingsSerializer(writings)
        import ipdb; ipdb.set_trace()
        #return writings array in serialized response.
        # serialized_writings = WritingsSerializer(data=writings)

        return JsonResponse(writings_serializer.data)


# @api_view(['POST'])
# def dashboard_detail(request):
#     if request.method == 'POST'
#         id = request.GET.get('writing_id', '')
#
#         all_entries = WritingInfo.objects.filter(writing_id=id)
#
#         if all_entries == []
#             w = WritingInfo(writing_id=id, word_count=request.GET.get('word_count', ''), time_spent=request.GET.get('time_spent', ''))
#
#             if w.save():
#                 return JsonResponse(writing_serializer.data, status=status.HTTP_201_CREATED)
#
#             return JsonResponse(writing_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#         elif all_entries != []
#             prev_word_count = all_entries.aggregate(Sum('word_count'))
#             prev_time_spent = all_entries.aggregate(Sum('time_spent'))
#
#             total_word_count = request.GET.get('word_count', '')
#             total_time_spent = request.GET.get('total_time', '')
#
#             add_word_count = total_word_count - prev_word_count
#             add_time_spent = total_time_spent - prev_time_spent
#
#             w = WritingInfo(writing_id=id, word_count=add_word_count, time_spent=add_time_spent)
#
#             if w.save():
#                 return JsonResponse(writing_serializer.data, status=status.HTTP_201_CREATED)
#
#             return JsonResponse(writing_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
