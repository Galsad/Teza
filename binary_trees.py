def generate_inf_and_vars_for_tree(depth = 10):
    E = range(1, depth + 1)
    V = [0]
    for i in range(1, depth):
        V.append(V[-1] + 0.5 * E[i-1]**2)

    return V, E

if __name__ == "__main__":
    depth = 6
    V, E = generate_inf_and_vars_for_tree(depth)
    print len(V), len(E)
    n = 2**depth
    print V, E
    print V[-1] / E[-1]**2
    s = 0
    for i in range(1, depth + 1):
        s += (V[i-1] * (n / 2**i))

    s /= n
    s /= depth

    print s