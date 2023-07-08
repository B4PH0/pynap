import argparse

def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('ip')
    parser.add_argument('-sT')
    args = parser.parse_args()
    return args.ip
