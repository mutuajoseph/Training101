def totalMarks(math,eng,kiswa,ssr,sci):
    totalMarks = math+eng+kiswa+ssr+sci
    return totalMarks

def average(total):
    avg = total/5
    return avg

def findGrade(average):
    if average >= 80 and average <101:
        return "A"
    elif average >=70:
        return "B"
    elif average >=60:
        return "C"
    elif average >=50:
        return "D"
    else:
        return "E"

    return grade