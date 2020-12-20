def FindRelation(record1, record2):
    if(record1.Start < record2.Start):
        # Before
        if (record1.End < record2.Start):
            return 'b'

        # Meets
        elif (record1.End == record2.Start):
            return 'm'

        # Overlaps
        elif(record1.End > record2.Start and record1.End < record2.End):
            return 'o'

        # Finishes
        elif(record1.End == record2.End):
            return 'f'

        # Contains
        elif(record1.End > record2.End):
            return 'c'

    elif(record1.Start == record2.Start):
        # Equals
        if(record1.End == record2.End):
            return 'e'

        # Starts
        elif(record1.End < record2.End):
            return 's'
    else:
        # Error
        return "X"
