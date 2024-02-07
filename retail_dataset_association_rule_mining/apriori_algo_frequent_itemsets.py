
# -*- coding: utf-8 -*-
# Lab 1-2: Apriori Algorithm for Frequent Itemset Mining and Association Rules
# Author: Dylan Rapanan, Danial Saber, Winter 2024

# NOTE: You may use any Python library you want to complete this lab. 
# However you cannot use any library that implements the Apriori algorithm or association rule mining.

# NOTE: You may not change the name of any of the functions or their arguments lest you tempt the autograder,
# however you may add as many additional helper functions as you like.

# NOTE: You may assume that all items in the dataset are integers.
# You may also assume that the dataset is a list of lists, where each list is a transaction.

# Implement the Apriori algorithm for frequent itemset mining
# dataset: A list of lists, where each list is a transaction
# min_support: The minimum support threshold for an itemset to be considered frequent
# Returns: A list of lists, where each list is a frequent itemset
def apriori(dataset, min_support) -> list:
    frequent_sets = []

    # TODO: Implement the Apriori algorithm

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