# AI_Powered_Summarization
Rad AI ML infrastructure engineer challenge

## Instructions
Create a FastAPI service that loads a pre-trained Hugging Face NLP model to do text summarization on user-provided text inputs. The service should expose an API to receive a text input and return a summary in a JSON Response.

### Requirements
-Set up a Python environment with the dependencies (FastAPI, Hugging Face Transformers, anything else you see fit).

-Choose a pre-trained NLP model from the Hugging Face Model Hub that is suitable for text summarization.

-An endpoint that takes a JSON input, for the user provided text and returns a response with the result. An example request-response can be like:

``{
"text": "This is a long text input that needs to be summarized. The FastAPI service should be able to handle lengthy inputs and generate a coherent summary based on the user-defined summary length...",
"summary_length": 50
}
``

``
{
"summary": "A brief summary of the lengthy input text, generated by the pre-trained Hugging Face model."
}
``

-Containerize the FastAPI service using Docker, and provide a Dockerfile and instructions on how to build and run the Docker container.

-Include a README that explains how to run a service.
******
## Process
-Python environment and dependencies 

I'm using JetBrains PyCharm IDE running Python 3.12 on a 2023 Mac Studio M2 Max 32gb ram. 

## Documentation
Hugging Face BART model for summarization:
https://huggingface.co/facebook/bart-large-cnn

Installing and using FastAPI: https://fastapi.tiangolo.com/tutorial/

Installing and using Docker to containerize apps: https://docs.docker.com/get-started/

