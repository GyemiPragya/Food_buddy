import numpy as np
from scipy.optimize import linear_sum_assignment

def optimal_matching(cost_matrix):
    """
    Implements the Hungarian algorithm for optimal assignment
    
    Parameters:
    cost_matrix (numpy.ndarray): Matrix where rows=donors, columns=recipients
                                 and values represent costs/distances
    
    Returns:
    list of tuples: Optimal donor-recipient pairings
    float: Total minimum cost
    """
    # Run Hungarian algorithm
    row_indices, col_indices = linear_sum_assignment(cost_matrix)
    
    # Create matches
    matches = list(zip(row_indices, col_indices))
    
    # Calculate total cost
    total_cost = cost_matrix[row_indices, col_indices].sum()
    
    return matches, total_cost
"""
# Example usage
if __name__ == "__main__":
    # Example cost matrix: rows = donors, columns = recipients
    # Lower cost means a better match (e.g., less distance)
    cost_matrix = np.array([
        [4, 2, 8],
        [2, 3, 7],
        [3, 1, 6]
    ])
    
    matches, total_cost = optimal_matching(cost_matrix)
    
    print("Optimal matches (donor_id, recipient_id):")
    for donor_id, recipient_id in matches:
        print(f"Donor {donor_id} → Recipient {recipient_id} (Cost: {cost_matrix[donor_id, recipient_id]})")
    
    print(f"Total cost: {total_cost}")
"""