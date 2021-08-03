# In this file I define variables that are used for multiple files

MELODY_LEN = 16
NOTE_RGE_MAX = 108  # The highest note that midi can play
NOTE_RGE_MIN = 36   # The lowest note that the <pretty-midi> player can
MAX_1ST_NOTE = 86   # Maximum first note when constrained by a scale

# 3 octaves of minor and major keys as intervals
MINOR_KEY = [-12, -10,-9,-7,-5,-4,-2, 0,2,3,5,7,8,10, 12,14,15,17,19,20,22, 24] 
MAJOR_KEY = [-12, -10,-8,-7,-5,-3,-1, 0,2,4,5,7,9,11, 12,14,16,17,19,21,23, 24] 

# persistency filenames
DATA_RULES_DAT = "./data/rules.dat"
DATA_MELOS_DAT = "./data/melodies.dat"
DATA_SWIPEDATA = "./data/swipedata.txt"
SWIP_CACHE_TXT = "./data/swipedata_cache.txt"

# Tabularized 
SWIPE_DATA_TSV = "./data/tabularized_swipedata.tsv" 

# score dump filename
SCORE_DUMP_TXT = "./dumps/score_dump.txt"
SCORE_DUMP_DAT = "./dumps/score_dump.dat"

# Random seed
RANDOM_SEED = 4

# Number of melodies in a generation
GEN_SIZE = 10

# Tabularized data headers
PRE_USERNAME_HEADER = ["INDEX", "LIKED", "DISLIKED"] + [f"RULE{i}" for i in range (1, 10)]
POST_USERNAME_HEADER = ""
