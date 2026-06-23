from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"mensaje:" "Ssitema academico api funcionando"}