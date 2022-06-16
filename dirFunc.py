#first commit
def dir1(x):
    return [a for a in dir(x) if not a.startswith('__')]
