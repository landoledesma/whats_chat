import sett
import services
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return "hola desde fastapi"

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app)
    
