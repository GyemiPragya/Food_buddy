def euclidean_distance(p1, p2):
    return ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2) ** 0.5

def clarke_wright_savings_with_capacity(depot, recipients, demands, vehicle_capacity):
    n = len(recipients)
    routes = [[i] for i in range(n)]  # Each recipient in their own route
    route_demands = [demands[i] for i in range(n)]  # Track demand for each route

    # Calculate savings
    savings = []
    for i in range(n):
        for j in range(i+1, n):
            s = (euclidean_distance(depot, recipients[i]) +
                 euclidean_distance(depot, recipients[j]) -
                 euclidean_distance(recipients[i], recipients[j]))
            savings.append((s, i, j))
    savings.sort(reverse=True)

    # Merge routes with highest savings, respecting capacity
    for s, i, j in savings:
        route_i = route_j = None
        for route in routes:
            if route[0] == i:
                route_i = route
            if route[-1] == j:
                route_j = route
        if route_i and route_j and route_i != route_j:
            demand_sum = sum([demands[idx] for idx in route_i + route_j])
            if demand_sum <= vehicle_capacity:
                # Merge routes
                merged = route_i + route_j
                routes.remove(route_i)
                routes.remove(route_j)
                routes.append(merged)
                # No need to update route_demands, as we recalculate on the fly
    return routes
'''
# Example usage:
if __name__ == "__main__":
    depot = (0, 0)
    recipients = [(2, 3), (5, 4), (1, 7), (6, 1)]
    demands = [2, 3, 2, 1]  # Each recipient's demand
    vehicle_capacity = 5
    routes = clarke_wright_savings_with_capacity(depot, recipients, demands, vehicle_capacity)
    print("Optimized routes with capacity:", routes)
'''
def run_clarke_wright(locations, demands, capacity):
    """
    Wrapper for Flask API. 
    locations: list of [x, y] coordinates, first one is depot, rest are recipients
    demands: list of demands (first one for depot, should be 0)
    capacity: vehicle capacity
    Returns: list of routes (each route is a list of recipient indices)
    """
    depot = tuple(locations[0])
    recipients = [tuple(loc) for loc in locations[1:]]
    # demands: first is depot, rest are recipients
    recipient_demands = demands[1:]
    routes = clarke_wright_savings_with_capacity(depot, recipients, recipient_demands, capacity)
    # Convert routes (which use recipient indices) to indices in the original locations list
    # +1 because recipients start from index 1 in locations
    routes_with_indices = [[0] + [r+1 for r in route] + [0] for route in routes]
    return routes_with_indices
