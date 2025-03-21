name: GPT-4 Code Review

on:
  pull_request:
    types: [opened, synchronize]

jobs:
  review:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repository
        uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'

      - name: Install dependencies
        run: |
          pip install openai

      - name: Run code review script
        run: python scripts/review_script.py
        env:
          OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}

# Repository URL
# REPO_URL = "https://github.com/lukeeterna/dropevolutionproject"
