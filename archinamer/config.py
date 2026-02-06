import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    API_KEY = os.getenv("DASHSCOPE_API_KEY")
    DEFAULT_MODEL = "qwen-plus"
    BASE_URL = "https://dashscope.aliyuncs.com/compatible-mode/v1"
    # We can inject your background here to ground the AI
    USER_PROFILE = "Senior Backend Engineer (Java, Spring Boot, K8s, AI Agents)"