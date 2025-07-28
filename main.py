import requests
import json
import time

# SerpAPI Key
API_KEY = ""

def get_top_restaurants(city):
    """
    Fetches the top 10 restaurants for a given city using the SerpAPI Google Maps engine.
    Combines ratings, number of reviews, address, and a sample review snippet.
    """
    query = f"top 10 restaurants in {city}"

    # Define search parameters for the API
    params = {
        "engine": "google_maps",     # Google Maps results
        "q": query,                  # Search query
        "type": "search",            # Search type
        "api_key": API_KEY           # SerpAPI key
    }

    print(f"\n Searching for: {query}")
    response = requests.get("https://serpapi.com/search.json", params=params)
    results = response.json()
    restaurant_data = {}

    # Extract local business results
    local_results = results.get("local_results", [])

    # Loop through top 10 restaurants
    for result in local_results[:10]:
        name = result.get("title", "Unknown")                        # Restaurant name
        rating = result.get("rating", "N/A")                         # Rating (e.g., 4.5)
        reviews_count = result.get("reviews", "N/A")                # Review count (e.g., 120)
        address = result.get("address", city)                        # Address
        place_id = result.get("place_id", None)                      # Used to fetch detailed reviews

        # Initialize review text
        review_text = ""

        # If we have a place_id, fetch a sample review
        if place_id:
            review_text = get_sample_review(place_id)
            time.sleep(1)  # Pause to respect API rate limits

        # Format the combined review field as per your expected output
        formatted_reviews = f"{reviews_count} reviews. Recommended: {review_text}" if reviews_count != "N/A" else f"Recommended: {review_text}"

        # Store restaurant data in dictionary
        restaurant_data[name] = {
            "Rating": str(rating),
            "Reviews": formatted_reviews,
            "Address": address
        }

    return restaurant_data

def get_sample_review(place_id):
    """
    Given a place_id, fetch a short review snippet using the reviews engine.
    """
    detail_params = {
        "engine": "google_maps_reviews",  # Reviews API engine
        "place_id": place_id,             # Specific place ID from previous results
        "api_key": API_KEY                # API key
    }

    # Make the API request for reviews
    review_response = requests.get("https://serpapi.com/search.json", params=detail_params)
    review_data = review_response.json()

    # Get the first review snippet if available
    reviews = review_data.get("reviews", [])
    if reviews:
        return reviews[0].get("snippet", "No review found.")

    return "No reviews available."

def save_to_json(data, filename="restaurants.json"):
    """
    Save the final result to a JSON file.
    """
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)
    print(f"\n Data saved to {filename}")

def main():
    """
    Main function to take input and trigger search + saving.
    """
    city = input("Enter the name of a city: ").strip()
    data = get_top_restaurants(city)
    save_to_json(data)

#  Entry point
if __name__ == "__main__":
    main()
