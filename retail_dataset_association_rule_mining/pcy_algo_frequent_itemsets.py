# -*- coding: utf-8 -*-
# Lab 3: PCY Algorithm for Frequent Itemset Mining
# Author: Dylan Rapanan, Danial Saber, Winter 2024

# NOTE: You may use any Python library you want to complete this lab. 
# However you cannot use any library that implements the PCY algorithm. 

# NOTE: You may not change the name of any of the functions or their arguments lest you tempt the autograder,
# however you may add as many additional helper functions as you like.

# NOTE: You may assume that all items in the dataset are integers.
# You may also assume that the dataset is a list of lists, where each list is a transaction.

import urllib.request
import itertools as it
from collections import defaultdict

# Load the retail dataset from the URL, this will be used in lab 4, not lab 3
def load_data_from_url(url):
    response = urllib.request.urlopen(url)
    lines = response.readlines()
    dataset = [list(map(int, line.strip().split())) for line in lines]
    return dataset


# Hash function for PCY algorithm, do not modify this, should be used in the pcy_algorithm function
def hash_function(pair, num_buckets):
    i, j = pair
    hash_value = ((i * num_buckets) + j) % num_buckets
    return hash_value


# Implement the PCY algorithm for frequent itemset mining
# dataset: A list of lists, where each list is a transaction
# min_support: The minimum support threshold for an itemset to be considered frequent
# hash_buckets: The number of buckets to use for the hash table
# Returns: A list of lists, where each list is a frequent itemset
def pcy_algorithm(dataset, min_support, hash_buckets) -> list:
    
    frequent_items = []
    
    # TODO: Implement the PCY algorithm
    
    # Pass 1: counting singletons and hashing pairs to buckets
    # each pair will be sorted in order to maintain consistent hashing for out of order pairs
    C1 = defaultdict(int)
    buckets = defaultdict(int)

    for basket in dataset:
        
        for i in basket:
            C1[i] += 1
            
        for p in it.combinations(basket,2):
            buckets[hash_function(sorted(p),hash_buckets)] += 1
    
    
    
    # Pruning C1 to create L1 for singletons
    # converting buckets to a bit-vector
    items = tuple(C1)
    
    for i in items:
        if C1[i] < min_support:
            del C1[i]
    
    # L1 is mapping of frequent singletons frequent singletons
    L1 = C1
    for i in L1:
        frequent_items.append([i])

    # converting buckets to a bit vector
    bitvector = 0
    for x in buckets:
        if buckets[x] >= min_support:
            bitvector |= (1 << x)
    del buckets
    
    
    # Pass 2: Generating C2 using L1 and bit vector to reduce candidate pair list
    C2 = defaultdict(int)
    
    for basket in dataset:
    
        for p in it.combinations(basket,2):
    
            p = tuple(sorted(p))
            bucket_num = hash_function(p, hash_buckets)
    
            if( (p[0] in L1) and (p[1] in L1) and (bitvector & (1 << bucket_num))):
                C2[p] += 1
                
                
                
    # Appending all frequent candidate pairs
    for p in C2:
        frequent_items.append(list(p))

    return frequent_items

# Modify the following main method as needed, this is just to help you test your PCY function
if __name__ == "__main__":
    dataset = [
        [1, 2, 3],
        [4, 5],
        [1, 4, 5],
        [1, 2, 4],
        [3, 4, 5],
        [2, 4, 5]
    ]

    min_support = 2
    hash_buckets = 10

    frequent_items = pcy_algorithm(dataset, min_support, hash_buckets)

    for item in frequent_items:
        print(item)

# Expected output:        
# [1]
# [2]
# [3]
# [4]
# [5]
# [1, 2]
# [1, 3]
# [2, 3]
# [4, 5]
# [1, 5]
# [3, 5]
# [2, 5]
# [1, 4]
# [2, 4]
# [3, 4]
