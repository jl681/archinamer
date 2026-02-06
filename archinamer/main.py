import sys
import os
import subprocess
from .consultant import NamingConsultant

def run():
    if len(sys.argv) < 2:
        print("Usage: archinamer 'your project idea'")
        return

    idea = " ".join(sys.argv[1:])
    consultant = NamingConsultant()

    print("\n🔍 Architect is analyzing your idea...")
    questions = consultant.ask_clarifications(idea)
    
    print(f"\n{questions}")
    context = input("\n📝 Your details: ")

    print("\n🏗️ Generating architectural name...")
    repo_name = consultant.generate_name(idea, context)

    confirm = input(f"✨ Suggested Name: '{repo_name}'. Initialize folder? (y/n): ")
    
    if confirm.lower() == 'y':
        os.makedirs(repo_name, exist_ok=True)
        # Standard init commands
        subprocess.run(["git", "init", repo_name], check=True)
        with open(f"{repo_name}/README.md", "w") as f:
            f.write(f"# {repo_name}\n\n{idea}\n\n**Context:** {context}")
        print(f"✅ Created /{repo_name}")

if __name__ == "__main__":
    run()