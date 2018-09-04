#Implement the functionality for a class that encapsulates the functionality of a least recently used cache.

class LRUCache:

  def __init__(self, capacity):
    self._capacity = capacity
    self._items = []
    pass
  
  #Behaviour: 
  # - If an item already exists for key, update it as most recently used. 
  # - If there is more than capacity items in the cache, remove the oldest one. Add the new item to the cache.  
  def set(self, key, item):
    if len(self._items) >= self._capacity:
      self._items.pop()

    for i in range(len(self._items)):
      if self._items[i]['key'] == key:
        self._items.pop(i)
        break
    
    self._items.insert(0, {'key': key, 'item': item})
    pass 
  
  #Behavior: 
  # - Return the item in the key if it exists or return None
  # - Mark the item that exists as most recently used.
  def get(self, key):
    for i, item in enumerate(self._items):
      if item['key'] == key:
        self._items.pop(i)
        self._items.insert(0, item)
        return item['item']
    return None

#Test code...

cache = LRUCache(20)

for i in range(20):
    cache.set(i, {'val' : i})

#moves 0 to be the most recently used
assert(cache.get(0))

cache.set(21, {'val' : 21})

print(cache._items)    
assert(not cache.get(1))
