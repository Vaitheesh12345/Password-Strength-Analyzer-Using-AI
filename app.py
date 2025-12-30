import gradio as gr
import re

def analyze_password(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter")

    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("Add at least one number")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Add at least one special character")

    if score <= 2:
        strength = "❌ Weak Password"
    elif score <= 4:
        strength = "⚠️ Medium Password"
    else:
        strength = "✅ Strong Password"

    result = f"Password Strength: {strength}\n\nSuggestions:\n"

    if feedback:
        for tip in feedback:
            result += f"- {tip}\n"
    else:
        result += "- Your password is strong and secure"

    return result


demo = gr.Interface(
    fn=analyze_password,
    inputs=gr.Textbox(type="password", label="Enter Password"),
    outputs=gr.Textbox(label="Result"),
    title="🔐 Password Strength Analyzer using AI",
    description="Checks password strength and gives security suggestions"
)

if __name__ == "__main__":
    demo.launch()
