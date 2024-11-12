# Modern Text Summarizer

This is a GUI-based text summarizer built with `customtkinter` and the BART transformer model from Hugging Face. It provides a modern, dark-themed interface that allows users to input text and receive a concise summary.

## Features
- **Text Summarization**: Uses the BART transformer model for high-quality text summarization.
- **Modern GUI**: Built with `customtkinter` for a clean, dark-mode look.
- **Easy-to-Use**: A single file, self-contained application.

## Screenshots
![GUI Screenshot](screenshot.png)

## How It Works
1. Enter the text you want to summarize in the input box.
2. Click the "Summarize" button.
3. The summary will be displayed in the output box.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/modern-text-summarizer.git
    cd modern-text-summarizer
    ```

2. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the application:
    ```bash
    python text_summarizer_gui.py
    ```

## Dependencies
- `transformers` (for the BART model)
- `torch` (for model support)
- `customtkinter` (for the modern GUI)

## Converting to an Executable
To create an executable file, use `pyinstaller`:
```bash
pyinstaller --onefile --windowed text_summarizer_gui.py
