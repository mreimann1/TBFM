from melody_t import *
import re # for regular expressions
import pickle
import mai # for writing lists to midi files. In the future I can use pretty_midi for this 

pickle_in = open("melodies.dat", "rb")
melody_list = pickle.load(pickle_in)
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

        # print (f"melody_name: {melody_name} index: {melody_index} swipe response: {response}\n")

        # Try to swipe the melody, passing on exceptions
        try:
            melody_list[melody_index].handle_response(response)
        except Exception:
            pass # ignore bad indices and more

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