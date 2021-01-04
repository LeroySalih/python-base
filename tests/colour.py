def green(msg):
    green = u"\u001b[32m" 
    reset = u'\u001b[0m'
    return f"{green}{msg}{reset}"

def red(msg):
    red = u'\u001b[31m' 
    reset = u'\u001b[0m'
    return f"{red}{msg}{reset}"
    