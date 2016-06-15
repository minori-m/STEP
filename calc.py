while True:
    print '> ',
    line = raw_input()
    answer = 0
    index = 0
    operation="+"
    
    
    while index < len(line):
        if line[index].isdigit() :
            number = 0
            a=0.1
            while index < len(line) and (line[index].isdigit() or line[index] == ".") :
                while index < len(line) and line[index].isdigit()
                    number = number * 10 + int(line[index])
                    index += 1
                if index < len(line) and line[index] == ".2:
                    index += 1
                    while len(line) and line[index].isdigit()
                        number = number + line[index]*a
                        a *=0.1
                        index += 1
            if operation == "+"
                answer +=number
            elif operation == "-"
                answer -= number
    
        elif line[index] == '+':
            index += 1
            operation ="+"
        elif line[index] == "-":
            index += 1
            operation = "-"
        else:
            print 'Invalid character found: ' + line[index]
            exit(1)
    print "answer = %d\n" % answer

