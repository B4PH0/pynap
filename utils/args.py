import argparse

def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('ip')
    parser.add_argument('-sT', action='store_true')
    global args
    args = parser.parse_args()
    return args.ip

def validar_st():
    if args.sT:
        return True
    else:
        return False
