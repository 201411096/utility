import clipboard

log = clipboard.paste()

log = log.splitlines()

queryLine = log[0]
parameterLine = log[1]

queryLine = queryLine.split('Preparing: ')[1]
parameterLine = parameterLine.split('Parameters: ')[1]

parameterLine = parameterLine.split(', ')

for parameter in parameterLine:
    parameter = "'" + parameter.split('(')[0] + "'"
    queryLine = queryLine.replace('?', parameter, 1)

clipboard.copy(queryLine)
