import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
import numpy as np


def cal_mse(gt, pred):
    rmse = np.sqrt(np.mean((gt - pred) ** 2))
    return rmse

def cal_mae(gt, pred):
    mae = np.mean(100/len(gt) * np.abs((gt - pred)/gt))
    return mae

def show(gt, pred):
    plt.plot(gt, color='r', label='Ground Truth')
    plt.plot(pred, color='b', label='Prediction')
    plt.legend(loc=2)
    plt.show()