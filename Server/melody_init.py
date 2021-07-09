from melody_t import *
import mai # for writing lists to midi files. In the future I can use pretty_midi for this 
import pickle # for data persistence

start = 1 # Start melody index at 1
stop = start + 10 # Only make 10 melodies
melody_list = []

# Create a rules list instance
rules = Rules()

# Generate the melodies
for i in range(start, stop):
    melody = Melody(i, rules.rules)
    melody.generate_notes()
    melody_list += [melody]
# Print them to .mid files
for i in range(0, stop-start):
    my_melody = melody_list[i].notes
    midi_file = mai.make_music(my_melody, pgm=1, format='MIDI')\
                .write('melody' + str(melody_list[i].index) + '.mid')
# Store Melody list to data file
pickle_out = open("melodies.dat", "wb")
pickle.dump(melody_list, pickle_out)
pickle_out.close()

# Store Rules list to data file
pickle_out = open("rules.dat", "wb")
pickle.dump(rules, pickle_out)
pickle_out.close()

# Dump desirability scores to score_dump.txt
rules.dump_rules("score_dump.txt")