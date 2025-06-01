import streamlit as st
import re
from google import gemini
from google.genai import types
from PIL import Image
from io import BytesIO
import base64
import mimetypes
from config import key

client = genai.Client(api_key=key)

def ispromptsafe(prompt: str) -> bool:
    forbidden = [
        "violence", "weapon", "gun", "blood", "nude", "porn", "penis", "vagina", "boobs", "drugs", "hate", "rascim", "sex",
        "child abuse", "bomb", "abuse", "kill", "death", "suicide", "unalive", "self-harm", "self harm", "hate speech"
    ]
    pattern = re.compile("|".join(forbidden), re.IGNORECASE)
    return not bool(pattern.search(prompt))

def generate(prompt: str):
    if not ispromptsafe(prompt):
        return None, "Your prompt contains restricted or unsafe content. Please modify and try again."
    try:
        