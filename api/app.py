from flask import Flask, request, jsonify
import numpy as np
from algorithms.hungarian import optimal_matching

app = Flask(__name__)

@app.route('/match', methods=['POST'])
def match():
    data = request.get_json()
    cost_matrix = np.array(data['cost_matrix'])
    matches, total_cost = optimal_matching(cost_matrix)
    # Convert numpy.int64 to int for JSON serialization
    matches = [[int(donor), int(recipient)] for donor, recipient in matches]
    total_cost = float(total_cost)
    return jsonify({
        'matches': matches,
        'total_cost': total_cost
    })

if __name__ == '__main__':
    app.run(debug=True)
