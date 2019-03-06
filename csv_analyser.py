import csv
import monster_dictionary


def csv_extractor(path):
    with open(path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter = ';')
        monster_names = []
        count_row = 0

        for row in csv_reader:
            count_row += 1 
            for x in range(len(row)):
                monster_name = row[x]
                monster_names.append(monster_name)
    
        monster_ID = [0 for x in range(len(row))]
    for x in range(len(row)):
        monster_ID[x] = monster_dictionary.monster(monster_names[27*x], monster_names[27*x + 1], monster_names[27*x + 2], monster_names[27*x + 3], monster_names[27*x + 4], monster_names[27*x + 5], monster_names[27*x +6], monster_names[27*x +7], monster_names[27*x +8], monster_names[27*x + 9], monster_names[27*x +10], monster_names[27*x +11], monster_names[27*x + 12], monster_names[27*x + 13], monster_names[27*x + 14], monster_names[27*x + 15], monster_names[27*x + 16], monster_names[27*x + 17], monster_names[27*x + 18], monster_names[27*x + 19], monster_names[27*x + 20], monster_names[27*x + 21], monster_names[27*x + 22], monster_names[27*x + 23], monster_names[27*x + 24], monster_names[27*x + 25], monster_names[27*x + 26])
    return monster_ID

