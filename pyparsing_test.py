from pyparsing import Word, Suppress, nums

survey = '''GPS,PN1,LA52.125133215643,LN21.031048525561,EL116.898812'''

number = Word(nums+'.').setParseAction(lambda t: float(t[0]))
separator = Suppress(',')
latitude = Suppress('LA') + number
longitude = Suppress('LN') + number
elevation = Suppress('EL') + number

line = (Suppress('GPS,PN1,')
        + latitude
        + separator
        + longitude
        + separator
        + elevation)

print (line.parseString(survey))