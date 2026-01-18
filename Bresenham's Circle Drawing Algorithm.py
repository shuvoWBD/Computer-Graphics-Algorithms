import matplotlib.pyplot as plt

def plot(x, y):
    plt.plot(x, y, 'ro')

def plot_circle_points(xc, yc, x, y):
    points = [
        (xc + x, yc + y), (xc - x, yc + y),
        (xc + x, yc - y), (xc - x, yc - y),
        (xc + y, yc + x), (xc - y, yc + x),
        (xc + y, yc - x), (xc - y, yc - x)
    ]
    for px, py in points:
        print(f"({px}, {py})")
        plot(px, py)

def bresenham_circle(xc, yc, r):
    x = 0
    y = r
    p = 3 - 2 * r
    print("Bresenham Circle Points:")
    while x <= y:
        plot_circle_points(xc, yc, x, y)
        if p < 0:
            p = p + 4 * x + 6
        else:
            p = p + 4 * (x - y) + 10
            y -= 1
        x += 1

if __name__ == "__main__":
    plt.figure()
    bresenham_circle(0, 0, 10)
    plt.title("Bresenham Circle Drawing Algorithm")
    plt.grid(True)
    plt.axis("equal")
    plt.show()