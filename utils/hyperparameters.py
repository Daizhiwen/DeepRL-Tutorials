import torch
import math

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

#epsilon variables
epsilon_start = 1.0
epsilon_final = 0.01
epsilon_decay = 500
epsilon_by_frame = lambda frame_idx: epsilon_final + (epsilon_start - epsilon_final) * math.exp(-1. * frame_idx / epsilon_decay)

#misc agent variables
GAMMA=0.99
LR=1e-3

#memory
TARGET_NET_UPDATE_FREQ = 100
EXP_REPLAY_SIZE = 10000
BATCH_SIZE = 32

#Multi-step returns
N_STEPS = 1

#Learning control variables
LEARN_START = 32 + N_STEPS
MAX_FRAMES=10000



'''

#epsilon variables
epsilon_start = 1.0
epsilon_final = 0.01
epsilon_decay = 30000
epsilon_by_frame = lambda frame_idx: epsilon_final + (epsilon_start - epsilon_final) * math.exp(-1. * frame_idx / epsilon_decay)

#misc agent variables
GAMMA=0.99
LR=1e-4

#memory
TARGET_NET_UPDATE_FREQ = 1000
EXP_REPLAY_SIZE = 100000
BATCH_SIZE = 32

#Learning control variables
LEARN_START = 10000
MAX_FRAMES=1000000

#Multi-step returns
N_STEPS = 3

'''