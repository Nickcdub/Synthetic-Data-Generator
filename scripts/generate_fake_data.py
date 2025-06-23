from faker import Faker
import pandas as pd

def main():

    fake = Faker()
    data = []

    for _ in range(1000):
        #We want to make sure that the emails correlate to the person
        fname = fake.first_name()
        lname = fake.last_name()
        name = fname + " " +lname

        data.append({
            'name': name,
            'email': (fname[0] + lname).lower() + '@example.com',
            'address': fake.address(),
            'phone': fake.phone_number(),
            'company': fake.company(),
            'job': fake.job(),
            'city': fake.city(),
            'state': fake.state()
        })

    df = pd.DataFrame(data)
    df.to_csv('data/raw/fake_data.csv', index=False)