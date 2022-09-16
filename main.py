# Importacion de Modulos (Externas)
from fastapi import FastAPI
from fastapi import FastAPI
import uvicorn
# Importacion de Modulos (Internos)
from routes.race import race_route
# from routes.driver import driver_route
# from routes.result import result_route


app = FastAPI(
    title='Proyecto Individual (PI HENR)Y - @royquillca',
    description='Version 0.0.1',
    version='0.0.1',
    openapi_tags=[{
        'name': 'users',
        'description': 'Users routes',
    }]
)

app.include_router(race_route)
# app.include_router(piloto.router)
# app.include_router(resultado.router)
# app.include_router(circuito.router)

@app.get("/")
def root():
    return {'Hello Everything is OKAY :)'}

if __name__ == '__main__':
    uvicorn.run('main:app', port=8000, reload=True)