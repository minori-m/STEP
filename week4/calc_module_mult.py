def readNumber(line, index):
    number = 0.0
    keta = 0.1
    while index < len(line) and line[index].isdigit():
        number = number * 10 + int(line[index])
        index += 1
    if index < len(line) and line[index] == '.':
        index += 1
        while index < len(line) and line[index].isdigit():
            number = number + float(line[index])*keta
            index += 1
            keta *= 0.1
    token = {'type': 'NUMBER', 'number': number}

    return token, index


def readPlus(line, index):
    token = {'type': 'PLUS'}
    return token, index + 1

def readMinus(line, index):
    token = {'type': 'MINUS'}
    return token, index + 1

def readMult(line, index):
    token = {'type': 'MULT'}
    return token, index + 1

def readOver(line, index):
    token = {'type': 'OVER'}
    return token, index + 1

def tokenize(line):
    """
        Tokenize the input line and return a list of tokens
        """
    tokens = []
    index = 0
    while index < len(line):
        if line[index].isdigit():
            (token, index) = readNumber(line, index)
        elif line[index] == '+':
            (token, index) = readPlus(line, index)
        elif line[index] == "-":
            (token, index) = readMinus(line,index)
        elif line[index] == "*":
            (token, index) = readMult(line,index)
        elif line[index] == "/":
            (token, index) = readOver(line,index)
        else:
            print 'Invalid character found: ' + line[index]
            exit(1)
        tokens.append(token)
    return tokens



def evaluate(tokens):
    """
        Evaluate the list of tokens and return a calculated result
        """
    answer = 0
    tokens.insert(0, {'type': 'PLUS'}) # Insert a dummy '+' token
    index = 1
    while index < len(tokens):
        if tokens[index]['type'] == 'NUMBER':
            if tokens[index - 1]['type'] == 'PLUS':
                answer += float(tokens[index]['number'])
            elif tokens[index - 1]['type'] == 'MINUS':
                answer -= float(tokens[index]['number'])
            else:
                print 'Invalid syntax 1'
        index += 1
    return answer

"""Evaluate multiply and over earier than plus and minus"""
def multover(tokens):
    index = 0
    while index < len(tokens):
        if tokens[index]['type'] == 'MULT':
            if tokens[index-1]['type'] == 'NUMBER' and tokens[index+1]['type'] == 'NUMBER':
                tokens[index-1]['number'] *= float(tokens[index+1]['number'])
                tokens=cut(tokens,index,index+1)
            else:
                print'Invalid syntax 2'
        elif tokens[index]['type'] == 'OVER':
            if tokens[index-1]['type'] == 'NUMBER' and tokens[index+1]['type'] == 'NUMBER':
                tokens[index-1]['number'] /= float(tokens[index+1]['number'])
                tokens=cut(tokens,index,index+1)
            else:
                print'Invalid syntax 3'
        index += 1
    return tokens

"""shorten the tokens after multiply and over"""
def cut(tokens,a,b):
    token1=tokens[:a]
    token2=tokens[b+1:]
    tokens=token1+token2
    return tokens


while True:
    print '> ',
    line = raw_input()
    tokens = tokenize(line)
    tokens = multover(tokens)
    answer = evaluate(tokens)
    print "answer = %s\n" % float(answer)
