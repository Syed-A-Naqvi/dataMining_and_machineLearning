
# -*- coding: utf-8 -*-
# Lab 1-2: Apriori Algorithm for Frequent Itemset Mining and Association Rules
# Author: Dylan Rapanan, Danial Saber, Winter 2024

# NOTE: You may use any Python library you want to complete this lab. 
# However you cannot use any library that implements the Apriori algorithm or association rule mining.

# NOTE: You may not change the name of any of the functions or their arguments lest you tempt the autograder,
# however you may add as many additional helper functions as you like.

# NOTE: You may assume that all items in the dataset are integers.
# You may also assume that the dataset is a list of lists, where each list is a transaction.


# importing libraries
import itertools as it
from collections import defaultdict

# global count storage dictionary
set_counts = {}

# Implement the Apriori algorithm for frequent itemset mining
# dataset: A list of lists, where each list is a transaction
# min_support: The minimum support threshold for an itemset to be considered frequent
# Returns: A list of lists, where each list is a frequent itemset
def apriori(dataset, min_support) -> list:

    # TODO: Implement the Apriori algorithm
    
    # Pass 1: recording singleton support in dictionary
    # This generates C1
    C1 = defaultdict(int)
    for basket in dataset:
        for item in basket:
            C1[tuple((item,))] += 1
    
    
    # Pruning C1: removing infrequent singletons from dictionary
    # this generates L1
    items = tuple(C1)
    # if the item count is less than support, entry is removed from dictionary
    for item in items:
        if C1[item] < min_support:
            del C1[item]
    # defining frequent itemset map as L1
    L1 = C1
    # appending list of frequent singletons to frequent_sets
    set_counts.update(L1)
    
    
    # Generating candidate item pairs for C2 using singletons in L1
    frequent_singletons = [i for s in L1 for i in s]
    pairs = it.combinations(frequent_singletons,2)
    # initializing C2 with candidates
    C2 = {}
    for pair in pairs:
        C2[tuple(sorted(pair))] = 0


    # Pass 2: finding support of all candidate item pairs in C2
    for basket in dataset:
        for pair in it.combinations(basket,2):
            pair = tuple(sorted(pair))
            if pair in C2:
                C2[pair] += 1

    
    # Pruning: removing all infrequent item pairs from C2
    # this will generate L2
    pairs = tuple(C2)
    for pair in pairs:
        if C2[pair] < min_support:
            del C2[pair]
    L2 = C2
    # appending list of frequent pairs to frequent_sets
    set_counts.update(L2)
    
    
    # generating candidate item triples for C3 using singletons in L2
    frequent_singletons = [i for s in L2 for i in s]
    triples = it.combinations(frequent_singletons, 3)
    # populating C3 with candidate triples
    C3 = {}
    for t in triples:
        t = tuple(sorted(t))
        C3[t] = 0
    
    
    # Initial Prune of C3: will remove all triples containing infrequent pairs (pairs not in L2)
    for t in triples:
        for p in it.combinations(t, 2):
            p = tuple(sorted(p))
            if p not in L2:
                del C3[t]
                break
    
    
    # Pass 3: counting support for all triples
    for basket in dataset:
        for t in it.combinations(basket, 3):
            t = tuple(sorted(t))
            if t in C3:
                C3[t] += 1
    
    
    # Pruning C3 to remove infrequent triples
    # this generates L3
    triples = tuple(C3)
    for t in triples:
        if C3[t] < min_support:
            del C3[t]
    L3 = C3
    # appending list of frequent triples to frequent_sets
    set_counts.update(L3)
    
    frequent_sets = []
    for s in set_counts:
        frequent_sets.append(list(s))
    
    return frequent_sets

# Implement the generation of association rules from frequent itemsets
# dataset: A list of lists, where each list is a transaction
# frequent_sets: A list of lists, where each list is a frequent itemset, this is the output of the apriori function
# min_confidence: The minimum confidence threshold for a rule to be considered interesting
# Returns: A list of tuples, where each tuple is a rule of the form (antecedent, consequent)
# i.e ([1], [3, 5]) means 1 -> 3, 5
def generate_association_rules(dataset, frequent_sets, min_confidence) -> list:
    rules = []

    # TODO: Implement the association rule generation
    
    for itmset in frequent_sets:
        
        for r in range(1, len(itmset)):
            
            for A in it.combinations(itmset,r):

                antecedent = set(A)
                consequent = set(itmset) - antecedent
                confidence = set_counts[tuple(itmset)] / set_counts[tuple(sorted(antecedent))]

                if (confidence >= min_confidence):

                    rules.append((list(antecedent), list(consequent)))

    return rules

if __name__ == "__main__":
    dataset = [[1, 3, 4],
               [2, 3, 5],
               [1, 2, 3, 5],
               [2, 5],
               [1, 3, 5]]
    
    min_support = 2  # Adjust the minimum support threshold as needed

    frequent_sets = apriori(dataset, min_support)

    print("Frequent Itemsets:")
    for itemset in frequent_sets:
        print(itemset)

    min_confidence = 0.6  # Adjust the minimum confidence threshold as needed
    association_rules = generate_association_rules(dataset, frequent_sets, min_confidence)

    print("\nAssociation Rules:")
    for rule in association_rules:
        print(rule)

    # Expected output when both functions are correct and min_support = 2 and min_confidence = 0.6:
    # Frequent Itemsets:
    # [1]
    # [2]
    # [3]
    # [5]
    # [1, 3]
    # [1, 5]
    # [2, 3]
    # [2, 5]
    # [3, 5]
    # [1, 3, 5]
    # [2, 3, 5]

    # Association Rules:
    # ([1], [3])
    # ([3], [1])
    # ([1], [5])
    # ([2], [3])
    # ([2], [5])
    # ([5], [2])
    # ([3], [5])
    # ([5], [3])
    # ([1], [3, 5])
    # ([1, 3], [5])
    # ([1, 5], [3])
    # ([3, 5], [1])
    # ([2], [3, 5])
    # ([2, 3], [5])
    # ([2, 5], [3])
    # ([3, 5], [2])