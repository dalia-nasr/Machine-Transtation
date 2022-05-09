# Machine-Transtation
English-French Machine Translation Using a Seq2Seq Architecture


The purpose of this repository is to get more familiar with the Seq2Seq models and their problems.
We will be working on a machine translation problem in which we will have a text as input (in English), and the output will be the translated sentence (in French), similar to how Google Translate works. 
We won't have a model that performs as well as Google Translate, but we'll have a better understanding of how it works and the obstacles that come with a translation problem.

After successfully building the model we need to deploy it so an end-user can communicate with it.
First, we have to extract the essential elements (prediction function, tokenizers, model) that we will use while deploying.
Then, create the Flask app that establishes communication with our model. 
Containerize the app using Docker. Add a docker file that defines the different steps we need to do to create the docker image, also we add a requirements.txt where we list in it the used dependencies

Deploy the Containerized app on Heroku using an AWS EC2 instance.

<img src="https://user-images.githubusercontent.com/91887942/167412710-abe9bdc7-8f75-4b21-b937-f84bb4865f98.png" width="400" height="200">

This small project was done during the MLC training program with Zaka AI

https://education.zaka.ai/machine-learning-certification
