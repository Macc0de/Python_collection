import plotly.express as px
import pandas as pd
import os


path = "udemy_courses_extended.csv"
if not os.path.exists(path):
    print('Файл не найден!')
    exit()

with open(path) as file:
    if os.fstat(file.fileno()).st_size:
        df = pd.read_csv(path, sep=",")
    else:
        print('Файл пуст!')
        exit()

# (1)
fig = px.histogram(df, x="is_paid", y="num_subscribers",
                   color='is_paid', barmode='group',
                   height=400,
                   histfunc="count",
                   text_auto=True,
                   title="Количество платных и бесплатных курсов",
                   )

# (2)
fig2 = px.histogram(df, x="is_paid", y="num_subscribers",
                    color='is_paid', barmode='group',
                    height=400,
                    histfunc="max",
                    text_auto=True,
                    title="Максимальное количество подписчиков"
                    )

fig3 = px.histogram(df, x="is_paid", y="num_subscribers",
                    color='is_paid', barmode='group',
                    height=400,
                    histfunc="avg",
                    text_auto=True,
                    title="Среднее количество подписчиков"
                    )

fig4 = px.histogram(df, x="is_paid", y="num_subscribers",
                    color='is_paid', barmode='group',
                    height=400,
                    histfunc="min",
                    text_auto=True,
                    title="Минимальное количество подписчиков"
                    )

fig.show()
fig2.show()
fig3.show()
fig4.show()

# (3)
paid = df[df["is_paid"] == True]
unpaid = df[df["is_paid"] == False]

# Платные курсы
fig4 = px.histogram(paid, x="level", y="course_title",
                    color='level', barmode='group',
                    height=400,
                    histfunc="count",
                    text_auto=True,
                    title="Количество курсов по уровням (Только платные)"
                    )

fig4.show()

# Бесплатные
fig5 = px.histogram(unpaid, x="level", y="course_title",
                    color='level', barmode='group',
                    height=400,
                    histfunc="count",
                    text_auto=True,
                    title="Количество курсов по уровням (Только бесплатные)"
                    )

fig5.show()
