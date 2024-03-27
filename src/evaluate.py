import torch
from model import Net
from data_loader import get_train_test_data_loader

MODEL_OUTPUT_PATH = './models/model.pth'

def evaluate():
    _, testloader = get_train_test_data_loader()
    net = Net()
    net.load_state_dict(torch.load(MODEL_OUTPUT_PATH))

    correct = 0
    total = 0
    with torch.no_grad():
        for data in testloader:
            images, labels = data
            outputs = net(images)
            _, predicted = torch.max(outputs.data, 1)
            total += labels.size(0)
            correct += (predicted == labels).sum().item()

    print('Accuracy of the network on the 10000 test images: %d %%' % (
        100 * correct / total))

if __name__ == "__main__":
    evaluate()