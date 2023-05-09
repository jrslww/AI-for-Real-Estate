import pandas as pd
import random
from faker import Faker

fake = Faker()

# Set a seed for reproducibility
random.seed(42)
Faker.seed(42)

# Number of rows to generate
num_rows = 50000

data = {
    "property_id": [i for i in range(1, num_rows + 1)],
    "location": [fake.city() for _ in range(num_rows)],
    "size_sqft": [random.randint(500, 5000) for _ in range(num_rows)],
    "num_rooms": [random.randint(1, 10) for _ in range(num_rows)],
    "age_years": [random.randint(0, 100) for _ in range(num_rows)],
    "condition": [random.choice(["Poor", "Fair", "Good", "Excellent"]) for _ in range(num_rows)],
    "proximity_to_amenities_km": [round(random.uniform(0.1, 10), 2) for _ in range(num_rows)],
    "sale_price_usd": [random.randint(100000, 2000000) for _ in range(num_rows)],
}

df = pd.DataFrame(data)

# Save the dataframe to a .csv file
df.to_csv("modules/property_valuation/data/property_data.csv", index=False)
