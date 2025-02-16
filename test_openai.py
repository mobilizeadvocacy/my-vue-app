from openai import OpenAI

client = OpenAI(api_key="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")
import speech_recognition as sr

# Set your OpenAI API key directly (for testing only – consider using environment variables for production)

def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for your speech...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        print("Processing...")
    try:
        text = recognizer.recognize_google(audio)
        print("You said:", text)
        return text
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand that.")
        return None
    except sr.RequestError:
        print("Could not request results from Google Speech Recognition service.")
        return None

def generate_letter_from_speech():
    text = speech_to_text()
    if text:
        prompt = f"Please generate a formal letter based on the following input: {text}. Write it as a professional and formal letter."
        response = client.chat.completions.create(model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ])
        letter = response.choices[0].message.content
        print("Generated Letter:")
        print(letter)
    else:
        print("No speech input received, cannot generate letter.")

# Run the program
generate_letter_from_speech()
