from fastapi import FastAPI, Depends, Form, Header, HTTPException
from database import find_contact
from auth import check_auth
app = FastAPI()

@app.get("/")
async def root():
    return {
        "This is an app for storing contacts. Please do not add any real contacts."
    }

@app.get("/contact",
    summary="Get a certain contact",
    description="If you have permission this will return either all contact information for a given person (defined by name, surname)",
)
async def get_the_contact(
    name :str = Form(..., description="Contact name"), surname:str = Form(..., description="Contact surname"), auth = Header(None)
):
    if not check_auth(auth):
        raise HTTPException(status_code=401, detail="Unauthorized access - check the auth.")
    if not name or not surname:
        raise HTTPException(status_code=400, detail="Missing parametr 'name' or 'surname'")
    try:
        contacts = find_contact(name, surname)
        if contacts == []:
            raise HTTPException(status_code = 404, detail="No contact was found")
        return contacts
    except ConnectionAbortedError as e:
        raise HTTPException(status_code=500, detail="Unable to connect to database")