from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from models import AnalysisRequest, AnalysisResponse, DetectedCommand, CommandType, RiskLevel
from patterns import DETECTION_PATTERNS
import uuid
import re
from datetime import datetime
from typing import List


app = FastAPI(
    title="VeritasAI - LLM Security Filter", 
    version="1.0.0",
    description="Security gateway that prevents LLMs from executing dangerous commands"
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



    

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)