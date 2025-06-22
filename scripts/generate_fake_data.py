from faker import Faker
import pandas as pd


fake = Faker()
data = []

for _ in range(1000):
    data.append({
        'name': fake.name(),
        'email': fake.email(),
        'address': fake.address(),
        'phone': fake.phone_number(),
        'company': fake.company(),
        'job': fake.job(),
        'city': fake.city(),
        'state': fake.state()
    })

df = pd.DataFrame(data)
df.to_csv('data/raw/fake_data.csv', index=False)