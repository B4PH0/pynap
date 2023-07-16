import argparse

def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('ip')
    args = parser.parse_args()
    global internet_protocol
    internet_protocol = args.ip
    return internet_protocol
