import matplotlib.pyplot as plt

def plot(x, y):
    plt.plot(x, y, 'ro')

def adaptive_decision_boundary(x1, y1, x2, y2):
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    steep = dy > dx

    if steep:
        x1, y1, x2, y2 = y1, x1, y2, x2
    if x1 > x2:
        x1, x2, y1, y2 = x2, x1, y2, y1

    dx = x2 - x1
    dy = abs(y2 - y1)
    error = dx / 2
    ystep = 1 if y1 < y2 else -1
    y = y1
    print("Adaptive Decision Boundary Points:")
    for x in range(x1, x2 + 1):
        if steep:
            print(f"({y}, {x})")
            plot(y, x)
        else:
            print(f"({x}, {y})")
            plot(x, y)
        error -= dy
        if error < 0:
            y += ystep
            error += dx

if __name__ == "__main__":
    plt.figure()
    adaptive_decision_boundary(2, 2, 10, 6)
    plt.title("Adaptive Decision Boundary Line Drawing Algorithm")
    plt.grid(True)
    plt.show()