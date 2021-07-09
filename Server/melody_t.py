# import
import random
from rules_l import *
from var_defs import *

# Rule Object
class Rule:
  def __init__(self, function):
    self.function = function
    self.likes = 1
    self.dislikes = 1
  def desirability(self):
    return (self.likes / self.dislikes)
  def leftswipe(self, dflag=False):
    self.likes += 1
    if dflag:
      print(f"Rule: {self}")
  def rghtswipe(self, dflag=False):
    self.dislikes += 1
    if dflag:
      print(f"Rule: {self}")
  def __str__(self):
    return f"likes: {self.likes}\tdislikes: {self.dislikes}\tdesirability: {self.desirability()}"

# List of Rules which can be selected for Melody instances
class Rules:  
  def __init__(self):
    self.rules = [Rule(rule1),
            Rule(rule2),
            Rule(rule3),
            Rule(rule4),
            Rule(rule5),
            Rule(rule6),
            Rule(rule7)]
  # Function for dumping rules to a file
  def dump_rules(self, filename):
    for i in range(0,len(self.rules)):
      f = open(filename, "a")
      f.write(f"Rule{i}: {self.rules[i]}\n")
      f.close()

# Define a Melody Object
class Melody:
  def __init__(self, index, rules_super) : #rules_super is the superset of rules
    self.notes = []
    self.rules_list = []
    self.index = index
    self.midi_path = ""
    self.rules = rules_super

  def print_rules(self, message="", and_desirability=False): # message added to help debug
    for rule in self.rules_list:
      print("rule:")
      rule.function(0,[], True)
      print(message)
      if and_desirability:
        print(f"has desirability: {rule.desirability()}")

  def generate_notes(self) :
    # Choose some rules
    num_rules = random.randint(3,5)
    self.rules_list = []
    self.rules_list = random.choices(self.rules, weights = [i.desirability() for i in self.rules], k=num_rules)
    # Use rules
    # loop until we have MELODY_LEN notes
    while len(self.notes) < MELODY_LEN:
      # generate a random note between 0 and 108
      new_note = random.randint(0,108)
      
      # test note with all rules in rules_list
      note_results = [rule.function(new_note, self.notes) for rule in self.rules_list]
          
      # does it pass ALL of the rules? append new_note to the melody
      if all(note_results):
        self.notes += [new_note]

  def handle_leftswipe(self, dflag=False) :
    if dflag: 
      print(f"Melody{self.index} was leftswiped")
      print(self.rules_list)
    for rule in self.rules_list:
        rule.leftswipe(dflag)

  def handle_rghtswipe(self, dflag=False) :
    if dflag: 
      print(f"Melody{self.index} was rghtswiped... before:")
      print(r.rules for r in self.rules_list)
    for rule in self.rules_list:
        rule.rghtswipe(dflag)
    if dflag: 
      print(f"after: ")
      print(r for r in self.rules_list)
    
  def handle_response(self, liked, dflag=False) :
    self.handle_rghtswipe(dflag) if liked else self.handle_leftswipe()
