# text_summarizer_gui.py

import customtkinter as ctk
from transformers import BartForConditionalGeneration, BartTokenizer
import torch

# Load model and tokenizer
def load_model():
    model_name = "facebook/bart-large-cnn"
    model = BartForConditionalGeneration.from_pretrained(model_name)
    tokenizer = BartTokenizer.from_pretrained(model_name)
    return model, tokenizer

# Summarize text function
def summarize_text(text, model, tokenizer, max_length=150, min_length=30, length_penalty=2.0, num_beams=4, early_stopping=True):
    inputs = tokenizer.encode("summarize: " + text, return_tensors="pt", max_length=1024, truncation=True)
    summary_ids = model.generate(inputs, max_length=max_length, min_length=min_length, 
                                 length_penalty=length_penalty, num_beams=num_beams, early_stopping=early_stopping)
    return tokenizer.decode(summary_ids[0], skip_special_tokens=True)

# Initialize model and tokenizer
model, tokenizer = load_model()

# Define the GUI application
class SummarizerApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Configure window
        self.title("NLP Text Summarizer")
        self.geometry("600x600")
        ctk.set_appearance_mode("light")  # Modes: "System" (default), "Dark", "Light"
        ctk.set_default_color_theme("blue")  # Themes: "blue" (default), "dark-blue", "green"

        # Create input text box
        self.input_label = ctk.CTkLabel(self, text="Enter text to summarize:", font=("Arial", 14))
        self.input_label.pack(pady=10)
        self.input_text = ctk.CTkTextbox(self, width=550, height=200)
        self.input_text.pack(pady=10)

        # Create summarize button
        self.summarize_button = ctk.CTkButton(self, text="Summarize", command=self.summarize_text)
        self.summarize_button.pack(pady=10)

        # Create output text box
        self.output_label = ctk.CTkLabel(self, text="Summary:", font=("Arial", 14))
        self.output_label.pack(pady=10)
        self.output_text = ctk.CTkTextbox(self, width=550, height=200)
        self.output_text.pack(pady=10)

    def summarize_text(self):
        # Get input text
        input_text = self.input_text.get("1.0", "end").strip()
        if not input_text:
            self.output_text.delete("1.0", "end")
            self.output_text.insert("1.0", "Please enter text to summarize.")
            return
        
        # Summarize and display output
        summary = summarize_text(input_text, model, tokenizer)
        self.output_text.delete("1.0", "end")
        self.output_text.insert("1.0", summary)

# Run the application
if __name__ == "__main__":
    app = SummarizerApp()
    app.mainloop()
