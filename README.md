# Visual Health Advisor

## Overview
Visual Health Advisor is an AI-powered platform designed to assist in medical image analysis. This tool utilizes Google Gemini AI to analyze medical images and provide insights into potential health concerns. It generates structured reports with detailed observations, recommendations, and risk assessments.

## Features

Upload and analyze medical images (PNG, JPG, JPEG)

AI-driven insights based on a structured prompt

Detailed analysis reports with actionable recommendations

Supports healthcare professionals in identifying medical conditions

Ensures compliance with safety settings to prevent misinformation

## Tech Stack

Python: Core programming language

Streamlit: Web interface for interactive user experience

Google Gemini AI: AI model for image analysis

Google API: Secure authentication and API integration

## Installation and Setup

### Prerequisites

Python 3.8+

Google Generative AI API Key

Required Python libraries: streamlit, google-generativeai, pathlib

### Installation Steps

1. Clone the repository:

```
git clone https://github.com/yourusername/visual-health-advisor.git
cd visual-health-advisor
```

2. Create a virtual environment:

```
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:

```
pip install -r requirements.txt
```

4. Set up your API key in google_api_key.py:

```
google_api_key = "your_google_api_key_here"
```

5. Run the application:
```
streamlit run app.py
```

## Usage

- Upload a medical image (PNG, JPG, JPEG).

- Click Execute Analysis.

- Receive a structured AI-generated analysis including:

- Detailed Image Analysis

- Comprehensive Report

- Actionable Recommendations

- Risk Assessment

- Use the results to support clinical decision-making.

## Model Configuration

- Temperature: 1 (Higher creativity)

- Top-p: 0.95

- Max Output Tokens: 8192

- Safety Settings: Blocks harassment, hate speech, explicit, and dangerous content

## Prompt Structure
- The AI model follows a structured prompt ensuring accuracy and relevance:

- Detailed Image Analysis: Detects anomalies and conditions.

- Comprehensive Report: Summarizes findings.

- Actionable Recommendations: Suggests next steps.

- Treatment Suggestions: Offers potential medical interventions.

- Risk Assessment: Categorizes severity as mild, moderate, or severe.


