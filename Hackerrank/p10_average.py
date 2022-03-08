if __name__ == '__main__':
    n = int(input())
    student_marks = {}

    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    average = 0
    # print(average)

    if query_name in student_marks:
        scores = student_marks.get(query_name)
        for score in scores:
            average = average + score
        average = average/len(scores)
    two_decimal_avg = "{:.2f}".format(average)

    print(two_decimal_avg)