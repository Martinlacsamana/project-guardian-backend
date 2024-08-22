from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from backend.firebase_config import db
from django.views.decorators.csrf import csrf_exempt
import json


class Story(View):
    @csrf_exempt # Disable CSRF protection for now

    # Method for adding a new Story to the database
    def post(self, request):
        try:
            req = json.loads(request.body)
            
            # Unpack relev fields directly into db
            db.collection('story').add({
                'title': req.get('title'),
                'text': req.get('text'),
                'location': req.get('location'),
                'image': req.get('image'),
                'user_id': req.get('user_id')
            })

            return JsonResponse({'status': 'User added successfully'}, status=201)

        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
