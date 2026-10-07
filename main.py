from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr

"""
Develop a simple contact form application with input fields for Name, Email,
and Message. The submitted data should be securely stored in a database.
"""
app = FastAPI

contact = []


class Contact(BaseModel):
    name: str
    email: EmailStr
    message: str


@app.post("/contact")
def add_contact(contact: Contact):
    for c in contact:
        if c in contact:
            raise HTTPException(
                status_code=404, message="contact already exit"
            )
        else:
            new_contact = ("id", len(contact)+1)
            contact.append(new_contact)
            return contact


@app.get("/contact")
def get_all_contact(contact):
    return contact


@app.delete("/contact/{contact_id}")
def delete(contact):
    for c in contact:
        if c == contact:
            contact.remove(c)
        else:
            raise HTTPException(
                status_code=404, message="data not found")


