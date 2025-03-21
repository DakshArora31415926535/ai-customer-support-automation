import re
from textblob import TextBlob
import pandas as pd
from transformers import pipeline
from transformers import pipeline
import os
from langdetect import detect
from deep_translator import GoogleTranslator
# Set up OpenAI client
qa_feedback_generator = pipeline("text-generation", model="google/flan-t5-large")  # Replace with your actual API key
# Load a grammar correction model
grammar_corrector = pipeline("text2text-generation", model="vennify/t5-base-grammar-correction")
def detect_and_translate(text, target_lang='en'):
    try:
        detected_lang = detect(text)
        if detected_lang != target_lang:
            translated_text = GoogleTranslator(source=detected_lang, target=target_lang).translate(text)
            return translated_text, detected_lang
        return text, detected_lang
    except Exception as e:
        print(f"Error detecting/translating language: {e}")
        return text, "unknown"
def generate_ai_feedback(agent_name, interaction_summary, strengths, weaknesses, score):
    """Generates AI-powered, human-like feedback for the specialist using a free Hugging Face model."""
    prompt = f"""
    You are a QA specialist providing constructive feedback to a customer service agent. 
    The feedback should be professional, actionable, and motivational.
    Agent Name: {agent_name}
    **Interaction Summary:** {interaction_summary}
    **Strengths:** {strengths}
    **Areas for Improvement:** {weaknesses}
    **QA Score:** {score}%
    Provide a structured feedback summary.
    """
    feedback = qa_feedback_generator(prompt, max_length=250, truncation=True)[0]["generated_text"]
    return feedback
    # Extract response correctly for OpenAI v1.0.0+
    return response.choices[0].message.content


def evaluate_email(email, guest_email):
    score_details = []
    total_score = 0

    # Accuracy
    if "correct" in email.lower():
        score_details.append("Accuracy (5): The response includes 'correct', ensuring factual correctness.")
        total_score += 5
    else:
        score_details.append("Accuracy (2): The response lacks 'correct', making accuracy uncertain.")
        total_score += 2

    # Communication Style
    if "thank you" in email.lower():
        score_details.append("Communication Style (5): 'Thank you' is present, adding politeness.")
        total_score += 5
    else:
        score_details.append("Communication Style (2): 'Thank you' is missing, reducing courtesy.")
        total_score += 2

    # Clarity & Language
    corrected_email = email  # Assuming some grammar correction tool is applied
    if corrected_email != email:
        score_details.append("Clarity & Language (5): The response needed corrections, and they were made.")
        total_score += 5
    else:
        score_details.append(
            "Clarity & Language (2): The response had no changes, indicating no explicit grammar improvements.")
        total_score += 2

    # Customer-Centric Approach
    if "help" in email.lower():
        score_details.append("Customer-Centric Approach (5): 'Help' is present, showing a supportive tone.")
        total_score += 5
    else:
        score_details.append(
            "Customer-Centric Approach (2): The email lacks 'help', reducing its customer-friendly tone.")
        total_score += 2

    # Message Comprehension
    first_ten_words = set(guest_email.lower().split()[:10])
    if any(word in email.lower().split() for word in first_ten_words):
        score_details.append(
            "Message Comprehension (5): The response reflects the guest’s message, ensuring understanding.")
        total_score += 5
    else:
        score_details.append(
            "Message Comprehension (2): No words from the guest’s message were found, suggesting a lack of understanding.")
        total_score += 2

    # Message Personalization
    if "dear" in email.lower():
        score_details.append("Message Personalization (5): 'Dear' is used, making the email more personal.")
        total_score += 5
    else:
        score_details.append("Message Personalization (2): 'Dear' is missing, making the email feel less personal.")
        total_score += 2

    # Correct Macro Utilization
    if "macro" in email.lower():
        score_details.append(
            "Correct Macro Utilization (5): The word 'macro' is included, indicating correct template usage.")
        total_score += 5
    else:
        score_details.append(
            "Correct Macro Utilization (2): 'Macro' is missing, suggesting incorrect or missing template use.")
        total_score += 2

    # Ticket Handling / Support Provided
    if "support" in email.lower():
        score_details.append("Ticket Handling / Support (5): 'Support' is mentioned, ensuring proper issue resolution.")
        total_score += 5
    else:
        score_details.append(
            "Ticket Handling / Support (2): The response lacks 'support', making it seem less helpful.")
        total_score += 2

    print("\n--- Evaluation Feedback ---")
    for detail in score_details:
        print(detail)
    print(f"\nTotal Score: {total_score}/40")

    # Print the perfect email
    print("\n--- Ideal Response for Full Score ---")
    perfect_email = (
        "Dear [Guest's Name],\n\n"
        "Thank you for reaching out to us. We understand your concern and are happy to help.\n"
        "The correct macro for your request is included below. Please follow the steps outlined.\n"
        "If you need any further support, feel free to reach out to us anytime.\n\n"
        "Best regards,\n[Your Name]"
    )
    print(perfect_email)


# Example Usage
guest_msg = "I need help with my booking. Can you confirm the details?"
specialist_email = "Dear customer, thank you for reaching out. We are happy to help. Please check the correct macro for your request."
evaluate_email(specialist_email, guest_msg)
