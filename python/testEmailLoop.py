import QTongEmail

if __name__ == '__main__':
    f = open('testEmails.txt', 'r')

    for line in f:
        newline = line.rstrip()
        tmpdict = QTongEmail.parse_email(newline)
        if tmpdict:
            print '{0:45} ==> {1:30s}'.format(newline, tmpdict)
        else:
            print '{0:45} ==> {1:30s}'.format(newline, 'Invalid Email!')