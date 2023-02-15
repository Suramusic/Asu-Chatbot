from os import getenv

LOAD = getenv("LOAD", "False").split()

NO_LOAD = getenv("NO_LOAD", "").split()

TOKEN = getenv("TOKEN", "5920443941:AAG1UJMR9X7QvM-wUH617Bz8pU-MRqlpM8E")

MONGO_DB_URL = getenv(
    "MONGO_DB_URL",
    "mongodb+srv://Lallumic: Lallumic@cluster0.hwfluz1.mongodb.net/?retryWrites=true&w=majority",
)
