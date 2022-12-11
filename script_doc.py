from docxtpl import DocxTemplate
from datetime import datetime, date
import pandas as pd

doc = DocxTemplate("template.docx")

t_date = date.today().strftime("%d.%m.%y")
#t_date = "12.12.2022"

my_context = { 't_date' : t_date }

df = pd.read_excel('collegue.xlsx')

for index, row in df.iterrows():
    context = {'c_name': row['name'], 
    'post' : row['post'],
    'region' : row['region']
    }

    context.update(my_context)

    doc.render(context)
    doc.save(f"mts_doc{index}.docx")