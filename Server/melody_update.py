from melody_t import *
import re # for regular expressions
import pickle
import mai # for writing lists to midi files. In the future I can use pretty_midi for this 

# Load melodies list
pickle_in = open("melodies.dat", "rb")
melody_list = pickle.load(pickle_in)
pickle_in.close()

# Load rules list
pickle_in = open("rules.dat", "rb")
rules = pickle.load(pickle_in)
pickle_in.close()



# Load swipe data
filename = "swipedata.txt"
with open(filename) as swipedata:
    for line in swipedata:
        # input santization?
        colon_index = line.find(":")
        melody_name = line[:colon_index]
        response = bool(re.search("True",line[colon_index+1:]))
        melody_index = int(re.search(r'\d+$', melody_name).group())

        # Try to swipe the melody, passing on exceptions
        try:
            melody_list[melody_index].handle_response(response)
        except Exception:
            print(f"passed on line: {line}")
            pass # ignore bad indices and more

# Clear the swipedata
with open(filename, 'r+') as f:
    f.truncate(0)

# Dump desirability scores to score_dump.txt
for i in range(0,len(melody_list[0].rules)):
    f = open("score_dump.txt", "a")
    f.write(f"Rule{i}: {melody_list[0].rules[i]}\n")
    f.close()

# Generate new set of melodies
for melody in melody_list:
    melody.generate_notes()
    my_melody = melody.notes
    midi_file = mai.make_music(my_melody, pgm=1, format='MIDI')\
                .write('melody' + str(melody.index) + '.mid')

# Pickle melody list
pickle_out = open("melodies.dat", "wb")
pickle.dump(melody_list, pickle_out)
pickle_out.close()