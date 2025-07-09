from ds.stack import Stack

def is_pair(symbol_string):
    s = Stack()
    paired = True
    index = 0
    while index < len(symbol_string) and paired:
        symbol = symbol_string[index]
        if symbol in '([{':
            s.push(symbol)
        else:
            if s.empty():
                paired = False
            else:
                top = s.pop()
                if not match_pair(top, symbol):
                    paired = False

        index += 1

    if s.empty() and paired:
        return True
    else:
        return False

def match_pair(open_symbol, close_symbol):
    opens = "([{"
    closes = ")]}"
    return opens.index(open_symbol) == closes.index(close_symbol)


if __name__ == '__main__':
    print(is_pair("[{{]}]"))
    print(is_pair("[{{}}]"))
    print(is_pair("()(((())))"))