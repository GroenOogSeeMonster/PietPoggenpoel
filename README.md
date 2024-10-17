# Crypto Expert Piet Poggenpoel - AI Analysis and Recommendations Tool

## Overview

This application is a sophisticated Crypto Expert Analysis and Recommendations Tool built using the crewAI library in Python. It leverages artificial intelligence to simulate a team of crypto experts working together to analyze market data, news sentiment, and technical indicators to provide informed investment recommendations.

## Features

- **Data Analysis**: Fetches and preprocesses market data for top cryptocurrencies.
- **News Sentiment Analysis**: Analyzes recent news articles to gauge market sentiment.
- **Technical Analysis**: Performs technical analysis on cryptocurrency price charts.
- **Expert Recommendations**: Compiles all data and analyses to provide investment recommendations.

## System Architecture

The system is composed of four main components, each represented by an AI agent:

1. **Crypto Data Analyst**: Gathers and preprocesses cryptocurrency market data.
2. **Crypto News Analyst**: Analyzes recent news and determines market sentiment.
3. **Technical Analyst**: Performs technical analysis on cryptocurrency price charts.
4. **Crypto Investment Advisor**: Provides expert recommendations based on all available data.

## Setup and Installation

1. Clone this repository:
   ```
   git clone https://github.com/GroenOogSeeMonster/PietPoggenpoel.git
   cd PietPoggenpoel
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Set up your OpenAI API key:
   You need to set your OpenAI API key as an environment variable. You can do this in two ways:

   a. Set it in your shell:
      ```
      export OPENAI_API_KEY='your-api-key-here'
      ```

   b. Set it in your Python script (add this near the top of main.py):
      ```python
      import os
      os.environ['OPENAI_API_KEY'] = 'your-api-key-here'
      ```

   Replace 'your-api-key-here' with your actual OpenAI API key. You can obtain an API key from https://platform.openai.com/account/api-keys

4. Run the main script:
   ```
   python main.py
   ```

## File Structure

- `main.py`: The main script that orchestrates the entire workflow.
- `tools.py`: Contains custom tools used by the AI agents for data fetching, news analysis, and technical analysis.
- `requirements.txt`: Lists all the Python packages required to run this project.

## Requirements

This project requires several Python packages to run. These are listed in the `requirements.txt` file and include:

- crewai
- yfinance
- pandas
- requests
- beautifulsoup4
- ta
- openai

You can install all required packages using pip:
`pip install -r requirements.txt`

## Customization

You can customize the behavior of the agents by modifying their roles, goals, and backstories in `main.py`. Additional tools can be added to `tools.py` to expand the capabilities of the system.

## Limitations and Future Improvements

- The current implementation provides a basic structure and would need to be expanded with more detailed logic for production use.
- Error handling and input validation should be improved for robustness.
- The news analysis and investment recommendation logic could be enhanced with more sophisticated AI models.
- Integration with real-time data feeds and APIs could improve the accuracy and timeliness of the analysis.

## Disclaimer

This tool is for educational and research purposes only. Always consult with a qualified financial advisor before making investment decisions.

## Contributing

Contributions to improve and expand this tool are welcome. Please feel free to submit pull requests or open issues for bugs and feature requests.

## License

This project is licensed under the MIT License - see the LICENSE file for details.