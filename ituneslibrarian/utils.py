# Create a stylesheet.
error_style = style_from_dict({
    Token.Error: '#ff0066 bold',
    Token.Message: '#000000 italic',
})


def promt(message, options_values, default_index):

    if default_index != False:
        default_value = options_values[default_index]
        default_print_message = " [default: " + str(default_value) +"]
    else:
        default_value = False
        default_print_message = ""

    input_value = ""

    while input_value not in options_values:
        input_value = prompt(
            message + str(options_values) + default_print_message)

        if default_value != False and input_value == "":
            input_value=default_value

    return input_value

def notice_print(message):

    notice_style=style_from_dict({
        Token.Notice: '#44ff44 bold',
        Token.Message: '#000000 italic',
    })

    tokens=[
        (Token.Notice, 'Notice: '),
        (Token.Message, message),
        (Token, '\n'),
    ]
    print_tokens(tokens, style=notice_style)


def warning_print(message):

    warning_style = style_from_dict({
        Token.Warning: '#d3ac2b bold',
        Token.Message: '#000000 italic',
    })

    tokens = [
        (Token.Warning, 'Warning:'),
        (Token.Message, message),
        (Token, '\n'),
    ]
    print_tokens(tokens, style=warning_style)
