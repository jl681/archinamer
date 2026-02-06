from openai import OpenAI
from .config import Config

class NamingConsultant:
    def __init__(self):
        self.client = OpenAI(
            api_key=Config.API_KEY,
            base_url=Config.BASE_URL,
        )

    def ask_clarifications(self, idea):
        """
        Phase 1: Acts as a Senior Architect to narrow down the project's scope and intent.
        """
        prompt = f"""
        User Idea: "{idea}"
        Role: Senior Architect. 
        Context: User is a {Config.USER_PROFILE}.
        
        Task: Ask 2-3 specific, high-signal questions to distinguish:
        1. Scope: Is this a personal experimental tool or an enterprise-grade production service?
        2. Interface: Is it a headless Library/CLI, or does it require a UI (Web/Mobile)?
        3. Tech Stack: Any specific architectural preferences (e.g., Microservices vs. Monolith)?
        
        Keep it professional, brief, and developer-centric.
        """
        completion = self.client.chat.completions.create(
            model=Config.DEFAULT_MODEL, 
            messages=[
                {"role": "system", "content": "You are a Senior Technical Lead specializing in system design and project bootstrapping."},
                {"role": "user", "content": prompt}
            ]
        )
        return completion.choices[0].message.content

    def generate_name(self, idea, context):
        """
        Phase 2: Synthesizes the initial idea and user context into a professional GitHub repository name.
        Applies industry-standard kebab-case and suffix conventions.
        """
        prompt = f"""
        Initial Idea: {idea}
        User Context: {context}
        
        Task: Suggest ONE ideal, professional kebab-case repository name based on industry standards:
        - Format: Strictly kebab-case (lowercase, hyphens).
        - Length: Max 3-4 words.
        - Redundancy: DO NOT use words like 'project', 'repo', or 'my-'.
        - Suffix Strategy:
            * Backend: use '-api', '-service', or '-core'.
            * Frontend: use '-ui', '-web', or '-app'.
            * Tools/CLIs: use '-cli', '-tool', or '-utils'.
            * Libraries: use '-lib' or '-sdk'.
            * Demos/Samples: use '-demo' or '-poc'.
        
        Response Requirement: Return ONLY the raw string of the name. No explanation, no quotes.
        """
        completion = self.client.chat.completions.create(
            model=Config.DEFAULT_MODEL, 
            messages=[
                {"role": "system", "content": "You are a naming expert for high-quality GitHub repositories. You output only the final string."},
                {"role": "user", "content": prompt}
            ]
        )
        return completion.choices[0].message.content.strip().replace('"', '').replace("'", "")