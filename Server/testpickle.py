import pickle

cheese = "string"

print (cheese)

pickle_out = open("test_pickle.dat", "wb")
pickle.dump(cheese, pickle_out)
pickle_out.close()

pickle_in = open("test_pickle.dat", "rb")
example_dict = pickle.load(pickle_in)

print (f"Pickled cheese: \n{example_dict}\n{example_dict[2]}")


