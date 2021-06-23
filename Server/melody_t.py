# import
import random
from rules_l import *

# Rule Object
class Rule:
  def __init__(self, function):
    self.function = function
    self.likes = 1
    self.dislikes = 1
  def desirability(self):
    return (self.likes / self.dislikes)
  def leftswipe(self):
    self.likes += 1
  def rghtswipe(self):
    self.dislikes += 1

# List of Rules which can be selected for Melody instances
rules = [Rule(rule1),
         Rule(rule2),
         Rule(rule3),
         Rule(rule4),
         Rule(rule5),
         Rule(rule6)]

# Define a Melody Object
class Melody:
  def __init__(self, index, rules_list=[]) :
    self.notes = []
    self.rules_list = rules_list
    self.index = index
    self.midi_path = ""

  def generate_notes(self) :
    # Choose some rules
    num_rules = random.randint(3,5)
    self.rules_list = []
    self.rules_list = random.choices(rules, weights = [i.desirability() for i in rules], k=num_rules)
    # Use rules
    # loop until we have 12 notes
    while len(self.notes) < 12:
      # generate a random note between 0 and 108
      new_note = random.randint(0,108)
      
      # test note with all rules in rules_list
      note_results = [rule.function(new_note, self.notes) for rule in self.rules_list]
          
      # does it pass ALL of the rules? append new_note to the melody
      if all(note_results):
        self.notes += [new_note]

  def handle_leftswipe(self) :
    for rule in self.rules_list:
        rule.leftswipe()

  def handle_rghtswipe(self) :
    for rule in self.rules_list:
        rule.rghtswipe()
    
  def handle_response(self, liked) :
    self.handle_rghtswipe() if liked else self.handle_leftswipe()
