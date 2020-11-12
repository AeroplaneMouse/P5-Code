def FindRelation(record1, record2):
    if(record1.Start < record2.Start):
        if (record1.End < record2.Start):
            return 'b'
        elif (record1.End == record2.Start):
            return 'm'
        elif(record1.End > record2.Start and record1.End < record2.End):
            return 'o'
        elif(record1.End == record2.End):
            return 'f'
        elif(record1.End > record2.End):
            return 'c'
    elif(record1.Start == record2.Start):
        if(record1.End == record2.End):
            return 'e'
        elif(record1.End < record2.End):
            return 's'
    else:
        return "X"
