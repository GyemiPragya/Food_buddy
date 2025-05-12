from flask import Flask, request, jsonify
import numpy as np
import sys
import os

# Ensure algorithms folder is in the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../algorithms')))

from hungarian import optimal_matching
from clarke_wright import run_clarke_wright
from priority_queue import FoodPriorityQueue, FoodItem
from r_tree import find_nearest_location  # Make sure you have this function

app = Flask(__name__)

@app.route('/match', methods=['POST'])
def match():
    data = request.get_json()
    cost_matrix = np.array(data['cost_matrix'])
    matches, total_cost = optimal_matching(cost_matrix)
    matches = [[int(d), int(r)] for d, r in matches]
    return jsonify({'matches': matches, 'total_cost': float(total_cost)})

@app.route('/route', methods=['POST'])
def route():
    data = request.get_json()
    locations = data['locations']
    demands = data['demands']
    capacity = data['capacity']
    routes = run_clarke_wright(locations, demands, capacity)
    return jsonify({'routes': routes})

@app.route('/next_expiring', methods=['POST'])
def next_expiring():
    data = request.get_json()
    pq = FoodPriorityQueue()
    for item in data['food_items']:
        pq.add_food(FoodItem(item['name'], item['expiration_date']))
    next_item = pq.get_next_to_deliver()
    return jsonify({'next_to_deliver': repr(next_item)})

@app.route('/nearest', methods=['POST'])
def nearest():
    data = request.get_json()
    locations = data['locations']
    query_point = data['query_point']
    idx = find_nearest_location(locations, query_point)
    return jsonify({'nearest_index': idx})

if __name__ == '__main__':
    app.run(debug=True)
