from textwrap import dedent
from rich.pretty import pprint
import os
from agno.agent import Agent
from datetime import datetime
from agno.playground import Playground, serve_playground_app
from agno.team.team import Team
#Models
from agno.models.groq import Groq
from agno.models.openai import OpenAIChat
#tools
from agno.tools.newspaper4k import Newspaper4kTools
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.yfinance import YFinanceTools
#memory
from agno.memory.v2.db.postgres import PostgresMemoryDb
from agno.memory.v2.memory import Memory
from agno.storage.postgres import PostgresStorage
from agno.memory.v2.db.sqlite import SqliteMemoryDb
from agno.storage.sqlite import SqliteStorage

# PostgreSQL database configuration
db_url = "tmp/agent_storage.db"

os.environ["AGNO_API_KEY"] = os.getenv("AGNO_API_KEY", "---your-agno-api-key---")
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY", "---your-groq-api-key---")
date = datetime.now()

#CREATING MEMORY WITH POSTGRES
memory_db = SqliteMemoryDb(
    table_name="memories",
    db_file="tmp/memory.db"
)
memory = Memory(db=memory_db)

# Create agent storage
agent_storage = SqliteStorage(
    table_name="agent_sessions",
    db_file="tmp/agent_storage.db"
)

#FINANCE RESEARCH AGENT
financeResearchAgent = Agent(
    name="Finance Research Agent",
    agent_id="finance_research_agent",
    model=Groq(
        id="llama3-70b-8192",
        api_key=os.environ["GROQ_API_KEY"]
    ),
    tools=[
        YFinanceTools(
            stock_price=True,                        # ✅ Always relevant
            analyst_recommendations=True,            # ✅ High value for investors
            stock_fundamentals=True,                 # ✅ Must-have for company analysis
            income_statements=True,                  # ✅ Critical for financial health
            key_financial_ratios=True,               # ✅ Useful for valuation (e.g., P/E, ROE)
            technical_indicators=True,               # ✅ Good for traders (RSI, MACD)
            historical_prices=True,                  # ✅ Needed for trend and volatility analysis
            company_info=True,                       # ✅ For basic overview, sector, etc.
            company_news=True,                       # ✅ Market sentiment
            enable_all=False                         # ❌ Avoid unnecessary overhead
        )
    ],
    memory=memory,
    storage=agent_storage,
    enable_user_memories=True,
    show_tool_calls=True,
    markdown=True,
    instructions=dedent(f"""
        You are a seasoned credit rating analyst with deep expertise in market analysis! 📊
        for getting the current recent developments and improvements for your help here is the todays date {date}
        Follow these steps for comprehensive financial analysis:
        1. Market Overview
           - Latest stock price
           - 52-week high and low
        2. Financial Deep Dive
           - Key metrics (P/E, Market Cap, EPS)
        3. Market Context
           - Industry trends and positioning
           - Competitive analysis
           - Market sentiment indicators

        Your reporting style:
        - Begin with an executive summary
        - Use proper markdown tables for data presentation (with | and - separators)
        - Include clear section headers
        - Highlight key insights with bullet points
        - Compare metrics to industry averages
        - Include technical term explanations
        - End with a forward-looking analysisv and Write this exactly "RESEARCH DONE BY FINANCE AGENT"

        Risk Disclosure:
        - Always highlight potential risk factors
        - Note market uncertainties
        - Mention relevant regulatory concerns
        
    """),
)

#Web Scrapping Agent 
webScrapperAgent = Agent(
    name="Web Scrapper Agent",
    agent_id="web_scrapper_agent",
    model=Groq(
        id="llama3-70b-8192",
        api_key=os.environ["GROQ_API_KEY"]
    ),
    tools=[
        DuckDuckGoTools(), 
        Newspaper4kTools(),
    ],
    memory=memory,
    storage=agent_storage,
    enable_user_memories=True,
    show_tool_calls=True,
    markdown=True,
    instructions=dedent("""
        You are a specialized agent designed for web scraping tasks.
        1. Use DuckDuckGo to search for relevant articles or URLs based on the user's query.
        2. Use Newspaper4k to extract clean summaries, titles, and full article content.
        3. Focus only on relevant and recent information.
        Do not generate content on your own — only extract and present existing information from reliable sources.
        4. Write this exactly "RESEARCH DONE BY WEBSCRAPPER AGENT"
    """),
    role="web_scraper"
)

#REPORT GENERATOR
os.environ["OPENAI_API_KEY"] = os.getenv("GITHUB_TOKEN", "---your-github-token----")
os.environ["OPENAI_API_BASE"] = "https://models.github.ai/inference"

reportGenerator = Agent(
    name="Report Generator",
    agent_id="report_generator",
    model=OpenAIChat(
        id="gpt-4.1",
        api_key=os.environ["OPENAI_API_KEY"],
        base_url=os.environ["OPENAI_API_BASE"]
    ),
    memory=memory,
    storage=agent_storage,
    enable_user_memories=True,
    show_tool_calls=True,
    markdown=True,
    instructions=dedent(f"""
        You are a financial report writing expert. Use formal language, clear markdown formatting,
        and include all insights in a structured manner. Date: {date}
        Your goals:
        - Structure given financial insights clearly
        - Use markdown tables
        - Present risks and future outlook
    """),
    expected_output=dedent("""\
        # {Compelling Headline}

        ## Executive Summary
        {Concise overview of key findings and significance}

        ## Key Findings
        {Main discoveries and analysis}
        {Expert insights and quotes}
        {Statistical evidence}

        ## Data Tables
        When presenting data, use proper markdown table format:
        ```
        | Column 1 | Column 2 | Column 3 |
        |----------|----------|----------|
        | Data 1   | Data 2   | Data 3   |
        | Data 4   | Data 5   | Data 6   |
        ```

        ## Impact Analysis
        {Current implications}
        {Stakeholder perspectives}
        {Industry/societal effects}

        ## Future Outlook
        {Emerging trends}
        {Expert predictions}
        {Potential challenges and opportunities}

        ## Expert Insights
        {Notable quotes and analysis from industry leaders}
        {Contrasting viewpoints}

        ## Sources & Methodology
        {List of primary sources with key contributions}
        {Research methodology overview}

        ---
        {RESEARCH DONE BY FINANCE TEAM}\
    """),
)

sentimentAnalysisAgent = Agent(
    name="Sentiment Analysis Agent",
    agent_id="sentiment_analysis_agent",
    model=OpenAIChat(
        id="gpt-4.1",
        api_key=os.environ["OPENAI_API_KEY"],
        base_url=os.environ["OPENAI_API_BASE"]
    ),
    memory=memory,
    storage=agent_storage,
    enable_user_memories=True,
    show_tool_calls=True,
    markdown=True,
    instructions=dedent(f"""
       You are a sentiment analysis expert specialized in financial content. Your task is to analyze the sentiment of various financial texts, including news articles, earnings reports, social media posts, or user-provided text. 
       Your goals are as follows:
       1. Analyze the sentiment and classify it as Positive, Negative, or Neutral.
       2. Provide a confidence score or reasoning for your classification.
       3. Identify emotional tone, market optimism or pessimism, and investor reactions.
       4. Summarize the implications of sentiment on stock performance or market trends.Guidelines for your analysis:
           - Begin your response by indicating the sentiment label at the top (e.g., Sentiment: Positive).
           - Use bullet points or short summaries for clarity in your analysis.
           - Highlight key phrases or signals from the text that influenced your judgment.- 
       Maintain an objective tone avoid exaggeration or personal opinion.
           - If the sentiment is mixed or unclear, mention the uncertainty in your assessment.
           - If the text is unrelated to finance, respond with: "The provided content does not appear to be financial in nature.
       "For example, you might receive a prompt like: "Analyze the sentiment of this article about Tesla’s recent earnings call." 
        Please provide a thorough analysis based on the guidelines above.
    """),
)

# FINANACE TEAM
financeChatbot = Team(
    name="Finance Team",
    mode="coordinate",
    model=OpenAIChat(
        id="gpt-4.1",
        api_key=os.environ["OPENAI_API_KEY"],
        base_url=os.environ["OPENAI_API_BASE"]
    ),
    members=[financeResearchAgent, reportGenerator,webScrapperAgent,sentimentAnalysisAgent],
    show_tool_calls=True,
    description="You are the Finance Team — a specialized group of agents with deep expertise in handling a wide range of financial tasks, including reporting, analysis, planning, and data-driven decision making. Your role is to route user queries to the most suitable financial tool or language model based on the context and complexity of the request.",
    instructions=[
        """
        You are a collaborative financial team made up of specialized agents. Work together to fulfill user queries with a coordinated approach.

        Team Workflow:
        - When a user asks to generate a new financial report:
            1. The Finance Research Agent must gather all relevant financial data, market insights, and store it in memory.
            2. The Web Scrapper Agent Gathers Data and Current Financial news from the DuckDuckGoSearch, Newspaper4k to extract clean summaries, titles, and full article content and saves it in memory.
            2. Once data is ready, the Report Generator reads the memory and generates a structured markdown report with insights.

        - When a user asks questions about a generated report:
            - The Business Chatbot (convoChatbot) should answer using context from the memory and maintain a professional tone.

        Agent Specializations:
        - 🔍 Finance Research Agent: Gathers data like stock prices, market trends, key ratios, etc.
        -  WebScrapper Agent : Gather Current news and Data from the DuckDuckGoSearch and Current recent News. 
        - 📄 Report Generator: Converts research into a detailed financial report with markdown formatting, tables, and summaries.
        - Sentiment Analysis Agent: Analyzes the emotional tone and market sentiment of financial news, earnings reports, or social content. Provides Positive, Negative, or Neutral classification with reasoning to guide investor perception.
        
        Notes:
        - You have to Write the Agent Name before the member agent response respectively: Finance Team, Webscrapper Agent, Report Making Agent , Convo Chatbot.
        - Maintain clear communication between agents using memory as shared context.
        - Ensure that the Research Agent runs before the Report Generator if fresh data is needed.
        - Always produce professional, well-structured, and insight-driven outputs.
        - Avoid duplicate responses—each agent should wait for its input from previous agents before acting.
        """
    ],
     storage=SqliteStorage(
        table_name="financeTeamStorage",
        db_file="tmp/agent_storage.db",
        mode="team",
        auto_upgrade_schema=True
    ),
    memory=memory,
    session_id="my_chat_session",
    add_history_to_messages=True,
    add_datetime_to_instructions=True,
    enable_user_memories=True,
)

# Correctly initialize the Team
financeChatbot.initialize_team()

# Create and configure the playground app correctly
playground = Playground(
    teams=[financeChatbot],
    app_id="finance-team-playground-app",
    name="Finance Team Playground"
)

# Get the app for ASGI server
app = playground.get_app()

if __name__ == "__main__":
    playground.serve(app="agent:app", reload=True)