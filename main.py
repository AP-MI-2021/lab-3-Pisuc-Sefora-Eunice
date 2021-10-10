def is_prime(n):
    for i in range(2,n):
        if n%i==0:
            return False
    return True
#8.get_longest_sum_is_prime(lst: list[int]) -> list[int]
def get_longest_sum_is_prime(lst):
    index_start = 0
    index_end = 0
    lung_max = 0
    for ids in range(len(lst) - 1):
        for ide in range(ids, len(lst)):
            if (is_prime(sum(lst[ids:ide + 1])) == True):
                if len(lst[ids:ide + 1]) > lung_max:
                    lung_max = len(lst[ids:ide + 1])
                    index_start = ids
                    index_end = ide
    return lst[index_start:index_end + 1]
#16.get_longest_arithmetic_progression(lst: list[int]) -> list[int]
def get_longest_arithmetic_progression(lst):
    index_start = 0
    index_end = 0
    lung_max = 0
    for ids in range(len(lst) - 1):
        for ide in range(ids, len(lst)):
            if (sum(lst[ids:ide + 1]) == (lst[ids]+lst[ide])* len(lst[ids:ide + 1])/2):
                if len(lst[ids:ide + 1]) > lung_max:
                    lung_max = len(lst[ids:ide + 1])
                    index_start = ids
                    index_end = ide
    return lst[index_start:index_end + 1]

def citire():
    n = int(input("Intoducem numarul de numere al listei:"))
    lst=[]
    for i in range(n):
        lst.append(int(input("Indroducem numar:")))
    return lst

def meniu():
    print("1.Citire date")
    print("2.Determina cea mai lunga secventa cu suma numerelor prima")
    print("3.Determina toate numerele in progresie aritmetica")
    print("4.Iesire")
def run():
    lst=[]
    while (True==True):
        meniu()
        opt=int(input("Alege optiunea"))
        if opt == 1:
            lst=citire()
        elif opt == 2:
            if len(lst)!=0:
                print(get_longest_sum_is_prime(lst))
        elif opt == 3:
            if len(lst)!=0:
                print(get_longest_arithmetic_progression(lst))
        elif opt == 4:
            break
        else :
            print("Optinea nu exista in meniu")
def test_get_longest_arithmetic_progression():
    assert(get_longest_arithmetic_progression([13,1,4,7,10,13,16,22])==[1,4,7,10,13,16])
def test_get_longest_sum_is_prime():
    assert(get_longest_sum_is_prime([1,2,3,4])==[1,2])


if __name__=="__main__":
    test_get_longest_sum_is_prime()
    test_get_longest_arithmetic_progression()
    run()


