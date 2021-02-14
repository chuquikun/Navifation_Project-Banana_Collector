# P1: Navigation Project - Banana Collector

### Introduction

![trained-agent-with-simple-dqn](images/trained_dqn_agent.gif)

                                                    
<p align="center"> Example of a DQN Tranied Agent </p> 

This repository shows how to train an agent to navigate a large square world and collect yellow bananas as many as it can, avoiding the blue bananas which might be decomposed or poisoned (that's not a normal color for a banana, right?).

A positive reward of +1 is granted for collecting yellow bananas and a negative reward or punish of -1 is given for collecting blue bananas.
The goal of the agent is to maximize its rewards by collecting yellow bananas.

The **state space** has 37 dimensions and contains the agent's velocity, along with ray-based perception of objects around agent's forward direction.  
The **action space** are the following 4 directive that the agent can take at each step:
- **`0`** - move forward.
- **`1`** - move backward.
- **`2`** - turn left.
- **`3`** - turn right.

The agent has to learn what actions are the best to take, given the information provided  by its vector state and its experience of previous steps. The agent is considered to be trained and the environment solved when it gets an average score al least of +13 over 100 episodes.



### Setting the environment up

1. To run the environment we need a specific version of ptyhon so you are ancouraged to set a conda environment. Here the env was called dqn_bca (deep q network banana collector agent):
* For Linux or Mac:

```bash
conda create --name dqn_bca python=3.6
conda activate dqn_bca
```
* For Windows:
```bash
conda create --name dqn_bca python=3.6 
activate dqn_bca
```

2. Perform a minimal installation of OpenAI gym:

*  Run the following line to perform minimal installation
```
git clone https://github.com/openai/gym.git
cd gym
pip install -e .
```
* Install the **classic control** and **box2** environments by runnning:
```
pip install -e '.[classic_control]'
pip install -e '.[box2d]'
```

3. Clone or download this repository:
```
git https://github.com/chuquikun/Navigation_Project-Banana_Collector.git
```
* Move to the folder `python/ ` and install dependencies within:
```
cd python
pip install .
```
4. Create an IPython kernel for the dqn_bca environment:

```
python -m ipykernel install --user --name dqn_bca --display-name "dqn_bca."
```
5. Download the environment from one of the links below.  You need only select the environment that matches your operating system:
    - Linux: [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/Banana_Linux.zip)
    - Mac OSX: [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/Banana.app.zip)
    - Windows (32-bit): [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/Banana_Windows_x86.zip)
    - Windows (64-bit): [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/Banana_Windows_x86_64.zip)
    
    (_For Windows users_) Check out [this link](https://support.microsoft.com/en-us/help/827218/how-to-determine-whether-a-computer-is-running-a-32-bit-version-or-64) if you need help with determining if your computer is running a 32-bit version or 64-bit version of the Windows operating system.
    
    Alternatively you can download a headless version of the Linux environment which is very convenient to train the agent without launch the graphic interface.
    - Linux No Visualization:[click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/Banana_Linux_NoVis.zip)
    
6. Place the file in the the roor of this repository and unzip (or decompress) the file. 

7. Running the notebooks 

To launch the notebooks run in the root of this directory:
```
jupyter notebook
```
Finally select and double-click the notebook you want to run.
Before running code in any notebook, change the kernel to match the dqn_bc environment by using the drop-down Kernel menu.
