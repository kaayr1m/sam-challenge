def same_place(place1, place2):
  return place1 == place2

def unique_ify(places):
  for i, place1 in enumerate(places):
    for j, place2 in enumerate(places):
      if i != j and same_place(place1, place2):
        del places[j]
  return places


place1 = {'name': 'West Edmonton Mall', 'city': 'Edmonton', 'country': 'Canada'}
place2 = {'name': 'The Legislature', 'city': 'Edmonton', 'country': 'Canada'}
place3 = {'name': 'The Saddle Dome', 'city': 'Calgary', 'country': 'Canada'}
place4 = {'name': 'The Legislature', 'city': 'Victoria', 'country': 'Canada'}
place5 = {'name': 'West Edmonton Mall', 'city': 'Edmonton', 'country': 'USA'}
place6 = {'name': 'West Edmonton Mall', 'city': 'Edmonton', 'country': 'Canada'}

assert(same_place(place1, place1))
assert(not same_place(place1, place3))
assert(not same_place(place2, place4))
assert(not same_place(place1, place5))
assert(same_place(place1, place6))


places = [ {'name': 'West Edmonton Mall', 'city': 'Edmonton', 'country': 'Canada'},
           {'name': 'The Legislature', 'city': 'Edmonton', 'country': 'Canada'},
           {'name': 'The Saddle Dome', 'city': 'Calgary', 'country': 'Canada'},
           {'name': 'The Legislature', 'city': 'Victoria', 'country': 'Canada'},
           {'name': 'The Legislature', 'city': 'Edmonton', 'country': 'Canada'},
           {'name': 'West Edmonton Mall', 'city': 'Edmonton', 'country': 'USA'},
           {'name': 'The Saddle Dome', 'city': 'Calgary', 'country': 'Canada'},
]


unique_places = unique_ify(places)

print(unique_places)
assert(unique_places == [{'name': 'West Edmonton Mall', 'city': 'Edmonton', 'country': 'Canada'},
                         {'name': 'The Legislature', 'city': 'Edmonton', 'country': 'Canada'},
                         {'name': 'The Saddle Dome', 'city': 'Calgary', 'country': 'Canada'},
                         {'name': 'The Legislature', 'city': 'Victoria', 'country': 'Canada'},
                         {'name': 'West Edmonton Mall', 'city': 'Edmonton', 'country': 'USA'},
])