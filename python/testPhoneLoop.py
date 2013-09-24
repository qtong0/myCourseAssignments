import QTongPhone

if __name__ == '__main__':
    f = open('testPhones.txt', 'r')
    for line in f:
        newline = line.rstrip()
        QTongPhone.myPhoneTest(newline)