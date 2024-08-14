import itertools
# hint1 = [6, 8, 2] # 1 number correct and well placed
# hint2 = [6, 1, 4] # 1 number wrongly placed
# hint3 = [2, 0, 6] # 2 numbers wrongly placed
# hint4 = [7, 3, 8] # nothing is correct
# hint5 = [7, 8, 0] # 1 number wrongly placed

hint1 = [3, 4, 2] # 1 number correct and well placed
hint2 = [1, 4, 6] # 1 number wrongly placed
hint3 = [8, 7, 6] # 2 numbers wrongly placed
hint4 = [4, 7, 3] # nothing is correct
hint5 = [0, 6, 9] # 1 number wrongly placed

def main():
    permutations = [list(permu) for permu in itertools.permutations(list(range(10)), 3)]
    print('Number of possible permutations before conditions:',len(permutations))
    correct_number, correct_index = test_well_placed()

    purge_cond1(correct_number, correct_index, permutations) # purging incorrect numbers in cond1
    print('Number of possible permutations after applying condition 1:',len(permutations))

    wrongly_placed_list = [[hint2, 1], [hint3, 2], (hint4, 0), (hint5, 1)]
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
        others_numbers = set([hint2[i], hint3[i], hint5[i]] + hint4)
        if hint1[i] in others_numbers:
            pass
        else:
            correct_number, correct_index = hint1[i], i
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

if __name__ == '__main__':
    main()
