if __name__ == '__main__':
    import grade

    grades = [grade.NumericGradeEntry('csc148', 87, 0.5),
              grade.NumericGradeEntry('mat137', 76, 1.0),
              grade.LetterGradeEntry('his450', 'B+', 0.5)]

    for g in grades:
        # Use appropriate ??? methods or attributes of g in format
        print("Weight: {}, grade: {}, points: {}".format(g.weight, g.grade, g.points))
    # Use methods or attributes of g to compute weight times points
    total = sum(            # sum of the list of...
        [g.points * g.weight # methods or attributes of g
    for g in grades]) # using each g in grades
    # sum up the credits
    total_weight = sum([g.weight for g in grades])
    print("GPA = {}".format(total / total_weight))
