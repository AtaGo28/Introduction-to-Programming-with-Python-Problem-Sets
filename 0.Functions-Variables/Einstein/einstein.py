def energy(m):
    c = 300000000  # meters per second
    E = m * pow(c, 2)
    return E
    # print("energy(j): ", E)


def main():
    mass = int(input("mass(kg): "))
    print("energy(j):", energy(mass))


main()
