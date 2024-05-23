from rest_framework import serializers

class ImageUploadSerializer(serializers.Serializer):
    """
    Serializer class for handling image uploads.
    
    This class defines a single field `image`, which expects an uploaded image file.
    It uses the `ImageField` from Django REST framework to handle image validation and processing.
    
    Fields:
    -------
    image : serializers.ImageField
        An image file to be uploaded and processed.
        
    Example:
    --------
    # Serialization: Convert a Python object to JSON
    image_upload_instance = ImageUpload(image=<InMemoryUploadedFile>)
    serializer = ImageUploadSerializer(image_upload_instance)
    print(serializer.data)
    # Output: {'image': '<URL or path to the image>'}
    
    # Deserialization: Convert JSON data to a Python object
    data = {'image': <InMemoryUploadedFile>}
    serializer = ImageUploadSerializer(data=data)
    if serializer.is_valid():
        image_instance = serializer.save()
        print(image_instance)
    """
    
    image = serializers.ImageField()