from fastapi import FastAPI, HTTPException
from phone.phone import Phone

# Initialize FastAPI app
app = FastAPI()

# Initialize Phone object
phone = Phone()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Phone Info API"}

@app.get("/metadata")
def get_metadata():
    return phone.get_phone_dat_msg()

@app.get("/lookup/{phone_number}")
def lookup_phone(phone_number: str):
    phone_info = phone.find(phone_number)
    if phone_info:
        return phone_info
    else:
        raise HTTPException(status_code=404, detail="Phone number not found")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)