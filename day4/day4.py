# --- Day 4: The Ideal Stocking Stuffer ---
# Santa needs help mining some AdventCoins (very similar to bitcoins) to use as gifts for all the economically forward-thinking little girls and boys.
#
# To do this, he needs to find MD5 hashes which, in hexadecimal, start with at least five zeroes.
# The input to the MD5 hash is some secret key (your puzzle input, given below) followed by a number in decimal.
# To mine AdventCoins, you must find Santa the lowest positive number (no leading zeroes: 1, 2, 3, ...) that produces such a hash.
#
# For example:
#
# If your secret key is abcdef, the answer is 609043, because the MD5 hash of abcdef609043 starts with five zeroes (000001dbbfa...), and it is the lowest such number to do so.
# If your secret key is pqrstuv, the lowest number it combines with to make an MD5 hash starting with five zeroes is 1048970; that is, the MD5 hash of pqrstuv1048970 looks like 000006136ef....
# Your puzzle input is iwrupvqb.
#

# so, there is, without a doubt, a python library for this..
# and there is.. hashlib..
import hashlib


def hash_for_key(the_data: str) -> str:
    """
    Return the MD5 hex digest for the data provided
    """
    hasher = hashlib.md5()
    hasher.update(the_data.encode("utf-8"))
    hex_digest = hasher.hexdigest()
    return hex_digest


def find_lowest_matching_hash_for_key(
    the_base: str, desired_hash_prefix: str = "00000"
) -> int:
    """
    Return the lowest non-negative integer where the md5 hash of the_base+str(i) starts with desired_hash_prefix
    """
    i = 0
    while not hash_for_key(the_base + str(i)).startswith(desired_hash_prefix):
        i += 1

    return i


# main
if __name__ == "__main__":
    data = "iwrupvqb"
    part1 = find_lowest_matching_hash_for_key(data, desired_hash_prefix="00000")
    part2 = find_lowest_matching_hash_for_key(data, desired_hash_prefix="000000")
    print(f"md5 for [{data}] part1=[{part1}], part2=[{part2}]")
