import pandas as pd
import tabula
from tabula import read_pdf
file_path = "/mnt/g/Book/Biology/Дубровский/aref_Dubrovski.pdf"
df = read_pdf(file_path, pages='all')
print(f'Number of Tables=  {len(df)}')

