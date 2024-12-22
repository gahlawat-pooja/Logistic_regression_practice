import numpy as np
import matplotlib.pyplot as plt
# square root of x 
def sqrt(x):
    return np.sqrt(x)
# main function
def main():
    x = np.linspace(0, 500, 200)
    y = sqrt(x)
    # add x and y labels
    plt.xlabel('Integers')
    plt.ylabel('Square root')
    # fig title
    plt.title('Square root of integers')
    plt.plot(x, y)
    plt.show()
if __name__ == '__main__':
    main()