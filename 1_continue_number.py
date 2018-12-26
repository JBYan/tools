
def max_continue(a):
    """ 'a' is a list may continue or break at some point, such as
         a = [1, 2, 3, 5, 6, 7, 8, 10, 11, 12, 15, 18, 19, 20] """
    cont, cont_list = 1, []
    for i, v in enumerate(a):
        if i == len(a) - 1:
            cont_list.extend([cont] * cont)
        elif a[i + 1] - v != 1:
            cont_list.extend([cont] * cont)
            cont = 1
        else:
            cont += 1
    print(cont_list)


if __name__ == "__main__":

    a = [1, 2, 3, 5, 6, 7, 8, 10, 11, 12, 15, 18, 19, 20]
    print(a)
    max_continue(a)
