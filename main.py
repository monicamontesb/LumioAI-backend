from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
 

app = FastAPI(title="Lumio MVP")

# CORS Permission
origins = [
    "http://localhost:5173",  # frontend
    "http://127.0.0.1:5173",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # permite GET, POST, OPTIONS, etc.
    allow_headers=["*"],
)


# GET: reading backend
@app.get("/")
def read_root():
    return {"message": "Lumio Backend is working!"}

from pydantic import BaseModel
# Question Model
class Question(BaseModel):
    role: str
    question: str

# Example Data for MVP
faqs = {
    "developer": {
        "Where is the API documentation?": "You can find it in the project docs folder.",
        "How do I set up my dev environment?": "Follow the setup guide in the repo README."
    },
    "analyst": {
        "How do I access datasets?": "Check the Data Lake instructions in Confluence.",
        "What BI tools are used?": "We mainly use Power BI and Tableau."
    }
}

learning_plans = {
    "developer": ["Setup dev environment", "Read API docs", "Complete first feature"],
    "analyst": ["Access datasets", "Learn BI tools", "Build first report"]
}

#POST: to answer questions
@app.post("/ask")
def ask_question(q: Question):
    responses = faqs.get(q.role.lower(), {})
    answer = responses.get(q.question, "Sorry, I don't have an answer for that yet.")
    return {"answer": answer}

#GET: to read the learning plan
@app.get("/learning-plan/{role}")
def get_learning_plan(role: str):
    plan = learning_plans.get(role.lower(), ["No plan available for this role"])
    return {"plan": plan}