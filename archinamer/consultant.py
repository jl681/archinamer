from openai import OpenAI
from .config import Config

class NamingConsultant:
    def __init__(self):
        self.client = OpenAI(
        # 若没有配置环境变量，请用阿里云百炼API Key将下行替换为: api_key="sk-xxx",
        api_key=Config.API_KEY,
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
    )


    def ask_clarifications(self, idea):
        prompt = f"""
        User Idea: "{idea}"
        Role: Senior Architect. 
        Context: User is a {Config.USER_PROFILE}.
        
        Task: Ask 2-3 specific questions to distinguish if this is:
        - A personal side project vs. Enterprise-grade service.
        - A CLI tool, a Library, or a full Web App (UI + API).
        - A specific tech stack (e.g., Spring Boot vs. FastAPI).
        
        Keep it professional and concise.
        """
        completion = self.client.chat.completions.create(
        model=Config.DEFAULT_MODEL, 
        messages=[
            {"role": "system", "content": "You are a helpful assistant that asks clarifying questions."},
            {"role": "user", "content": prompt}
        ]
    )
        return completion.choices[0].message.content

    def generate_name(self, idea, context):
        prompt = f"""
        Finalizing name for: {idea}
        Context provided: {context}
        
        Rules:
        - Return ONLY the kebab-case name.
        - No "Project" or "Repo" words.
        - Match the scale (e.g., use '-core' for enterprise, '-lite' or '-cli' for tools).
        """
        completion = self.client.chat.completions.create(
        model=Config.DEFAULT_MODEL, 
        messages=[
            {"role": "system", "content": "You are a helpful assistant that asks clarifying questions."},
            {"role": "user", "content": prompt}
        ]
        )
        return completion.choices[0].message.content