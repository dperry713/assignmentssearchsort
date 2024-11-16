from flask import Flask, request, jsonify

# Predefined list of video titles
video_titles = [
    "The Art of Coding",
    "Exploring the Cosmos",
    "Cooking Masterclass: Italian Cuisine",
    "History Uncovered: Ancient Civilizations",
    "Fitness Fundamentals: Strength Training",
    "Digital Photography Essentials",
    "Financial Planning for Beginners",
    "Nature's Wonders: National Geographic",
    "Artificial Intelligence Revolution",
    "Travel Diaries: Discovering Europe"
]

# Ensure the list is sorted
video_titles.sort()

# Binary Search Implementation
def binary_search(titles, query):
    low, high = 0, len(titles) - 1
    while low <= high:
        mid = (low + high) // 2
        if titles[mid] == query:
            return titles[mid]
        elif titles[mid] < query:
            low = mid + 1
        else:
            high = mid - 1
    return None

# Flask Application Setup
app = Flask(__name__)

@app.route('/search', methods=['GET'])
def search_videos():
    # Get the query parameter
    query = request.args.get('query', '')
    
    if not query:
        return jsonify({"error": "Query parameter is required"}), 400
    
    # Perform binary search
    result = binary_search(video_titles, query)
    
    if result:
        return jsonify({"message": "Video found", "video_title": result}), 200
    else:
        return jsonify({"message": "Video not found"}), 404

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
