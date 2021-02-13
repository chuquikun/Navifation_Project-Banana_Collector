import torch
import torch.nn as nn
import torch.nn.functional as F

class QNetwork(nn.Module):
    """Actor (Policy) Model."""

    def __init__(self, state_size, action_size, hidden_layers, p, seed):
        """Initialize parameters and build model.
        Params
        ======
            state_size (int): Dimension of each state
            action_size (int): Dimension of each action
            seed (int): Random seed
            fc1_units (int): Number of nodes in first hidden layer
            fc2_units (int): Number of nodes in second hidden layer
        """

        super(QNetwork, self).__init__()
        # Set random seed
        self.seed = torch.manual_seed(seed)
        # Define input and output for each hidden layer
        layer_sizes = zip(hidden_layers[:-1], hidden_layers[1:])
        # Create ModuleList and add input layer
        self.hl = nn.ModuleList([nn.Linear(state_size, hidden_layers[0])])
        # Add hidden layers to the ModuleList
        self.hl.extend([nn.Linear(h1, h2) for h1, h2 in layer_sizes])
        # Add output layer
        self.output = nn.Linear(hidden_layers[-1], action_size)
        # Add the probability for a node to be dropped at each layer
        self.dropout = nn.Dropout(p=p)
    
    def forward(self, x):
        for linear in self.hl:
            x = F.relu(linear(x))
            x = self.dropout(x)
                
        return self.output(x)
