"""CTP 2 - Exercise 1 STARTER: profile customers.csv with pandas.
Run from the 02_CTP2 folder:  python profile_customers_starter.py
Goal: measure at least 8 rules (2 per dimension) and copy the numbers into quality_scorecard_template.csv
"""
import pandas as pd

df = pd.read_csv("../shopfast-kit/data/customers.csv", dtype=str)   # dtype=str: keep the raw text (e.g. 01300)
n = len(df)
print("Rows:", n)
print(df.head())

# --- Completeness: how many empty values per column? ---
print("\nEmpty values per column:\n", df.isna().sum())

# --- Uniqueness: is customer_id unique? ---
print("\nDuplicated customer_id rows:", df["customer_id"].duplicated(keep=False).sum())

# TODO 1 (Uniqueness): normalise email (strip + lower case) and count people registered twice
print(f"\nDuplicated email rows: {df["email"].duplicated(keep=False).sum()} before step 1")
df["email"] = df["email"].str.lower()
df["email"] = df["email"].str.strip(" ")
df = df.drop_duplicates(subset = ["email"])
print(f"Duplicated email rows: {df["email"].duplicated(keep=False).sum()} after step 1")

# TODO 2 (Validity): count emails that do not match the regex  ^[^@\s]+@[^@\s]+\.[a-zA-Z]{2,}$   (hint: .str.match)
masque_valide = df["email"].str.match(r"^[^@\s]+@[^@\s]+\.[a-zA-Z]{2,}$", na=False)
print(f"\nCount of Email not respecting the standard email format: {len(df.loc[~masque_valide, "email"])}")

# TODO 3 (Consistency): list the distinct values of country with value_counts() - how many spellings for 4 countries?
country = df["country"].value_counts()
print(country)
# France: 5 | Allemagne : 4 | Belgique : 4 | Espagne : 4

# TODO 4 (Consistency): count signup_date values that are NOT in the format YYYY-MM-DD
masque_valide = df["signup_date"].str.match(r"\d{4}-\d{2}-\d{2}", na=False)
print(f"\nNumber fo signup date in the wrong format : {len(df.loc[~masque_valide, "signup_date"])}")

# TODO 5 (Validity): loyalty_tier values outside bronze / silver / gold / platinum
allowed_tier = {"bronze", "silver", "gold", "platinum"}
invalid_tier = df[~df["loyalty_tier"].isin(allowed_tier)]["loyalty_tier"]
print(f"\nNumber of invalid tier : {len(invalid_tier)}")

# TODO 6 (Accuracy): birth dates in the future or before 1906 (convert the ISO ones with pd.to_datetime)
anniversary = pd.to_datetime(df["birth_date"], format='mixed')
print(f"\nNumber of invalid birth date : {len([birthday for birthday in anniversary if birthday.year < 1906 or birthday > pd.Timestamp.today().normalize()])}")

# TODO 7 (Validity): French postal codes that do not have 5 digits
french_postal_codes = df.loc[df["country"] == "France", "postal_code"]
invalid_postal_codes = french_postal_codes[~french_postal_codes.str.match(r"^\d{5}$", na=False)]
print(f"\nNumber of invalid postal codes in France : {len(invalid_postal_codes)}")

# Bonus: compute score_pct = 100 * (1 - failing_rows / n) for each rule
