import requests
from faker import Faker

# Initialize the Faker library
faker = Faker()

url = 'http://localhost:5000/api/v1/leads/'
headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjY2YzE3MDEzZGIwMjc1Njg4MDEzNTEwNyIsImlhdCI6MTcyMzk1NDU0MSwiZXhwIjoxNzI0MDQwOTQxfQ.u2RfpjXCSPy-apuoCpEpTPJ_f6falsrY2ImY-p1cnII'  # Replace with your actual JWT token
}

# Create 200 leads
for _ in range(200):
    data = {
        "name": faker.name(),
        "email": faker.unique.email(),
        "phone": faker.unique.phone_number(),
        "status": faker.random_element(elements=('New', 'Contacted', 'Qualified', 'Lost', 'Converted')),
    }

    # Send POST request to add the lead
    response = requests.post(url, headers=headers, json=data)

    # Check if the request was successful
    if response.status_code == 201:
        print(f"Lead added successfully: {data['name']}")
    else:
        print(f"Failed to add lead: {data['name']} - Status code: {response.status_code}")
