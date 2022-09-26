import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-W", type=int)
parser.add_argument("-w", nargs='+', type=int)
parser.add_argument("-n", type=int)
args = parser.parse_args()


def knapsack(W, w, n):
    K = [[0 for x in range(W + 1)] for x in range(n + 1)]
    for i in range(n + 1):
        for j in range(W + 1):
            if i == 0 or j == 0:
                K[i][j] = 0
            elif w[i - 1] <= j:
                K[i][j] = max(w[i - 1] + K[i - 1][j - w[i - 1]], K[i - 1][j])
            else:
                K[i][j] = K[i - 1][j]

    return K[n][W]


print(knapsack(args.W, args.w, args.n))
