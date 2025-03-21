# AI Customer Support Automation

This project implements a modular system to enhance and partially automate customer support workflows using AI.

## Key Components

1. **Email Response Evaluation**  
   A pipeline that analyzes customer support emails and scores them across key dimensions like:
   - Sentiment
   - Clarity
   - Personalization
   - Correctness  
   This is designed to help review and improve agent replies.

2. **Multilingual Support**  
   Includes language detection and translation functionality using external APIs.  
   Automatically identifies the language of incoming queries and translates both incoming and outgoing messages to ensure smooth communication.

3. **Text Classification**  
   Classifies incoming emails into categories to guide routing or template selection.

4. **Feedback Generation with FLAN-T5**  
   Uses a fine-tuned FLAN-T5 model to generate structured, real-time feedback for support agents based on their response.

5. **Macro Selection Automation**  
   Automatically suggests or applies the correct response macro/template based on query classification.

## Status

The codebase is structured but still under development.  
Each module can be tested independently before full pipeline integration.

## Tech Stack

- Python  
- FLAN-T5 (via HuggingFace Transformers)  
- spaCy / TextBlob / langdetect  
- Google Translate API (or similar)  
- scikit-learn  
- pandas / numpy

## Notes

- No frontend or deployment code included.
- Focus is on backend logic and evaluation automation.
- External API keys may be needed for language and translation services.
