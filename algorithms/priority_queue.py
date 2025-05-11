import heapq
from datetime import datetime

class FoodItem:
    def __init__(self, name, expiration_date):
        self.name = name
        self.expiration_date = datetime.strptime(expiration_date, "%Y-%m-%d")
    def __lt__(self, other):
        return self.expiration_date < other.expiration_date
    def __repr__(self):
        return f"{self.name} (expires: {self.expiration_date.date()})"

class FoodPriorityQueue:
    def __init__(self):
        self.heap = []
    def add_food(self, food_item):
        heapq.heappush(self.heap, food_item)
    def get_next_to_deliver(self):
        if self.heap:
            return heapq.heappop(self.heap)
        else:
            return None
    def show_queue(self):
        return sorted(self.heap)

# Example usage
if __name__ == "__main__":
    pq = FoodPriorityQueue()
    pq.add_food(FoodItem("Bread", "2025-05-12"))
    pq.add_food(FoodItem("Milk", "2025-05-10"))
    pq.add_food(FoodItem("Rice", "2025-06-01"))
    pq.add_food(FoodItem("Eggs", "2025-05-09"))

    print("Current queue (soonest expiring first):", pq.show_queue())
    print("Next food to deliver:", pq.get_next_to_deliver())
    print("Queue after delivery:", pq.show_queue())
