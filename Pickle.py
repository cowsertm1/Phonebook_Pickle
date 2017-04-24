import pickle

self.contacts = {}

# Store data (serialize)
with open('contacts.pickle', 'wb') as handle:
    pickle.dump(self.contacts, handle, protocol=pickle.HIGHEST_PROTOCOL)

# Load data (deserialize)
with open('contacts.pickle', 'rb') as handle:
    unserialized_data = pickle.load(handle)

print(self.contacts == unserialized_data)