# algorithms/clarke_wright.py

def euclidean_distance(p1, p2):
    """Calculate Euclidean distance between two points."""
    return ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2) ** 0.5

def clarke_wright_savings(depot, recipients):
    """
    depot: tuple (x, y)
    recipients: list of tuples [(x1, y1), (x2, y2), ...]
    Returns: list of routes (each route is a list of recipient indices)
    """
    n = len(recipients)
    # Step 1: Start with each recipient as its own route
    routes = [[i] for i in range(n)]
    
    # Step 2: Calculate savings for every pair
    savings = []
    for i in range(n):
        for j in range(i+1, n):
            s = (euclidean_distance(depot, recipients[i]) +
                 euclidean_distance(depot, recipients[j]) -
                 euclidean_distance(recipients[i], recipients[j]))
            savings.append((s, i, j))
    # Step 3: Sort savings in descending order
    savings.sort(reverse=True)
    
    # Step 4: Merge routes with highest savings (simple version)
    for s, i, j in savings:
        # Find routes containing i and j
        route_i = route_j = None
        for route in routes:
            if route[0] == i:
                route_i = route
            if route[-1] == j:
                route_j = route
        if route_i and route_j and route_i != route_j:
            # Merge if they are not the same route
            merged = route_i + route_j
            routes.remove(route_i)
            routes.remove(route_j)
            routes.append(merged)
    return routes

# Example usage:
if __name__ == "__main__":
    depot = (0, 0)
    recipients = [(2, 3), (5, 4), (1, 7), (6, 1)]
    routes = clarke_wright_savings(depot, recipients)
    print("Optimized routes:", routes)
