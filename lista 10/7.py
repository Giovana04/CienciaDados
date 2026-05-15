import time
from tqdm import tqdm

for i in tqdm(range(10), desc="Processando"):
    time.sleep(0.5)
