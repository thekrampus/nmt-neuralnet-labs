#!/usr/bin/python2
#
# Noisy Data Generator
# author: Rob K
# For use with Neural Nets project 1.
#
# Given an input "prototype" vector, this script produces a distorted image by
# applying additive white pseudorandom binary noise. This can be used to produce
# a set of independently noisy vectors.
#
# For example:
#   $ ./noisy_data.py -n 100 -p 0.05 a_24x24.dat
# The above invocation will create 100 distorted versions of a_24x24.dat (named
# a_24x24.dat.1, a_24x24.dat2, ...), where each bit of the input vector has a
# 5% probability of being flipped.
#
# To clean up the above command:
#   $ rm a_24x24.dat.*
#

from random import random
import argparse

def add_noise(proto, p):
    return [map(lambda b: b if random() > p else not b, r) for r in proto]

def parse_input(filename):
    with open(filename, 'r') as f:
        v = [[c == '1' for c in line.split()] for line in f]
    return v

def write_output(filename, vector):
    form = [' '.join(['1' if b else '0' for b in r]) + '\n' for r in vector]
    with open(filename, 'w') as f:
        f.writelines(form)

def main():
    parser = argparse.ArgumentParser(description = 'Adds random noise to '
                                    'the input vector.')
    parser.add_argument('filename', type = str, 
                        help = 'prototype vector to distort')
    parser.add_argument('-n', dest = 'number', type = int, default = 1,
                        help = 'number of noisy vectors to generate')

    def probability(p):
        p = float(p)
        if p < 0.0 or p > 1.0:
            raise argparse.ArgumentTypeError("%r out of range [0, 1]"%(p,))
        return p
    parser.add_argument('-p', dest = 'prob', type = probability, default = 0.1,
                        help = 'distortion probability (0 <= p <= 1)')
    
    args = parser.parse_args()

    proto = parse_input(args.filename)

    for n in range(1, args.number + 1):
        noisy = add_noise(proto, args.prob)
        write_output(args.filename + '.' + str(n), noisy)
    
if __name__ == '__main__':
    main()
