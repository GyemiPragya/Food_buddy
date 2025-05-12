"""from rtree import index

# Example donor/recipient locations (latitude, longitude)
locations = [
    (28.7041, 77.1025),  # Delhi
    (19.0760, 72.8777),  # Mumbai
    (13.0827, 80.2707),  # Chennai
    (22.5726, 88.3639),  # Kolkata
]

idx = index.Index()
for i, loc in enumerate(locations):
    idx.insert(i, (*loc, *loc))  # Insert as a point

# Query: find nearest to Bangalore (12.9716, 77.5946)
nearest = list(idx.nearest((12.9716, 77.5946, 12.9716, 77.5946), 1))
print("Nearest location index (R-Tree):", nearest)
print("Nearest location:", locations[nearest[0]])
"""
from rtree import index

def find_nearest_location(locations, query_point):
    idx = index.Index()
    for i, loc in enumerate(locations):
        idx.insert(i, (*loc, *loc))
    nearest = list(idx.nearest((*query_point, *query_point), 1))
    return nearest[0]
