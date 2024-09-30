from rest_framework.test import APITestCase


class SampleTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        print("Setting up test data...")

    def test_1(self):
        print("This is test #1")
        self.assertEqual(1, 1)

    def test_2(self):
        print("This is test #2")
        self.assertEqual(2, 2)
