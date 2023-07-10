from fastapi import FastAPI
import funcionesLocas as fl
import uvicorn


#Api structure
app = FastAPI(title='Data Engineering', description='Data Scientist Mauro Alexander Pimentel Azurin')

@app.get('/')
async def index():
    return {'API realizada por Mauro Alexander Pimentel'}

@app.get('/about/')
async def about():
    return {'Data Engineering'}

@app.get('/get_word_count/({keyword}_{platform})')
async def get_word_count(keyword:str,plataforma:str):
    '''keyword = Cualquier palabra; plataforma = [Hulu, Netflix, Amazon, Disney]'''
    return fl.get_word_count(keyword, plataforma)

@app.get('/get_score_count/({platform}_{score}_{year})')
async def get_score_count(plataforma:str,puntaje:int, anio:int):
    '''plataforma = [Hulu, Netflix, Amazon, Disney], puntaje = [0 a 100], anio = Año'''
    return fl.get_score_count(plataforma, puntaje, anio)

@app.get('/get_second_score/({plataforma})')
async def get_second_score(plataforma:str):
    '''plataforma = [Hulu, Netflix, Amazon, Disney]'''
    return fl.get_second_score(plataforma)

@app.get('/get_longest/({plataforma}_{min_o_season}_{anio})')
async def get_longest(plataforma:str, min_o_season:str, anio:int):
    '''plataforma = [hulu, netflix, amazon, disney], min_o_season = escoge entre min o season, anio = Año'''
    return fl.get_longest(plataforma, min_o_season, anio)

@app.get('/get_rating_count/({rating})')
async def get_rating_count(rating:str):
    '''rating = ['G' '13+' 'ALL' '18+' 'R' 'TV-Y' 'TV-Y7' 'NR' '16+' 'TV-PG' '7+' 'TV-14'
 'TV-NR' 'TV-G' 'PG-13' 'TV-MA' 'PG' 'NC-17' 'UNRATED' '16' 'AGES_16_'
 'AGES_18_' 'ALL_AGES' 'NOT_RATE' 'TV-Y7-FV' 'NOT RATED'] '''
    return fl.get_rating_count(rating)