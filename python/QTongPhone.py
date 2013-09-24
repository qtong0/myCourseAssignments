import re

def myPhoneTest(input_str):
    regex = r'^((\d)([ \-])?)?(\+1)?(\()?(\d{3})?(\))?([ \-\.])?(\d{3})([\-\. ])?(\d{4})$'
    p = re.compile(regex)
    match = re.search(p, input_str)
    if match:
        print "The phone number: \"" + input_str + "\" is valid!"
    else:
        print "The phone number: \"" + input_str + "\" is invalid!"
    return 0

if __name__ == '__main__':
    while True:
        input_str = raw_input("Please input a phone number(\"/quit\" to exit):\n")
        if input_str == "/quit":
            break
        else:
            myPhoneTest(input_str)