import math

import argparse


parser= argparse.ArgumentParser(description='Calcuating the volume of a cube') 
parser.add_argument('--length', type = int)
parser.add_argument('--height', type = int)
parser.add_argument('--breadth', type = int)
args = parser.parse_args()


def volume_cube(length, breadth, height):
    volume = length * breadth * height
    return volume


if __name__ == "__main__":
    print(volume_cube(args.length, args.height,args.breadth))
