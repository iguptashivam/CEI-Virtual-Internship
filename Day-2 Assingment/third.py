import json

jsonData = """
{
    "date": "2023-07-01",
    "explanation": "On July 4th, Earth's annual aphelion...",
    "title": "aphelion sunrise",
    "url": "https://apod.nasa.gov/apod/image/2307/AphelionSunrise2023_1024.jpg"
}
"""

data = json.loads(jsonData)

print(f"Explanation: {data['explanation']}")
print(f"Title: {data['title']}")
