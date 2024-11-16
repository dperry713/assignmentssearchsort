from flask import Flask, jsonify

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

# Merge Sort Implementation
def merge_sort(titles):
    if len(titles) <= 1:
        return titles
    
    # Divide the list into halves
    mid = len(titles) // 2
    left_half = merge_sort(titles[:mid])
    right_half = merge_sort(titles[mid:])
    
    # Merge the sorted halves
    return merge(left_half, right_half)

def merge(left, right):
    sorted_list = []
    i = j = 0
    
    # Compare and merge elements from both halves
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1
    
    # Append remaining elements from left or right
    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])
    
    return sorted_list

# Flask Application Setup
app = Flask(__name__)

@app.route('/sort', methods=['GET'])
def sort_videos():
    # Perform merge sort on the video titles
    sorted_titles = merge_sort(video_titles)
    return jsonify({"sorted_videos": sorted_titles}), 200

if __name__ == '__main__':
    app.run(debug=True)
