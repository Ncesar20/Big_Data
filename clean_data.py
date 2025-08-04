import pandas as pd

# Load your original dataset
df = pd.read_csv("data/bdsp_psg_master.csv")

# Drop unnecessary columns
df = df.drop(columns=["HashFolderName", "BDSPLastModifiedDTS"])

# Convert datetime
df["ShiftedCreationTime"] = pd.to_datetime(df["ShiftedCreationTime"], errors='coerce')

# Standardize values
df["PreSleepQuestionnaire"] = df["PreSleepQuestionnaire"].replace({"Y": "Yes", "N": "No"})
df["HasAnnotations"] = df["HasAnnotations"].replace({"Y": "Yes", "N": "No"})
df["HasStaging"] = df["HasStaging"].replace({"Y": "Yes", "N": "No"})
df["SexDSC"] = df["SexDSC"].str.capitalize()

# Drop missing StudyType
df = df.dropna(subset=["StudyType"])

# Drop duplicates
df = df.drop_duplicates()
import pandas as pd

# Load your original dataset
df = pd.read_csv("notebooks/cleaned_bdsp_psg_master.csv")

# ...existing cleaning code...

# Add count of StudyType as a new column
df['Count'] = df.groupby('StudyType')['StudyType'].transform('count')


# Save cleaned file
df.to_csv("notebooks/cleaned_bdsp_psg_master.csv", index=False)
