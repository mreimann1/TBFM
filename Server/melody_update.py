from melody_t import *
from var_defs import *
import re # for regular expressions
import pickle
import music_maker as mai

# Load melodies list
pickle_in = open(DATA_MELOS_DAT, "rb")
melody_list = pickle.load(pickle_in)
pickle_in.close()

# Load rules list
pickle_in = open(DATA_RULES_DAT, "rb")
rules = pickle.load(pickle_in)
pickle_in.close()

# Load swipe data
with open(DATA_SWIPEDATA) as swipedata:
    for line in swipedata:
        
        # Search for a colon, set melodyname to the string before it, response to the string after
        colon_index = line.find(":")
        if (colon_index < 0) : continue
        melody_name = line[:colon_index]
        response = bool(re.search("True",line[colon_index+1:]))
        melody_index = int(re.search(r'\d+$', melody_name).group())

        # Try to swipe the melody, passing on exceptions
        try:
            melody_list[melody_index].handle_response(response)
        except Exception:
            print(f"passed on line: {line}")
            pass # ignore bad indices and more

# Append swipedata to cache
# Open first file in append mode and second file in read mode
cache_file = open(SWIP_CACHE_TXT, 'a+')
dump_file = open(DATA_SWIPEDATA, 'r+')
 
# Append the contents of the second file to the first file
cache_file.write(dump_file.read())

# Clear the swipedata
dump_file.truncate(0)

cache_file.close()
dump_file.close()

# Dump desirability scores to score_dump.txt
for i in range(0,len(melody_list[0].rules)):
    f = open(SCORE_DUMP_TXT, "a+")
    f.write(f"Rule{i}: {melody_list[0].rules[i]}\n")
    f.close()

# load list of rules lists from file
pickle_in = open(SCORE_DUMP_DAT, "rb")
rules_l_series = pickle.load(pickle_in)
pickle_in.close()

# append and dump list of rules lists back
rules_l_series += [melody_list[0].rules]
pickle_out = open(SCORE_DUMP_DAT, "wb")
pickle.dump(rules_l_series, pickle_out)
pickle_out.close()

# Store Rules list to data file
pickle_out = open(DATA_RULES_DAT, "wb")
pickle.dump(rules, pickle_out)
pickle_out.close()

# Generate new set of melodies
for melody in melody_list:
    melody.generate_notes()
    my_melody = melody.notes
    midi_file = mai.make_music(my_melody, pgm=1, format='MIDI')\
                .write('melody' + str(melody.index) + '.mid')

# Pickle melody list
pickle_out = open(DATA_MELOS_DAT, "wb")
pickle.dump(melody_list, pickle_out)
pickle_out.close()