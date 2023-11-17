import uvicorn 

if __name__ == "__main__":

    # uvicorn.run("app.views:app", reload=True)

    # For production 
    uvicorn.run("app.views:app")