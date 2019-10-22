import argparse
import numpy as np
import timeit

import os
import sys

# to make sure relative import works
# for a detailed explanation, see test_matchmaker.py

current_script_path = sys.argv[0]
package_home_path = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..'))
if package_home_path not in sys.path:
    sys.path.append(package_home_path)

import pyteiser.glob_var as glob_var
import pyteiser.structures as structures
import pyteiser.IO as IO
import pyteiser.representation as representation



def handler():
    parser = argparse.ArgumentParser()
    parser.add_argument("--seeds_bin_file", type=str)

    parser.set_defaults(
        seeds_bin_file = '/Users/student/Documents/hani/programs/pyteiser/data/combined_optimized_seeds/tarbp2/seed_optimized_100k_tarbp2_utrs_10k.bin',
    )

    args = parser.parse_args()

    return args


def test_representation(w_motif):
    pwm = representation.generate_PWM_from_motif(w_motif)

    # w_motif.print()
    # print(pwm)



def main():
    args = handler()

    w_motifs_list = IO.read_motif_file(args.seeds_bin_file)

    test_representation(w_motifs_list[0])



if __name__ == "__main__":
    main()