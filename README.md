# 🤖 AI Chatbot with LangChain & Streamlit

A modern chatbot application built with LangChain and Streamlit, featuring a clean interface and streaming responses from OpenAI's GPT models.

## Features

- 💬 Real-time chat interface with streaming responses
- 🔄 Multiple GPT model support (GPT-3.5-turbo, GPT-4, GPT-4-turbo)
- ⚙️ Adjustable temperature settings for response creativity
- 💾 Persistent chat history during session
- 🎨 Clean and responsive UI
- 🔒 Secure API key handling

## Prerequisites

- Python 3.8 or higher
- OpenAI API key ([Get one here](https://platform.openai.com/api-keys))

## Local Installation

1. **Clone or download this repository**

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up your API key**
   
   Option A - Environment Variable:
   ```bash
   # Copy the example env file
   cp .env.example .env
   
   # Edit .env and add your OpenAI API key
   OPENAI_API_KEY=your_api_key_here
   ```
   
   Option B - Enter in the app:
   - You can also enter your API key directly in the app's sidebar

4. **Run the application**
   ```bash
   streamlit run app.py
   ```

5. **Open your browser**
   - The app will automatically open at `http://localhost:8501`

## Deploying to Streamlit Cloud

### Step 1: Prepare Your Repository

1. Create a GitHub repository with your code
2. Ensure these files are included:
   - `app.py`
   - `requirements.txt`
   - `.gitignore`
   - `README.md` (this file)

### Step 2: Deploy to Streamlit Cloud

1. Go to [share.streamlit.io](https://share.streamlit.io)

2. Sign in with your GitHub account

3. Click "New app"

4. Configure your app:
   - **Repository**: Select your GitHub repository
   - **Branch**: `main` (or your default branch)
   - **Main file path**: `app.py`

5. Click "Advanced settings" and add your secrets:
   ```toml
   OPENAI_API_KEY = "your_openai_api_key_here"
   ```

6. Click "Deploy!"

7. Your app will be live at `https://[your-app-name].streamlit.app`

### Step 3: Updating Your Deployed App

The app will automatically redeploy when you push changes to your GitHub repository.

## Usage

1. **Enter API Key**: If not set as an environment variable, enter your OpenAI API key in the sidebar

2. **Select Model**: Choose from available GPT models (default: GPT-3.5-turbo)

3. **Adjust Temperature**: Control response creativity (0.0 = focused, 2.0 = creative)

4. **Start Chatting**: Type your message in the chat input and press Enter

5. **Clear History**: Use the "Clear Chat History" button to start a new conversation

## Project Structure

```
chatbot-app/
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies
├── .env.example       # Example environment variables
├── .gitignore         # Git ignore file
└── README.md          # This file
```

## Technologies Used

- **Streamlit**: Frontend framework for the web interface
- **LangChain**: Framework for building LLM applications
- **OpenAI API**: Powers the AI responses
- **Python**: Programming language

## Configuration

### Model Options

- `gpt-3.5-turbo`: Fast and cost-effective (recommended for most use cases)
- `gpt-4`: More capable but slower and more expensive
- `gpt-4-turbo-preview`: Latest GPT-4 with improved performance

### Temperature Settings

- **0.0-0.3**: More focused and deterministic responses
- **0.7-1.0**: Balanced creativity and coherence (default: 0.7)
- **1.5-2.0**: More creative and varied responses

## Troubleshooting

### API Key Issues
- Ensure your API key is valid and has available credits
- Check that the key is properly set in the sidebar or environment

### Installation Issues
- Make sure Python 3.8+ is installed
- Try upgrading pip: `pip install --upgrade pip`
- Install dependencies in a virtual environment

### Deployment Issues
- Verify all files are pushed to GitHub
- Check that secrets are properly configured in Streamlit Cloud
- Review the deployment logs for specific errors

## Cost Considerations

- GPT-3.5-turbo: ~$0.002 per 1K tokens
- GPT-4: ~$0.03-0.06 per 1K tokens
- Monitor your usage at [OpenAI Platform](https://platform.openai.com/usage)

## Security Notes

- Never commit your `.env` file or expose API keys in code
- Use Streamlit Cloud's secrets management for production deployments
- Regularly rotate your API keys

## License

This project is open source and available under the MIT License.

## Contributing

Contributions are welcome! Feel free to submit issues or pull requests.

## Support

For issues or questions:
- Check the [Streamlit documentation](https://docs.streamlit.io)
- Review [LangChain documentation](https://python.langchain.com)
- Visit [OpenAI documentation](https://platform.openai.com/docs)

---

Made with ❤️ using Streamlit and LangChain
