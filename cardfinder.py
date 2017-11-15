import re
import sys

def foundCard(line):
    print "[!] Potential card found/nRegex Match: "+line

def findCards(line):
    if re.match('\b(?:3[47]\d{2}([\ \-]?)\d{6}\1\d|(?:(?:4\d|5[1-5]|65)\d{2}|6011)([\ \-]?)\d{4}\2\d{4}\2)\d{4}\b', line) is not None:
        foundCard(line)
    elif re.match('(?:3[47]\d{2}([\ \-]?)\d{6}\1\d|(?:(?:4\d|5[1-5]|65)\d{2}|6011)([\ \-]?)\d{4}\2\d{4}\2)\d{4}', line) is not None:
        foundCard(line)
    elif re.match('(?ms)(.*)\b(?:4[0-9]{8}(?:[0-9]{3})?|5[1-5][0-9]{10}|6(?:011|5[0-9]{2})[0-9]{8}|3[47][0-9]{9}|3(?:0[0-5]|[68][0-9])[0-9]{7}|(?:2131|1800|35\d{3})\d{7})(\d{4}\b.*)', line) is not None:
        foundCard(line)
    elif re.match('\b3[47][0-9]{13}\b.', line) is not None:
        foundCard(line)
    elif re.match('\b(6541|6556)[0-9]{12}\b.', line) is not None:
        foundCard(line)
    elif re.match('\b389[0-9]{11}\b.', line) is not None:
        foundCard(line)
    elif re.match('\b3(?:0[0-5]|[68][0-9])[0-9]{11}\b.', line) is not None:
        foundCard(line)
    elif re.match('\b6(?:011|5[0-9]{2})[0-9]{12}\b.', line) is not None:
        foundCard(line)
    elif re.match('\b63[7-9][0-9]{13}\b.', line) is not None:
        foundCard(line)
    elif re.match('\b(?:2131|1800|35\d{3})\d{11}\b.', line) is not None:
        foundCard(line)
    elif re.match('\b9[0-9]{15}\b.', line) is not None:
        foundCard(line)
    elif re.match('\b(6304|6706|6709|6771)[0-9]{12,15}\b.', line) is not None:
        foundCard(line)
    elif re.match('\b(5018|5020|5038|6304|6759|6761|6763)[0-9]{8,15}\b.', line) is not None:
        foundCard(line)
    elif re.match('\b5[1-5][0-9]{14}\b.', line) is not None:
        foundCard(line)
    elif re.match('(?:5[1-5][0-9]{14})', line) is not None:
        foundCard(line)
    elif re.match('\b(6334|6767)[0-9]{12}|(6334|6767)[0-9]{14}|(6334|6767)[0-9]{15}\b.', line) is not None:
        foundCard(line)
    elif re.match('\b(4903|4905|4911|4936|6333|6759)[0-9]{12}|(4903|4905|4911|4936|6333|6759)[0-9]{14}|(4903|4905|4911|4936|6333|6759)[0-9]{15}|564182[0-9]{10}|564182[0-9]{12}|564182[0-9]{13}|633110[0-9]{10}|633110[0-9]{12}|633110[0-9]{13}\b.', line) is not None:
        foundCard(line)
    elif re.match('\b4[0-9]{12}(?:[0-9]{3})?\b.', line) is not None:
        foundCard(line)
    elif re.match('\b(?:3[47]\d{2}([\ \-]?)\d{6}\1\d|(?:(?:4\d|5[1-5]|65)\d{2}|6011)([\ \-]?)\d{4}\2\d{4}\2)\d{4}\b', line) is not None:
        foundCard(line)
    elif re.match('(?:3[47]\d{2}([\ \-]?)\d{6}\1\d|(?:(?:4\d|5[1-5]|65)\d{2}|6011)([\ \-]?)\d{4}\2\d{4}\2)\d{4}', line) is not None:
        foundCard(line)
    elif re.match('\b(62[0-9]{14,17})\b.', line) is not None:
        foundCard(line)
    elif re.match('\b(4[0-9]{14,17})\b.', line) is not None:
        foundCard(line)
    elif re.match('(4[0-9]{14,17})', line) is not None:
        foundCard(line)
    elif re.match('((?<!\.)4[0-9]{14,17})', line) is not None:
        foundCard(line)
    elif re.match('\b(?:4[0-9]{12}(?:[0-9]{3})?|5[1-5][0-9]{14})\b.', line) is not None:
        foundCard(line)
    elif re.match('^4[0-9]{12}(?:[0-9]{3})?$', line) is not None:
        foundCard(line)
    elif re.match('(0200[0-9]{43})(4[0-9]{12}(?:[0-9]{3}))', line) is not None:
        foundCard(line)
    elif re.match('^4\d{3}([\ \-]?)\d{4}\1\d{4}\1\d{4}$', line) is not None:
        foundCard(line)

if __name__ == "__main__":
    with open(sys.argv[1]) as fp:
        for line in fp:
            findCards(line)
