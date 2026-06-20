# soil_tech_api/test.py
from django.test import TestCase
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from rest_framework import status
from rest_framework.test import APIClient

from soilsensor_app.models import Sensor, Sample  # Make sure these imports are correct


class ProcessSampleCSVTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        
        # Create BOTH sensors needed in the CSV
        self.sensor1 = Sensor.objects.create(id=1)   # Add other required fields if any
        self.sensor2 = Sensor.objects.create(id=2)   # Add other required fields if any

    def test_process_valid_csv(self):
        csv_content = """sensor_id,nitrogen,phosphorus,potassium,pH,latitude,longitude
1,25.5,15.2,30.1,6.8,40.7128,-74.0060
2,28.0,18.5,35.0,7.2,40.7306,-73.9352"""

        csv_file = SimpleUploadedFile(
            "test_sample.csv",
            csv_content.encode('utf-8'),
            content_type="text/csv"
        )

        response = self.client.post(
            reverse('load-sample-csv'),
            {'csv_file': csv_file},
            format='multipart'
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Sample.objects.count(), 2)
        self.assertIn("message", response.data)