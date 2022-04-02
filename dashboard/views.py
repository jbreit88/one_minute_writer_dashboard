from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from django.core import serializers

from django.core.exceptions import BadRequest

from dashboard.models import WritingInfo
from dashboard.models import WritingTotals
from dashboard.models import DashboardMetrics
from dashboard.serializers import WritingInfoSerializer
from dashboard.serializers import WritingsSerializer
from dashboard.serializers import DashboardMetricsSerializer
from rest_framework.decorators import api_view
from django.db.models import Sum

@api_view(['GET', 'POST'])
def dashboard_list(request):

    if request.method == 'GET':
        #receive array of writing_ids associated with user as writing_ids
        writing_ids = request.GET.get('writing_ids', '').split(',')
        booleans = []

        #iterates over all WritingInfo objects & compares with id list passed as params
            #shovels boolean value whether list includes id
        for obj in WritingInfo.objects.all():
            booleans.append((str(obj.id) in writing_ids))
            
        #if any booleans in 'boolean' list are False it is a bad request
        if False in booleans:
            raise BadRequest('Invalid request')
        else:

        # writing_ids[0] not in WritingInfo.objects.all()
        # make empty array to fill with nested hashes of necessary information
            writings = []

        # Iterate through writing_ids to count total words and time for all IDs passed
        for id in writing_ids:
            w = WritingInfo.objects.filter(writing_id=id)
            total_words = w.aggregate(Sum('word_count'))
            total_time = w.aggregate(Sum('time_spent'))

            # Save totals of word count and time for each document id
            writing_total = WritingTotals(writing_id=id, total_words=total_words['word_count__sum'], total_time_in_seconds=total_time['time_spent__sum'])

            # Put totals of each document in list to iterate over and sum later.
            writings.append(writing_total)

        # Set some variables to keep track of added up time and words
        time = 0
        words = 0

        for writing in writings:
            # These can be refactored to use += operator
            # For each writing totals object in the writings array we add the time and word count to our counter variables above.
            time = time + writing.total_time_in_seconds
            words = words + writing.total_words

        # Create a dashboard_metrics object with the totals calculated above
        dashboard_metrics = DashboardMetrics(total_words_all_time=words, total_time_all_time=time)

        # Serialize data and send in a response.
        dashboard_serializer = DashboardMetricsSerializer(dashboard_metrics)

            return JsonResponse(dashboard_serializer.data, safe=False)

    elif request.method == 'POST':
        # Capture the posted ID
        id = request.GET.get('writing_id', '')

        # Find all rows in database associated with the document ID provided
        all_entries = WritingInfo.objects.filter(writing_id=id)
        entries_list = list(all_entries) # Change all entries into a list, not a query object.

        if entries_list == []:
            # If this is a new document ID, no calculations need to be done. Simply grab the word count, the time, and the ID and persist them to the DB.
            first_word_count = request.GET.get('word_count', '')
            first_total_time = request.GET.get('total_time', '')

            new_writing = WritingInfo.objects.create(writing_id=id, word_count=int(first_word_count), time_spent=int(first_total_time))

            # Serialize the data
            writing_info_serializer = WritingInfoSerializer(new_writing)

            # Check that object was persisted to the database. Return status 201 if it exists, return status 400 if creation failed.
            if WritingInfo.objects.filter(id=new_writing.id).exists():

                return JsonResponse(writing_info_serializer.data, status=status.HTTP_201_CREATED)

            return JsonResponse({'message': 'Bad request, object not saved'}, status='400')

        elif entries_list != []:
            # If this document has been posted to the databse previously, we must aggregate all relevant data.

            # First, capture our posted values
            posted_word_count = request.GET.get('word_count', '')
            posted_time = request.GET.get('total_time', '')

            # Second, filter our database by the document ID to find all rows that are associated with this document. Then sub the word_count column and the time_spent column.
            w = WritingInfo.objects.filter(writing_id=id)

            logged_word_total = w.aggregate(Sum('word_count'))
            logged_time_total = w.aggregate(Sum('time_spent'))

            logged_word_total_int = logged_word_total['word_count__sum']
            logged_time_total_int = logged_time_total['time_spent__sum']

            # Make sure everything is an integer and not a string. Calculate the difference between the total posted and the accumulated previously posted data.
            words_diff = int(posted_word_count) - int(logged_word_total_int)
            time_diff = int(posted_time) - int(logged_time_total_int)

            # Use the difference in those values to post a new row with the same ID, but the newly calculated words and time differences.
            new_writing = WritingInfo.objects.create(writing_id=id, word_count=words_diff, time_spent=time_diff)

            writing_info_serializer = WritingInfoSerializer(new_writing)

            # Check that object has been eprsisted ot DB. Return a 201 status if created, and a 400 status if not.
            if WritingInfo.objects.filter(id=new_writing.id).exists():

                return JsonResponse(writing_info_serializer.data, status=status.HTTP_201_CREATED)

            return JsonResponse({'message': 'Bad request, object not saved'}, status='400')
