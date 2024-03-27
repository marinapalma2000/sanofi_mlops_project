import unittest
import torch
from src.model import Net

class TestModel(unittest.TestCase):

    def test_model_initialization(self):
        net = Net()
        self.assertIsInstance(net, Net, "Failed to initialize the Net model")

    def test_model_forward_pass(self):
        net = Net()
        input_tensor = torch.rand(1, 3, 32, 32) 
        output = net(input_tensor)
        self.assertEqual(output.shape, torch.Size([1, 10]), "Model output has incorrect shape")

if __name__ == '__main__':
    unittest.main()
