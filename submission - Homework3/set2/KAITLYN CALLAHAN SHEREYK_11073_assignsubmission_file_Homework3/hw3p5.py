from sys import argv

def trajectory(argv):
    v0, t = float(argv[0]), float(argv[1])
    g=9.81
    y=v0*t-0.5*g*t**2
    return y


def main(argv):
    print(trajectory(argv[1:]))

if __name__ == '__main__':
    main(argv)