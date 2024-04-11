1. What was your approach?
- To build this system to be deployed on Docker and used locally from a developer's perspective.

2. what was the focus?
- I focused on making it easier for anyone to use this app and build upon it without much
research.

3. Why did you choose the BART model? 
- I chose the BART model because it's large and has a lot of pre-training on different
aspects of NLP. It can also be fine-tuned easily with supervised learning. 
- Alternatives could be Pegasus which has pre-training for text summarization or the GPT models
which can be fine-tuned (but don't have pre-training)
- To fine-tune a model, play with parameters like learning rate or batch size. 
- Pre-process any data as needed
- Continuously evaluate the performance of the fine-tuned model against the original responses
for text summarization

4. How would you scale this tool up for multiple users? 

- Utilize load balancing for handling requests
- Continue to utilize asynchronous functions for handle concurrency
- Continue to use Docker or Kubernetes ro auto-deploy and manage services individually
- Use cloud providers like AWS that can provide auto-scaling for containerized apps
- Implement caching like a CDN for frequent requests (the same string of text requested)

5. What are some security issues?
- Injection attacks due to not sanitizing or validating input text at the end-point
- Error messages should be sanitized to prevent an opening for sensitive data to leak
- Compressed summary isn't sanitized which could expose the app to attacks if the input has malicious characters
- No authentication or authorization. In a more in-depth app, we would validate credentials and access or some kind. 
>Input Sanitization:
> 
> Validate data for expected formats, data types, length
> 
> Limit input length to prevent denial of service attacks
> 
> Output Sanitization:
> 
> Use HTML encoding to prevent cross-site scripting attacks
> 
> Handle escaping special characters to prevent injection attacks
> 
> 
6. How would you change your testing?
- The testing included here is to check the output of the text inputted for summarization 
- More thorough testing for empty string, long repeated consecutive characters (happpppppppppppppppy),
test for general validation of input text

7. POST vs GET
- If you need to mainly retrieve data, GET requests are more appropriate (minimal strain on servers)
- If you need to modify information, POST requests are more appropriate 
- If you want to handle large amounts of data, POST requests are more appropriate

8. Docker vs Kubernetes 
- Both manage containerized applications
- Docker is better for smaller scale, local apps 
- Kubernetes is better for large scale apps that need high availability 
- Kubernetes has built-in load balancing abilities 