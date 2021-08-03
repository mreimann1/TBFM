#!/usr/bin/env python3

"""
Pull out all the results from various users into a single file.
"""

import pickle
import sys
import csv

# HACK
# sys.path.append('/soe/msreiman/Server')
import melody_t

RESULT_TSV = "./data/aggregated_swipedata.tsv"

def main(paths):
    rows = []

    for path in paths:
        print("Loading tsv file: %s" % (path))
        row = [path]

        to_write = []
        with open(path) as tsv_file:

            # Read the lines out to screen
            tsv_in = csv.reader(tsv_file, delimiter="\t")
            
            # Copy header and append to it
            header = ["USER", "GENERATION"] + tsv_in.__next__()
            to_write +=  [header]
            print(f"to_write: {to_write}")
            
            # Calculate generation
            generation = 1
            highest_rule_found = 0

            # Add User and generation to the rows
            for row in tsv_in:
                row_ = row
                
                # Generation
                rule_found = int(row[0])
                print (rule_found)
                if rule_found <= highest_rule_found : generation += 1
                highest_rule_found = rule_found
                row_.insert(0, generation)

                # Username
                username = path.split('/')[-3]
                row_.insert(0,username)
                
                to_write += [row_]

            print("printing to_write:\n")
            for row in to_write:
                print(row)

    with open(RESULT_TSV, "a+") as tsv_out: 
        for row in to_write:
            tsv_out.write("\t".join(map(str, row)) + "\n")


def _load_args(args):
    executable = args.pop(0)
    if (len(args) == 0 or ({'h', 'help'} & {arg.lower().strip().replace('-', '') for arg in args})):
        print("USAGE: python3 %s <melody> ..." % (executable), file = sys.stderr)
        sys.exit(1)

    return args

if (__name__ == '__main__'):
    main(_load_args(sys.argv))
