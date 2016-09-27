from __future__ import print_function
import os
import sys


class Solution(object):
    def __init__(self, ads):
        self.ads = ads

    def shuffle(self):
        """ Python implementation of the Durstenfeld shuffle algorithm. It is
        an O(n) time in-place shuffle algorithm similar to the earlier
        Fisher-Yates algorithm. It has been proven that this algorithm yields
        a uniformly shuffled list because the set of all states constitutes a 
        cycle, there are no subcycles, and there is no set of states that occur 
        more or less frequently than others. It is also the algorithm 
        implemented by random.shuffle.
        """
        for i in range(1, len(self.ads)):
            j = self.urandrange(i + 1)
            self.ads[i], self.ads[j] = self.ads[j], self.ads[i]

    def solve(self, k):
        """ First checks to make sure len(ads) >= k, throws ValueError 
        otherwise. Shuffles the ads and returns a slice of the ads k-long.
        :param k: number of ads to return
        :return list: the first k ads in our shuffled input list
        """
        if k > len(self.ads):
            raise ValueError("K is larger than the number of ads")
        
        self.shuffle()
        return self.ads[:k]

    @staticmethod
    def urandrange(n):
        """ Homemade random number generator. Importing from random felt 
        too easy. Also, why be random when you can be urandom?
        :return int: 0 <= a random integer < n
        """
        return ord(os.urandom(1)) % n


if __name__ == "__main__":
    try:
        # Expects path to input file and an integer, k
        input_file, k = sys.argv[1:]
        k = int(k)
    except ValueError as e:
        print("Check parameters and try again.\n"
              "Usage: python solution.py <input_file> <k>")
        sys.exit(1)

    with open(input_file) as f:
        ads = f.readlines()
    
    sln = Solution(ads)
    for line in sln.solve(k):
        print(line.strip())

