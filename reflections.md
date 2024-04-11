1. What was your approach?
- To build this system to be deployed on Docker and used locally from a developer's perspective.

2. what was the focus?
- I focused on making it easier for anyone to use this app and build upon it without much
research.

3. Why did you choose the BART model? 
- I chose the BART model because it's large and has a lot of pre-training on different
aspects of NLP. It can also be fine-tuned easily with supervised learning. 
-Alternatives could be Pegasus which has pre-training for text summarization or the GPT models
which can be fine-tuned (but don't have pre-training)
- To fine-tune a model, play with parameters like learning rate or batch size. 
- Pre-process any data as needed
- Continuously evaluate the performance of the fine-tuned model against the original responses
for text summarization

4. How would you scale this tool up for multiple users? 
-Utilize load balancing for handling requests 
-Continue to utilize asynchronous functions for handle concurrency 
-Continue to use Docker or Kubernetes ro auto-deploy and manage services individually 
-Use cloud providers like AWS that can provide auto-scaling for containerized apps
-Implement caching like a CDN for frequent requests (the same string of text requested)

5. What are some security issues?
-