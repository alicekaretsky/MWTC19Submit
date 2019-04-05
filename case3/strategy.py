import numpy as np
import pickle

def load_object(file_name):
    "load the pickled object"
    with open(file_name, 'rb') as f:
        return pickle.load(f)


def view_data(data_path):
    data = load_object(data_path)
    prices = data['prices']
    names = data['features']['names']
    features = data['features']['values']
    print(prices.shape)
    print(names)
    print(features.shape)
    return prices, features


class Strategy():
    def __init__(self):
        pass

    def handle_update(self, inx, price, factors):
        tobuy = np.zeros(680)
        for x in range(680):
            if (factors[x][4]>80):
                tobuy[x] += 1.3
            if (factors[x][4]>70):
                tobuy[x] += 1.2
            if (factors[x][4]>60):
                tobuy[x] += 1.1
            if (factors[x][4]>50):
                tobuy[x] += 0.7
            if (factors[x][4]<50):
                tobuy[x] -= 0.7
            if (factors[x][4]<40):
                tobuy[x] -= 1.1
            if (factors[x][4]<30):
                tobuy[x] -= 1.2
            if (factors[x][4]<20):
                tobuy[x] -= 1.3

        assert price.shape[0] == factors.shape[0]
        return tobuy.astype(float)
