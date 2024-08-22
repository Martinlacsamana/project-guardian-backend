from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from backend.firebase_config import db
from django.views.decorators.csrf import csrf_exempt
import json

class User(View):
    @csrf_exempt  # Disable CSRF protection for this view
    def post(self, request):
        try:
            user_data = json.loads(request.body)
            user_id = user_data.get('user_id')
            phone_number = user_data.get('phone_number')

            db.collection('user').add({
                'user_id': user_id,
                'phone_number': phone_number
            })

            return JsonResponse({'status': 'User added successfully'}, status=201)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

