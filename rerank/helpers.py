# Importing Libraries

import random
import time

import faker
import openai
import pinecone
import tqdm
from datasets import Dataset

fake = faker.Faker()
index_name = "coherererank"
dimension = 1536
embed_model = "text-embedding-ada-002"
