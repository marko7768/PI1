from fastapi import FastAPI
from typing import Union
import pandas as pd
from datetime import datetime

df_games = pd.read_parquet("PI MLOps - STEAM/output_steam_games.parquet")
df_items = pd.read_parquet("PI MLOps - STEAM/australian_users_items.parquet")
df_reviews = pd.read_parquet("PI MLOps - STEAM/australian_user_reviews.parquet")

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/PlayTimeGenre/{genero}")
async def PlayTimeGenre(genero:str):
    #año con mas horas jugadas del genero
    df = df_games[df_games["genres"].apply(lambda x:genero in x if isinstance(x,list) else False)]
    df = pd.merge(df,df_items,on='item_id',how='inner')
    df2 = df.groupby('release_date')['playtime_forever'].sum()
    df2 = df2.sort_values(ascending=False)
    df3 = df2.reset_index()
    df4 = df3.drop('playtime_forever',axis=1)
    anio = df4.iloc[0,0]
    try:
        return {"genero": genero,"año":anio}
    except:
        return ""

@app.get("/UserForGenre/{genero}")
async def UserForGenre(genero:str):
    #usuario con mas horas jugadas en el genero
    df = df_games[df_games["genres"].apply(lambda x:genero in x if isinstance(x,list) else False)]
    df = pd.merge(df,df_items,on='user_id',how='inner')
    df2 = df.groupby('user_id')['playtime_forever'].sum()
    df2 = df2.sort_values(ascending=True)
    df3 = df2.reset_index()
    df3 = df3.loc['user_id']
    try:
        return {"usuario": "Hello World"}
    except:
        return ""

@app.get("/UsersRecommend/{anio}")
async def UsersRecommend(anio:int):
    #top 3 juegos recomendados por usuarios para el año
    juegos_del_anio = df_games[datetime.strptime(df_games[df_games["release_date"]],"%Y-%m-%d").year == anio]
    df = pd.merge(juegos_del_anio,df_reviews,on='item_id',how='inner')
    #df2 = df[df['recommend'] == False]
    df2 = df[df['recommend'] == True]
    df3 = df2.groupby("app_name")['recommend'].count()
    #df3 = df3.sort_values(ascending=False)
    df3 = df3.sort_values(ascending=True)
    #df4 = df3.tail(3)
    df4 = df3.head(3)
    try:
        return {"año": anio,"Juegos":df4}
    except:
        return ""

@app.get("/UsersWorstDeveloper/{anio}")
async def UsersWorstDeveloper(anio:int):
    #top 3 desarrolladoras con juegos menos recomendados por usuarios para el año
    juegos_del_anio = df_games[datetime.strptime(df_games[df_games["release_date"]],"%Y-%m-%d").year == anio]
    df = pd.merge(juegos_del_anio,df_reviews,on='item_id',how='inner')
    df2 = df[df['recommend'] == False]
    df3 = df2.groupby("developer")['recommend'].count()
    df3 = df3.sort_values(ascending=False)
    df4 = df3.tail(3)
    try:
        return {"año": anio,"desarrolladoras":df4}
    except:
        return ""


@app.get("/sentiment_analysis/{desarrolladora}")
async def sentiment_analysis(desarroladora:str):
    #analisis de sentimiento
    return ""

