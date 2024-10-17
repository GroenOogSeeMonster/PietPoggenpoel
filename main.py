import os
from crewai import Crew, Agent, Task
from tools import crypto_data_tool, news_analysis_tool, technical_analysis_tool

# Check for OpenAI API key
if not os.getenv("OPENAI_API_KEY"):
    raise EnvironmentError(
        "OpenAI API key not found. Please set the OPENAI_API_KEY environment variable."
        "\nYou can get an API key from https://platform.openai.com/account/api-keys"
        "\nThen, set it in your environment with:"
        "\n\nexport OPENAI_API_KEY='your-api-key-here'"
        "\n\nor in your Python script with:"
        "\n\nos.environ['OPENAI_API_KEY'] = 'your-api-key-here'"
    )

# Define the agents
data_analyst = Agent(
    role='Crypto Data Analyst',
    goal='Gather and preprocess cryptocurrency market data',
    backstory='You are an expert in collecting and analyzing cryptocurrency market data.',
    verbose=True,
    allow_delegation=False,
    tools=[crypto_data_tool]
)

news_analyst = Agent(
    role='Crypto News Analyst',
    goal='Analyze recent news and sentiment related to cryptocurrencies',
    backstory='You are an expert in analyzing crypto news and determining market sentiment.',
    verbose=True,
    allow_delegation=False,
    tools=[news_analysis_tool]
)

technical_analyst = Agent(
    role='Technical Analyst',
    goal='Perform technical analysis on cryptocurrency price charts',
    backstory='You are an expert in technical analysis for cryptocurrency markets.',
    verbose=True,
    allow_delegation=False,
    tools=[technical_analysis_tool]
)

advisor = Agent(
    role='Crypto Investment Advisor',
    goal='Provide expert recommendations based on all available data',
    backstory='You are a seasoned crypto investment advisor with years of experience.',
    verbose=True,
    allow_delegation=True
)

# Define the tasks
task1 = Task(
    description='Gather and preprocess market data for top 10 cryptocurrencies',
    agent=data_analyst,
    expected_output="A comprehensive dataset of market data for the top 10 cryptocurrencies."
)

task2 = Task(
    description='Analyze recent news and determine market sentiment',
    agent=news_analyst,
    expected_output="A report on the current market sentiment based on recent crypto news."
)

task3 = Task(
    description='Perform technical analysis on price charts of top 10 cryptocurrencies',
    agent=technical_analyst,
    expected_output="Technical analysis results for the top 10 cryptocurrencies, including key indicators and patterns."
)

task4 = Task(
    description='Compile all data and analyses to provide investment recommendations',
    agent=advisor,
    expected_output="A comprehensive investment recommendation report based on market data, news sentiment, and technical analysis."
)

# Create the crew
crypto_crew = Crew(
    agents=[data_analyst, news_analyst, technical_analyst, advisor],
    tasks=[task1, task2, task3, task4],
    verbose=True  # Changed from 2 to True
)

# Execute the crew's plan
result = crypto_crew.kickoff()

print("Final Result:", result)
