# Paraphrasing API using `chatgpt_paraphraser_on_T5_base`

This repository contains a Flask API that uses the `chatgpt_paraphraser_on_T5_base` model from Hugging Face to paraphrase input sentences. It also includes a Python script to make requests to this API.

## Setup

1. **Install Required Libraries**:

   Before running the API or the request script, you need to install the required libraries:

    pip install transformers flask requests

## Running the API

1. Navigate to the directory containing the API script.
2. Run the Flask application:

    python api.py

The API will start, and it should be accessible at `http://127.0.0.1:5000/`.

## Using the Request Script

1. Ensure the Flask API is running.
2. Navigate to the directory containing the request script.
3. Run the request script:

    python request.py

The script will make a request to the Flask API, and you should see the original and paraphrased sentences printed to the console.

or using curl:

curl -X POST -H "Content-Type: application/json" -d '{"prompt":"I am an hardware architecht which try to imrpove architects with ai"}' http://127.0.0.1:5000/paraphrase

    {
        "result": [
            "I am a hardware engineer who endeavors to impress architects with AI.",
            "As a hardware organization, I aim to gain the trust of architects through Ai.",
            "My role as a hardware architect involves working with architects to gain access to their software development expertise.",
            "The hardware organization I work for aims to empower architects with AI."
        ]
    }

## API Endpoint

- **Endpoint**: `/paraphrase`
- **Method**: `POST`
- **Data Format**: JSON with a key named "prompt" containing the sentence to be paraphrased.

    {
        "prompt": "I am an hardware architecht which try to imrpove architects with ai"
    }

- **Response**: JSON containing a key named "result" with a list of paraphrased sentences.

Example:

    {
        "result": [
            "I am a hardware engineer who endeavors to impress architects with AI.",
            "As a hardware organization, I aim to gain the trust of architects through Ai.",
            "My role as a hardware architect involves working with architects to gain access to their software development expertise.",
            "The hardware organization I work for aims to empower architects with AI."
        ]
    }


## Request Script Functionality

The request script sends a sentence to the API for paraphrasing and then prints the original and paraphrased sentences. You can modify the `sentence` variable in the script to test with different inputs.

