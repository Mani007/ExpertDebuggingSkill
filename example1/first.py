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
        elif c == '"' or c == "'" and tag_mode:
            quote_mode = not quote_mode
        elif not tag_mode:
            output += c
    return output

html_input1 = '<bold>somehting</bold>'
html_input2 = '<bold herf=">">somehting</bold>'
html_input3 = '"<bold>somehting</bold>"'  # some more buggy inputs , clearly fails the test
html_input4 = '<bold>"somehting"</bold>' # some more buggy inputs
html_input5 = '<"bold">somehting<"/bold">' # some more buggy inputs

parsed_output1 = html_parser(html_input1)
print(parsed_output1)
parsed_output2 = html_parser(html_input2)
print(parsed_output2)
parsed_output3 = html_parser(html_input3)
print(parsed_output3)
parsed_output4 = html_parser(html_input4)
print(parsed_output4)
parsed_output5 = html_parser(html_input5)
print(parsed_output5)
