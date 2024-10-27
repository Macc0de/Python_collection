import plotly.express as px
import pandas as pd
import os


path = "country.csv"
if not os.path.exists(path):
    print('Файл не найден!')
    exit()

with open(path) as file:
    if os.fstat(file.fileno()).st_size:
        df = pd.read_csv(path, delimiter=',')
    else:
        print('Файл пуст!')
        exit()

df.columns = ['Country', 'Health Expenditure', 'Income', 'Inflation', 'Life Expectancy']

fig = px.imshow(df.iloc[:, 1:].T, y=df.columns[1:], x=df['Country'],
    labels={"x": "Country", "y": "Indicator", "color": "Value"},
    title="Тепловая карта стран и их показателей",
    width=800, height=600, text_auto=True)

fig.update_traces(hoverongaps=False) # Информация о каждом значении
fig.update_layout(hovermode="closest")

fig.show()
