import torch
import torchvision
import torch.nn as nn
import torch.nn.functional as F
import matplotlib.pyplot as plt
from torchvision import transforms, datasets

# %%
train = datasets.MNIST("",
                       train=True,
                       download=True,
                       transform=transforms.Compose([transforms.ToTensor()]))
test = datasets.MNIST("",
                      train=False,
                      download=True,
                      transform=transforms.Compose([transforms.ToTensor()]))
# %%
trainset = torch.utils.data.DataLoader(train, batch_size=10, shuffle=True)
testset = torch.utils.data.DataLoader(test, batch_size=10, shuffle=True)


# %%
class Net(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = nn.Linear(28 * 28, 64)
        self.fc2 = nn.Linear(64, 64)
        self.fc3 = nn.Linear(64, 64)
        self.fc4 = nn.Linear(64, 10)

    def forward(self, x):
        x = torch.tanh(self.fc1(x))
        x = torch.tanh(self.fc2(x))
        x = torch.tanh(self.fc3(x))
        x = self.fc4(x)

        return F.log_softmax(x, dim=1)


# %%
net = Net()
print(net)

# %%
X = torch.rand((28, 28))
X = X.view(-1, 28 * 28)
print(X)

# %%
output = net(X)
print(output)
# %%
