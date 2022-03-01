#Rakin Mohammad Sifullah
#University of Asia Pacific


## create hashtable

class HashTable:

  def __init__(self):
    self.size = 10
    self.hashmap = [[]for i in range(10)]  ## nested list 

    print(self.hashmap)

## create hashing func
  def hashing_func(self, key):
    hashed_key = hash(key) % self.size #hash holo python ar built in function
    return hashed_key


  def insert(self, key, value):
    hash_key = self.hashing_func(key)
    key_exists = False
    slot = self.hashmap[hash_key]
    for i , kv in enumerate(slot):  #for many item  a in a  slot

      k, v = kv #split key and value
      if key == k:
         key_exists = True
         break

    if key_exists:
      slot[i] = ((key, value))
    
    else:
      slot.append((key, value))


#get hash key
  def getHashKey(self, key):
    hash_key = self.hashing_func(key)
    slot = self.hashmap[hash_key] 
    for kv in slot:
      k, v = kv
      if key == k:
        return hash_key

      else:
        print("None")

#delete
  def delete(self, key):
    hash_key = self.hashing_func(key)
    
    for index, element in enumerate(self.hashmap[hash_key]):
          if element[0] == key:
  
              del self.hashmap[hash_key][index] # first brckt ta index number , 2nd ta oi index r vitore koto num index

#search
  def search(self, key):
    hash_key = self.hashing_func(key)
    slot = self.hashmap[hash_key] 
    for kv in slot:
      if kv[0] == key:
        return slot

#update      
  def update(self, key, value):
    hash_key = self.hashing_func(key)
    found = False
    for index, element in enumerate(self.hashmap[hash_key]):
            if len(element)==2 and element[0] == key:
               self.hashmap[hash_key][index] = (key,value)
               found = True
    if not found:
          print("no update")

#create an object of the hashmap
H = HashTable()

H.insert('fariha', 'ID')
H.insert(10, 'Number')
H.insert('+', 'Symbol')
H.insert('int', 'Keyword')
H.insert('if', 'Keyword')

#show 
print(H.hashmap)

print(H.getHashKey('fariha'))

H.delete('fariha')
print(H.hashmap)

H.update(10,'Num')
print(H.hashmap)

H.search(10)