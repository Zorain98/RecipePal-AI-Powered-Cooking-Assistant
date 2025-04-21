# 👨🏻‍🍳 RecipePal: AI Powered Cooking Assistant

RecipePal is a smart cooking assistant that suggests personalized recipes based on the ingredients you have available in your kitchen. No more food waste or unplanned grocery trips!

## Features

- **Ingredient-Based Recipe Generation**: Enter the ingredients you have on hand, and RecipePal will craft a delicious recipe tailored to your available items
- **Simple, User-Friendly Interface**: Clean Streamlit UI makes recipe discovery a breeze
- **Powered by AI**: Leverages OpenAI's GPT-3.5 Turbo model through LangChain for intelligent recipe creation

## How It Works

RecipePal takes your available ingredients as input, passes them to a sophisticated AI model trained on culinary knowledge, and returns custom recipe suggestions complete with preparation instructions.

## Tech Stack

- **Frontend**: Streamlit
- **AI Implementation**: LangChain + OpenAI's GPT-3.5 Turbo
- **Dependencies**: langchain, streamlit, langchain_openai

## Getting Started

1. Clone this repository
2. Install dependencies: `pip install -r requirements.txt`
3. Set up your OpenAI API key in the Streamlit secrets
4. Run the app: `streamlit run app.py`

## Usage

1. Enter your available ingredients, separated by commas
2. Click "Get Recipe"
3. Enjoy your AI-crafted recipe suggestion!

## Contributing

Contributions are welcome! Feel free to submit a pull request or open an issue to suggest improvements or report bugs.

## License

[MIT License](LICENSE)
