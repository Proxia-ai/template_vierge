import numpy as np

mean_compute = lambda tab: np.mean(tab)

if __name__ == "__main__":
    tab = [3, 4, 5]
    res = mean_compute(tab)
    print(res)
