# 🏦 Finance Team AI Agent

A sophisticated multi-agent financial analysis system powered by AI that provides comprehensive market research, sentiment analysis, and automated report generation.

## 🌟 Features

- **🔍 Finance Research Agent**: Gathers real-time stock data, market trends, and financial metrics using Yahoo Finance
- **🌐 Web Scrapper Agent**: Collects current financial news and market insights from multiple sources
- **📊 Sentiment Analysis Agent**: Analyzes market sentiment from news articles and financial content
- **📄 Report Generator**: Creates structured, professional financial reports with markdown formatting
- **🤝 Team Coordination**: Intelligent agent coordination for comprehensive financial analysis
- **💾 Memory System**: Persistent storage for analysis history and context
- **🎮 Interactive Playground**: Web-based interface for easy interaction with the AI team

## 🏗️ Architecture

The system consists of specialized AI agents working together:

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│ Finance Research│    │  Web Scrapper    │    │ Sentiment       │
│ Agent           │    │  Agent           │    │ Analysis Agent  │
│ (Yahoo Finance) │    │ (News & Search)  │    │ (Market Mood)   │
└─────────────────┘    └──────────────────┘    └─────────────────┘
         │                       │                       │
         └───────────────────────┼───────────────────────┘
                                 │
                    ┌─────────────────────┐
                    │  Report Generator   │
                    │  (Structured Output)│
                    └─────────────────────┘
```

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- Node.js 18+ (for UI)
- API Keys:
  - Groq API Key
  - OpenAI API Key (or GitHub Models API)
  - Agno API Key

### 1. Clone the Repository

```bash
git clone <your-repo-url>
cd Agno
```

### 2. Backend Setup (Python Agent)

#### Install Dependencies
```bash
pip install -r requirements.txt
```

#### Set Environment Variables
Create a `.env` file or set environment variables:
```bash
export GROQ_API_KEY="your_groq_api_key"
export OPENAI_API_KEY="your_openai_api_key"  # or GitHub token
export AGNO_API_KEY="your_agno_api_key"
```

#### Run the Agent
```bash
python agent.py
```

The agent playground will be available at: `http://localhost:8000`

### 3. Frontend Setup (Next.js UI)

#### Navigate to UI Directory
```bash
cd agent-ui
```

#### Install Dependencies
```bash
# Using npm
npm install

# Using pnpm (recommended)
pnpm install

# Using yarn
yarn install
```

#### Run Development Server
```bash
# Using npm
npm run dev

# Using pnpm
pnpm dev

# Using yarn
yarn dev
```

The UI will be available at: `http://localhost:3000`

## 📋 Available Commands

### Backend (Python)
```bash
# Run the main agent
python agent.py

# Install dependencies
pip install -r requirements.txt
```

### Frontend (Next.js)
```bash
# Development server
pnpm dev

# Build for production
pnpm build

# Start production server
pnpm start

# Linting and formatting
pnpm lint
pnpm format
pnpm typecheck
```

## 🔧 Configuration

### API Keys Setup

1. **Groq API**: Get your API key from [Groq Console](https://console.groq.com/)
2. **OpenAI/GitHub Models**: 
   - OpenAI: Get from [OpenAI Platform](https://platform.openai.com/)
   - GitHub Models: Use your GitHub token with models access
3. **Agno API**: Get from [Agno Platform](https://agno.ai/)

### Environment Variables

```bash
# Required API Keys
GROQ_API_KEY=your_groq_api_key_here
OPENAI_API_KEY=your_openai_or_github_token_here
AGNO_API_KEY=your_agno_api_key_here

# Optional: Custom OpenAI Base URL (for GitHub Models)
OPENAI_API_BASE=https://models.github.ai/inference
```

## 💡 Usage Examples

### Basic Financial Analysis
```python
# The system will automatically coordinate agents to:
# 1. Gather financial data (Finance Research Agent)
# 2. Collect recent news (Web Scrapper Agent)
# 3. Analyze sentiment (Sentiment Analysis Agent)
# 4. Generate comprehensive report (Report Generator)

# Example query: "Analyze Tesla's current financial position"
```

### Custom Queries
- "What's the market sentiment around Apple's latest earnings?"
- "Generate a comprehensive report on Microsoft's financial health"
- "Analyze the tech sector trends for Q4 2024"

## 🗂️ Project Structure

```
Agno/
├── agent.py              # Main agent configuration and team setup
├── requirements.txt      # Python dependencies
├── README.md            # This file
├── tmp/                 # Database files (auto-created)
│   ├── memory.db        # Agent memory storage
│   └── agent_storage.db # Session storage
└── agent-ui/            # Next.js frontend
    ├── src/             # Source code
    ├── package.json     # Node.js dependencies
    └── ...              # Other UI files
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Support

If you encounter any issues or have questions:

1. Check the [Issues](../../issues) page
2. Create a new issue with detailed information
3. Join our community discussions

## 🙏 Acknowledgments

- Built with [Agno](https://agno.ai/) - Advanced AI Agent Framework
- Powered by [Groq](https://groq.com/) and [OpenAI](https://openai.com/)
- UI built with [Next.js](https://nextjs.org/) and [Tailwind CSS](https://tailwindcss.com/)

---

**Made with ❤️ by the Finance Team AI**
