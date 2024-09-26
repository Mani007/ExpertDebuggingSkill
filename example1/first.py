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

html_input1 = '<bold>somehting</bold>'
html_input2 = '<bold herf=">">somehting</bold>'

parsed_output1 = html_parser(html_input1)
print(parsed_output1)
parsed_output2 = html_parser(html_input2)
print(parsed_output2)
