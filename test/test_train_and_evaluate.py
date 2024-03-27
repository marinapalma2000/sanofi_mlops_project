import unittest
import os
from src.train import train
from src.evaluate import evaluate
from src.model import Net

class TestTrainAndEvaluate(unittest.TestCase):

    def test_train_and_evaluate(self):
        train()
        self.assertTrue(os.path.exists('./models/model.pth'), "Model file not found after training")

        evaluate()  

if __name__ == '__main__':
    unittest.main()
