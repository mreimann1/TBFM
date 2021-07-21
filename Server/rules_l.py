# Author: Marques Reimann
# Date: 6/18/2021
# Description: A list of rule functions

from var_defs import *

# Rules taken form illiac suite
def rule1 (new_note, melody, dflag=False):
  # the octave rule
  if (dflag): print("the octave rule")
  return (max(melody + [new_note]) - min(melody + [new_note]) <= 12)

# rules 2 and 3?
def rule2 (new_note, melody, dflag=False):
  if (dflag): print("true 2")
  return True

def rule3 (new_note, melody, dflag=False):
  if (dflag): print("true 3")
  return True

def rule4 (new_note, melody, dflag=False):
  # no skips of a major or minor seventh
  if (dflag): print("no skips of a major or minor seventh")
  return (len(melody) < 1 or abs(new_note - melody[-1]) != 11 and abs(new_note - melody[-1]) != 10)

def rule5 (new_note, melody, dflag=False):
  # a skip must be followed by stepwise motion
  if (dflag): print("a skip must be followed by stepwise motion")
  return (len(melody) < 2 or abs(melody[-1] - melody[-2]) < 3 or abs(new_note - melody[-1]) <= 2)

def rule6 (new_note, melody, dflag=False):
  # no more than one successive repeat of a given note
  if (dflag): print("no more than one successive repeat of a given note")
  return (len(melody) < 2 or not (new_note == melody[-2] == melody[-1]))

# last note must be same as first
def rule7 (new_note, melody, dflag=False):
  if (dflag): print("last note must be same as first")
  return ( len(melody) < (MELODY_LEN - 1) or new_note == melody[0] )

# note must fit in Minor key based on first note as root
def rule8 (new_note, melody, dflag=False):
  if (dflag): print("note must fit in minor key based on first note as root")
  return (((len(melody) == 0 ) and (new_note < MAX_1ST_NOTE)) or 
          ((len(melody) > 0) and any(new_note == melody[0] + interval for interval in MINOR_KEY)))

# note must fit in Major key based on first note as root
def rule9 (new_note, melody, dflag=False):
  if (dflag): print("note must fit in major key based on first note as root")
  return (((len(melody) == 0 ) and (new_note < MAX_1ST_NOTE)) or 
          ((len(melody) > 0) and any(new_note == melody[0] + interval for interval in MAJOR_KEY)))