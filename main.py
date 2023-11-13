import random


def bubleSort(mass):
    for i in range(len(mass)-1):
        for j in range(len(mass)-i-1):
            if mass[j] > mass[j+1]:
                temp = mass[j]
                mass[j] = mass[j+1]
                mass[j+1] = temp
    return mass


if __name__ == '__main__':
    print("Введите количество элементов в массиве: ")
    n = int(input())
    print("Введите параметр сортировки: \n0 - по убыванию \n1 - по возрастанию")
    p = int(input())

    mass = [0] * n

    for i in range(n):
        mass[i] = int(random.random() * 100)

    print(mass)
    sortedMass = bubleSort(mass)
    print(sortedMass)
