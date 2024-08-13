import itertools
cond1 = [6, 8, 2] # 1 number correct and well placed
cond2 = [6, 1, 4] # 1 number wrongly placed
cond3 = [2, 0, 6] # 2 numbers wrongly placed
cond4 = [7, 3, 8] # nothing is correct
cond5 = [7, 8, 0] # 1 number wrongly placed

def main():
    permutations = [list(permu) for permu in itertools.permutations(list(range(10)), 3)]
    print('Number of possible permutations before conditions:',len(permutations))
    correct_number, correct_index = test_well_placed()

    purge_cond1(correct_number, correct_index, permutations)
    print('Number of possible permutations after applying condition 1:',len(permutations))
    wrongly_placed_list = [[cond2, 1], [cond3, 2], (cond4, 0), (cond5, 1)]
    i = 2
    for cond, quantity in wrongly_placed_list:
        test_wrongly_placed(permutations, cond, quantity)
        print(f'Number of possible permutations after applying condition {i}:',len(permutations))
        i += 1

    for password in permutations:
        print('-' * len(str(f'The password is: {password}')))
        print('The password is', password)
        print('-' * len(str(f'The password is: {password}')))


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
        
def test_wrongly_placed(permutations, cond, quantity):
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
