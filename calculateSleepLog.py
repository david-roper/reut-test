import polars as pl
import pandas as pd


def date_converter(date):
    dates = {"01":"Jan","02":"Feb","03":"Mar","04":"Apr","05":"May","06":"June","07":"July","08":"Aug","09":"Sept", "10":"Oct","11":"Nov", "12":"Dec"}

    print(date[3:5])
    date = date[:3] + dates[date[3:5]] + date[5:]

    return date

df = pl.read_excel('data/formattedMorning.xlsx')

df2 = pl.read_excel('data/formattedEvening.xlsx')


df = df.slice(1)


s = "27/03/2023"

print(df)
print(df2)

print(date_converter(s))


'''
convert calculations into python code, iterate through each participants morning and evening weekly data. take those weeks of data and produce the spss lines through calculations

'''

