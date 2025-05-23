# Food_buddy
A project for 4th sem making use of DAA 
<br>
Author - Pragya Thapliyal
---

## Algorithms Used

### 1. Hungarian Algorithm (Optimal Matching)

**Purpose:**  
Assigns food donors to recipients in a way that maximizes total efficiency (minimizing distance, matching food types, etc.).

**How it works:**  
- Models the donor-recipient assignment as a bipartite graph.
- Uses the Hungarian Method to find the optimal matching based on a cost matrix (e.g., distance, food compatibility).

**How to run/test:**  
 Start the Flask backend (`python app.py` in the `backend` directory).  
  Send a POST request to `/match`

---

### 2. Clarke-Wright Savings Algorithm (Route Optimization with Capacity)

Optimizes delivery routes for volunteers, minimizing total travel distance while respecting vehicle/volunteer capacity limits.

- **How it works:**  
Starts with each recipient as a separate route. Calculates "savings" for combining routes, and merges the best routes as long as the total food to deliver does not exceed vehicle capacity.

- **How to run/test:**  
Start the Flask backend.  
Send a POST request to `/route`

---
### Priority Queue (Food Expiration Management)

Ensures food items closest to expiration are delivered first, reducing waste.

- **How it works:**  
  Uses a priority queue (min-heap) where each food item’s priority is its expiration date. The soonest-to-expire food is always delivered first.

- **How to run/test:**  
Start the Flask backend.  
Send a POST request to `/next_expiring` 

---
### R-Tree Spatial Indexing (Geographic Queries)

Allows fast queries for nearest donors or recipients based on location.

- **How it works:**  
  Uses an R-Tree (or KDTree fallback) to index locations and quickly find the nearest ones.

- **How to run/test:**  
Start the Flask backend.  
Send a POST request to `/nearest` 
---
## API Endpoints

The following API endpoints are available:

-   **`/match` (POST):**
    -   Description: Finds the optimal matches between donors and recipients based on a cost matrix.
    -   Input (JSON):
        ```
        {
          "cost_matrix": [[1],[2],[2][2]
          ]
        }
        ```
    -   Output (JSON):
        ```
        {
          "matches": [[1],[1],[2][2]],
          "total_cost": 5.0
        }
        ```

-   **`/route` (POST):**
    -   Description: Optimizes delivery routes for volunteers using the Clarke-Wright Savings Algorithm.
    -   Input (JSON):
        ```
        {
          "locations": [,[2],,[1],[1]],
          "demands":[2][2][1],
          "capacity": 5
        }
        ```
    -   Output (JSON):
        ```
        {
          "routes": [[1][2],]
        }
        ```

-   **`/next_expiring` (POST):**
    -   Description: Returns the next food item that should be delivered based on expiration date.
    -   Input (JSON):
        ```
        {
          "food_items": [
            { "name": "Bread", "expiration_date": "2025-05-12" },
            { "name": "Milk", "expiration_date": "2025-05-10" }
          ]
        }
        ```
    -   Output (JSON):
        ```
        {
          "next_to_deliver": "FoodItem('Milk', datetime.date(2025, 5, 10))"
        }
        ```

-   **`/nearest` (POST):**
    -   Description: Finds the nearest location to a given query point using R-Tree spatial indexing.
    -   Input (JSON):
        ```
        {
        "locations": [
            [28.7041, 77.1025],
            [19.0760, 72.8777],
            [13.0827, 80.2707],
            [22.5726, 88.3639]
        ],
        "query_point": [12.9716, 77.5946]
        }
    -    Output (JSON):
        {
        "nearest_index": 2
        }

## How to Contribute

- Clone the repo and create a new branch for your feature or algorithm.
- Add your code in the `algorithms/` folder with clear comments.
- Update this README with instructions for your algorithm.
- Open a pull request for review.

---
## How to Run the Backend and Test the API

1. Install dependencies:  
 `pip install flask numpy scipy rtree`
2. Go to the backend directory:  
 `cd backend`
3. Start the Flask server:  
 `python app.py`
4. Use Thunder Client (VS Code), Postman, or curl to send POST requests to the endpoints above.

---

## Team

- Moksh Dhandariya - UI/UX, Features, Gamification
- Pragya Thapliyal - UI/UX, Key Features
- Ashutosh - Database, Backend
- Ashu Chauhan - Testing, Documentation

---

---

## References

1. Food and Agriculture Organization of the United Nations. (2023). Food Loss and Food Waste. http://www.fao.org/food-loss-and-food-waste/
2. Kuhn, H.W. (1955). The Hungarian Method for the assignment problem. Naval Research Logistics Quarterly, 2(1-2), 83-97.
3. Clarke, G., & Wright, J.W. (1964). Scheduling of vehicles from a central depot to a number of delivery points. Operations Research, 12(4), 568-581.
4. Guttman, A. (1984). R-trees: A dynamic index structure for spatial searching. SIGMOD '84, 47-57.
5. Fathollahi-Fard, A.M., Hajiaghaei-Keshteli, M., & Tavakkoli-Moghaddam, R. (2018). The social engineering optimizer (SEO). Engineering Applications of Artificial Intelligence, 72, 267-293.
6. Hamari, J., Koivisto, J., & Sarsa, H. (2014). Does Gamification Work? A Literature Review of Empirical Studies on Gamification. 47th Hawaii International Conference on System Sciences.



