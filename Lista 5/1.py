import pandas as pd
import matplotlib.pyplot as plt

failures = pd.read_csv("Lista 5\Falencia_Bancos.csv", sep=',', encoding='latin-1')

failures.columns = failures.columns.str.replace('\xa0', '', regex=True).str.strip()
print(failures.columns)

close_timestamps = pd.to_datetime(failures["Closing Date"], errors='coerce')
close_timestamps = close_timestamps.dropna()

failures_by_year = close_timestamps.dt.year.value_counts().sort_index()

failures_by_year.plot(kind='area')
plt.xlabel("Ano")
plt.ylabel("Numero de flencias")
plt.title("Falencia de bancos por ano")
plt.show()