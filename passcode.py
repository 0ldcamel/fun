import itertools
cond1 = [6, 8, 2] # 1 number correct and well placed
cond2 = [6, 1, 4] # 1 number wrongly placed
cond3 = [2, 0, 6] # 2 numbers wrongly placed
cond4 = [7, 3, 8] # nothing is correct
cond5 = [7, 8, 0] # 1 number wrongly placed

def main():
    permutations = [list(permu) for permu in itertools.permutations(list(range(10)), 3)]
    print('Number of possible permutations before purging     :',len(permutations))
    correct_number, correct_index = test_well_placed()

    purge_cond1(correct_number, correct_index, permutations)
    print('Number of possible permutations after purging cond1:',len(permutations))

    test_wrongly_placed(cond2, permutations, 1)
    print('Number of possible permutations after purging cond2:',len(permutations))

    test_wrongly_placed(cond3, permutations, 2)
    print('Number of possible permutations after purging cond3:',len(permutations))

    test_wrongly_placed(cond4, permutations, 0)
    print('Number of possible permutations after purging cond4:',len(permutations))

    test_wrongly_placed(cond5, permutations, 1)
    print('Number of possible permutations after purging cond5:',len(permutations))

    for password in permutations:
        print('The password is',password)


def test_well_placed():
    for i in range(3):
        others_numbers = set([cond2[i], cond3[i], cond5[i]] + cond4)
        if cond1[i] in others_numbers:
            pass
        else:
            correct_number, correct_index = cond1[i], i
    return correct_number, correct_index

def purge_cond1(correct_number, correct_index, permutations):
    permu_copy = permutations[:]
    for permu in permu_copy:
        if permu[correct_index] != correct_number:
            permutations.remove(permu)
        
def test_wrongly_placed(cond, permutations, quantity):
    permu_copy = permutations[:]
    for permu in permu_copy:
        if len(set(cond) & set(permu)) != quantity:
            permutations.remove(permu)
    permu_copy = permutations[:]
    for i in range(3):
        for permu in permu_copy:
            if permu[i] == cond[i]:
                permutations.remove(permu)

    return permutations

main()
