from fastapi import FastAPI, Depends, Form, Header, HTTPException, Response
from database import find_contact, delete_contact, create_contact
from auth import check_auth
from uuid import UUID
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
    name :str, surname:str, auth = Header(None)
):
    if not check_auth(auth):
        raise HTTPException(status_code=401, detail="Unauthorized access - check the auth.")
    if not name or not surname or name =="" or surname=="": 
        raise HTTPException(status_code=400, detail="Missing parametr 'name' or 'surname'")
    try:
        contacts = find_contact(name, surname)
        if contacts == []:
            raise HTTPException(status_code = 404, detail="No contact was found")
        return contacts
    except ConnectionAbortedError as e:
        raise HTTPException(status_code=500, detail="Unable to connect to database")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server erro: {e}")
    
@app.delete("/contact",
    summary="Delete a certain contact",
    description="If you have permission this will delete a contact idenfied by the given id.",
)
async def get_the_contact(
    id:str = Form(description="Contact surname"), auth = Header(None)
):
    if not check_auth(auth):
        raise HTTPException(status_code=401, detail="Unauthorized access - check the auth.")
    if not id:
        raise HTTPException(status_code=400, detail="Missing parametr 'id'")
    try:
        delete_contact(id)
        return Response(status_code=204)
    except ConnectionAbortedError as e:
        raise HTTPException(status_code=500, detail=f"Unable to connect to database: {e}")
    except NameError as e:
        raise HTTPException(status_code=404, detail=f"User with given id does not exist: {e}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server erro: {e}")
    

@app.post("/contact",
    summary="Add a contact",
    description="If you have permission, you can add a contact through this endpoint.",
)
async def add_contact(
    name: str = Form(..., description="Contact name"), 
    surname: str = Form(..., description="Contact surname"), 
    phone: str | None = Form(None, description="Contact phone"), 
    email: str | None = Form(None, description="Contact email"),
    address: str | None = Form(None, description="Contact address"), 
    note: str | None = Form(None, description="Contact note"),
    auth: str | None = Header(None)
):
    if not check_auth(auth):
        raise HTTPException(status_code=401, detail="Unauthorized access - check the auth.")
    if not name or not surname or name =="" or surname=="": 
        raise HTTPException(status_code=400, detail="Missing parametr 'name' or 'surname'")
    try:
        id = create_contact(name, surname, phone, email, address, note)
        return {"id": id}
    except ConnectionAbortedError as e:
        raise HTTPException(status_code=500, detail=f"Unable to connect to database: {e}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {e}")
