from fastapi import FastAPI
app = FastAPI()
@app.get("/")
async def index():
   return {"message": "Heyyyy! Changing this message for learning git"}


   
