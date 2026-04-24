# Install
!pip install -q google-generativeai

# Imports
import google.generativeai as genai
import random
import time

# Configure API
genai.configure(api_key="YOUR_NEW_API_KEY")

# Use a valid model from your available list
model = genai.GenerativeModel("gemini-2.5-flash")

# -------------------------------
# Add noise (forward process)
# -------------------------------
def add_noise(text):
    words = text.split()
    words = [w for w in words if random.random() > 0.2]
    random.shuffle(words)
    return " ".join(words)

# -------------------------------
# Refine idea (reverse process)
# -------------------------------
def refine_text(text, goal, retries=3):
    prompt = f"""
You improve ideas step by step.

Goal:
{goal}

Current idea:
{text}

Improve it:
- make it clear
- structure it
- make it realistic
- keep it concise

Return only the improved idea.
"""

    for attempt in range(retries):
        try:
            response = model.generate_content(prompt)
            return response.text.strip()
        
        except Exception as e:
            print(f"Retry {attempt+1} due to error:", e)
            time.sleep(10)

    return "Failed to refine."

# -------------------------------
# Diffusion loop
# -------------------------------
def diffusion_agent(goal, steps=3):
    current = f"random vague idea about {goal}"
    history = []

    for step in range(steps):
        print(f"\nSTEP {step+1}")
        
        noisy = add_noise(current)
        print("Noisy idea:\n", noisy)
        
        refined = refine_text(noisy, goal)
        print("\nRefined idea:\n", refined)
        
        current = refined
        history.append(refined)
        
        time.sleep(5)

    return history

# -------------------------------
# Run
# -------------------------------
goal = "Build an AI startup for students"
results = diffusion_agent(goal, steps=3)

print("\nFinal Output:\n", results[-1])
