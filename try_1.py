import numpy as np
import matplotlib.pyplot as plt
# square root of x 
def sqrt(x):
    return np.sqrt(x)
# main function
def main():
    x = np.linspace(0, 100, 100)
    y = sqrt(x)
    plt.plot(x, y)
    plt.show()
if __name__ == '__main__':
    main()