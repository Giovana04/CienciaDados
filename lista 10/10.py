import pandas as pd
from tqdm import tqdm

tqdm.pandas()
df = pd.DataFrame({'coluna': range(1000)})
df['nova'] = df['coluna'].progress_apply(lambda x: x * 2)