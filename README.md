# Machine-Transtation
English-French Machine Translation Using a Seq2Seq Architecture


This project is to become more familiarized with the Seq2Seq models and their issues. We will be working on a machine translation problem in which we will have a text as input (in English), and the output will be the translated sentence (in French), similar to how Google Translate works.

We won't have a model that performs as well as Google Translate, but we will better understand how it works and the challenges associated with a translation problem.

After successfully building the model, we need to deploy it so an end-user can communicate with it. First, we need to extract the essential elements (prediction function, tokenizers, model) that we will use while deploying. Then, create the Flask app that establishes communication with our model. Containerize the app using Docker. Add a docker file that defines the different steps we need to do to create the docker image and a requirements.txt where we list in it the used dependencies.
Deploy the Containerized app on Heroku using an AWS EC2 instance.

<img src="https://user-images.githubusercontent.com/91887942/167418420-bc630656-1eae-40ad-a21d-1e133396f13a.png" width="400" height="200">

This small project was done during the MLC training program with Zaka AI

https://education.zaka.ai/machine-learning-certification
