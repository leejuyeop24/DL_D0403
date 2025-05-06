# utils.py

import matplotlib.pyplot as plt

def plot_history(HIST):
    plt.plot(HIST['Train'][0], HIST['Train'][1], label='Train Loss')
    plt.plot(HIST['Valid'][0], HIST['Valid'][1], label='Valid Loss')
    plt.xlabel('Epoch')
    plt.ylabel('Loss')
    plt.title('Training History')
    plt.legend()
    plt.grid(True)
    plt.show()