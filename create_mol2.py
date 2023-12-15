import numpy as np
import argparse

parser = argparse.ArgumentParser(description="Create a single chain in mol2 format")
parser.add_argument("-l", "--chain_len", type=int, default=100, help="Chain length")
parser.add_argument(
    "-o", "--out_path", type=str, default="./chain.mol2", help="Chain length"
)
out = open(parser.parse_args().out_path, "w")
out.write("@<TRIPOS>MOLECULE\n")
out.write("mol_name\n")
out.write(
    f"\t{parser.parse_args().chain_len}\t{parser.parse_args().chain_len - 1}\t0\t0\t0\n"
)
out.write("SMALL\n")
out.write("USER_CHARGES\n")
out.write("@<TRIPOS>ATOM\n")
for i in range(parser.parse_args().chain_len):
    out.write(
        f"{i+1} 	 C 	 {np.random.rand()} 	 {np.random.rand()} 	 {np.random.rand()} 	 C 	 1  ala 	 1.000000\n"
    )
out.write("@<TRIPOS>BOND\n")
for i in range(1, parser.parse_args().chain_len):
    out.write(f"{i}\t{i}\t{i+1}\t1\n")
out.close()
