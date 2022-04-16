# https://www.hackerrank.com/challenges/nested-list/problem?isFullScreen=true


if __name__ == '__main__':
    all_values = []
    for _ in range(int(input('Enter no. of people '))):
        name = input('Enter name ')
        score = float(input('Enter score '))
        name_score_list = [name, score]
        all_values.append(name_score_list)

    lowest = None
    second_lowest = None
    for name_score in all_values:
        if not lowest or name_score[1] <= lowest:
            lowest = name_score[1]
            name = name_score[0]
        elif not second_lowest or name_score[1] <= second_lowest:
            second_lowest = name_score[1]
            name2 = name_score[0]
        else:
            print(f"Score {name_score[1]} is not lowest or seconds lowest... ignore!")

    print(f"Name of the student with second lowest score is '{name2}'. The score is '{second_lowest}'")







