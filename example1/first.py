# HTML parser 
# sample html input: <bold>somehting</bold>
# sample output: something
# Finite state machine as algo check the algo1.drawio file
def html_parser(s):
    tag = False
    output = ''
    for c in s: 
        if c == '<':
            tag = True
        elif c == '>':
            tag = False
        elif not tag:
            output += c
    return output

html_input = '<bold>somehting</bold>'

parsed_output = html_parser(html_input)
print(parsed_output)
