# AI Sports Article Generator from Tweets

## Overview
This project fetches trending sports tweets (or uses local tweets) and generates full-length articles automatically using AI models. It can use:

- **OpenAI GPT** (if API is available)  
- **Hugging Face OPT** (CPU-compatible, local fallback)

The generated articles are saved in a folder for easy access.

## Features
- Fetch latest tweets about sports events  
- Generate human-like articles automatically  
- Save articles locally in `articles/` folder  
- Automatic fallback from OpenAI GPT to Hugging Face OPT if API fails  

## Installation

1. Clone this repository:

```bash
git clone https://github.com/yourusername/AI-Sports-Article-Generator.git
cd AI-Sports-Article-Generator
