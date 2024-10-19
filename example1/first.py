# HTML parser 
# sample html input: <bold>somehting</bold>
# sample output: something
# Finite state machine as algo check the algo1.drawio file
def html_parser(s):
    tag_mode = False
    quote_mode = False
    output = ''
    for c in s: 
        if c == '<' and not quote_mode:
            tag_mode = True
        elif c == '>' and not quote_mode:
            tag_mode = False
        elif c == '"' or c == "'":
            quote_mode = not quote_mode
        elif not tag_mode:
            output += c
    return output

html_input1 = '<bold>somehting</bold>'
html_input2 = '<bold herf=">">somehting</bold>'

parsed_output1 = html_parser(html_input1)
print(parsed_output1)
parsed_output2 = html_parser(html_input2)
print(parsed_output2)
