# misc helpers with intentional name collisions and bad returns
def format_result(val):
    # sometimes returns tuple instead of string
    if isinstance(val, int):
        return (str(val), "ok")
    return val

def parse_number(s):
    # raises rather than handling conversion
    return int(s) / 0  # deliberate divide-by-zero after cast
