import os
from django.conf import settings
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ImageUploadSerializer
import cv2
import easyocr
from django.core.files.storage import default_storage, FileSystemStorage

# Create your views here.
class OCRView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = ImageUploadSerializer(data=request.data)
        if serializer.is_valid():
            image = serializer.validated_data['image']
            
            # Define the upload folder path
            upload_path = os.path.join(settings.STATIC_ROOT, 'image')
            
            # Create the upload directory if it doesn't exist
            if not os.path.exists(upload_path):
                os.makedirs(upload_path)
            
            # Save the image in the static/image folder
            file_storage = FileSystemStorage(location=upload_path)
            saved_file = file_storage.save(image.name, image)
            file_path = file_storage.path(saved_file)
            
            print(file_path)
            
            # Use OpenCV to read the image
            # image_cv = cv2.imread(file_path)
            # print(image_cv)
            # if image_cv is not None:
            #     return Response(
            #         {"error": "Could not read the image."},
            #         status=status.HTTP_400_BAD_REQUEST
            #     )
                
            # Initialize EasyOCR reader
            reader = easyocr.Reader(['en', 'fr'])
            
            # Perform OCR
            result = reader.readtext(file_path)
            
            # Extract text
            extracted_text = " ".join([text for (_, text, _) in result])

            # Clean up the stored file
            # default_storage.delete(file_path)
            
            return Response(
                {"text": extracted_text},
                status=status.HTTP_200_OK
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)