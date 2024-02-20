from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, ValidationError
from typing import Optional, Dict, List
from elasticsearch import Elasticsearch

app = FastAPI()

# Elasticsearch configuration
es = Elasticsearch("http://localhost:9200")
index_name = "students"

class StudentCreate(BaseModel):
    name: str
    age: int
    grade: int
    marks: Optional[Dict[str, int]] = None

    class Config:
        # Allow/Forbid extra fields in the input data
        extra = "forbid"

class StudentUpdate(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    grade: Optional[int] = None
    marks: Optional[Dict[str, int]] = None

    class Config:
        # Allow extra fields in the input data
        extra = "forbid"

class StudentDetail(BaseModel):
    id: str
    name: str
    age: int
    grade: int
    marks: Optional[Dict[str, int]] = None

@app.post("/student", response_model=StudentDetail)
def create_student(student: StudentCreate):
    # Indexing student record in Elasticsearch
    doc_id = None  # Elasticsearch will generate its own document ID
    body = {
        "name": student.name,
        "age": student.age,
        "grade": student.grade,
        "marks": student.marks
    }
    try:
        res = es.index(index=index_name, id=doc_id, body=body)
        body['id'] = res['_id']
        return body
    except Exception as e:
        raise HTTPException(status_code=500, detail="Failed to create student record in Elasticsearch")

@app.put("/student/{student_id}", response_model=StudentDetail)
def update_student(student_id: str, student: StudentUpdate):
    # Updating student record in Elasticsearch with partial updates
    try:
        existing_student = es.get(index=index_name, id=student_id)['_source']
    except Exception:
        raise HTTPException(status_code=404, detail="Student record not found")

    updated_fields = {}
    for field, value in student.dict().items():
        if value is not None:
            updated_fields[field] = value

    try:
        res = es.update(index=index_name, id=student_id, body={"doc": updated_fields})
        updated_student = {**existing_student, **updated_fields}
        updated_student['id'] = student_id
        return updated_student
    except Exception as e:
        raise HTTPException(status_code=500, detail="Failed to update student record in Elasticsearch")

@app.get("/student/{student_id}", response_model=StudentDetail)
def get_student(student_id: str):
    # Retrieving student record from Elasticsearch
    try:
        res = es.get(index=index_name, id=student_id)
        student_data = res['_source']
        student_data['id'] = student_id
        return student_data
    except Exception as e:
        raise HTTPException(status_code=404, detail="Student record not found")

@app.get("/students/", response_model=List[StudentDetail])
def list_students():
    # Retrieving all student records from Elasticsearch
    try:
        res = es.search(index=index_name, body={"query": {"match_all": {}}})
        student_list = []
        for hit in res["hits"]["hits"]:
            student_data = hit["_source"]
            student_data['id'] = hit["_id"]
            student_list.append(student_data)
        return student_list
    except Exception as e:
        raise HTTPException(status_code=500, detail="Failed to list student records from Elasticsearch")
