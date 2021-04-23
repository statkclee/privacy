# Classification Data set ------------------------------------
from sklearn.datasets import make_classification
from matplotlib import pyplot as plt
import numpy as np

## Visualization Helper Function to Check the correctness ----------
def plot_data_points(x, labels):

  my_scatter_plot = plt.scatter(x[:,0],
                                x[:,1],
                                c=y,
                                vmin=min(y),
                                vmax=max(y),
                                s=35)
  plt.title("Dataset with n_features="+ str(x.shape[1]) + " and n_classes=" + str(len(np.unique(labels))))
  plt.show()

x, y = make_classification(n_samples  = 5000,
                           n_classes  = 2,
                           n_features = 4,
                           class_sep  = 0.1,
                           n_clusters_per_class = 3)

## Checking -----------------------------
print(x.shape)

plot_data_points(x, y)

# Dataframe Data set ------------------------------------

from faker import Faker
import pandas as pd
import numpy as np
import random
from datetime import datetime

fake = Faker('ko_KR')

def create_rows_faker(num=1):
    output = [{"name"       : fake.name(),
               "ssn"        : fake.ssn(),
               "address"    : fake.address(),
               "latlng"     : fake.latlng(),
               "gender"     : np.random.choice(["M", "F"], p=[0.5, 0.5]),
               "email"      : fake.email(),
               "city"       : fake.city(),
               "company"    : fake.company(),
               "job"        : fake.job(),
               "ip_address" : fake.ipv4(network=False, address_class=None, private=None),
               "date_of_birth": fake.date_between_dates(date_start=datetime(1950,1,1), date_end=datetime(2000,12,31)).strftime("%Y-%m-%d"),
               "credit_card_full": fake.credit_card_full(card_type=None),
               "salary"     : np.random.lognormal(3, 1)} for x in range(num)]
    return output

df_faker = pd.DataFrame(create_rows_faker(100))

df_faker.to_csv("faked.csv")

