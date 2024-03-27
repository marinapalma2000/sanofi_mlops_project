import unittest
from src.data_loader import get_train_test_data_loader

class TestDataLoader(unittest.TestCase):

    def test_data_loader(self):
        trainloader, testloader = get_train_test_data_loader()
        self.assertIsNotNone(trainloader, "Failed to load training data")
        self.assertIsNotNone(testloader, "Failed to load test data")

if __name__ == '__main__':
    unittest.main()