# 🤖 CV Reviewer

![cv-assistant.png](LLM%20-%20CV%20Reviewer%20aa40fd79ca9f46378ba47a9213315c00/cv-assistant.png)

# Description

In this project I build an streamlit app which allow you to chat with your resume. You can ask it several questions related a pdf document (your resume). You are able to see how I build it in my blog

# Demo

![cv-assitant-demo.gif](LLM%20-%20CV%20Reviewer%20aa40fd79ca9f46378ba47a9213315c00/cv-assitant-demo.gif)

# Installation and Use

## Pre-requisites

In this app we use Google LLM (PaLM). For this you have two options:

- Have credentials configured for your environment (gcloud, workload identity, etc...)
- Store the path to a service account JSON file as the GOOGLE_APPLICATION_CREDENTIALS environment variable

This codebase uses the `google.auth` library which first looks for the application credentials variable mentioned above, and then looks for system-level auth.

For more information, see:

- [https://cloud.google.com/docs/authentication/application-default-credentials#GAC](https://cloud.google.com/docs/authentication/application-default-credentials#GAC)
- [https://googleapis.dev/python/google-auth/latest/reference/google.auth.html#module-google.auth](https://googleapis.dev/python/google-auth/latest/reference/google.auth.html#module-google.auth)

I strongly recommend to use the second option, please you should set the GOOGLE_APPLICATION_CREDENTIALS in a `.env` file (look `.env.example` as reference). PLEASE DONT USE .env.example TO STORE YOUR CREDENTIALS, CREATE YOUR OWN .env FILE AND DON'T SHOW IT TO ANYONE

## Installation

You just have to do the following to instantiate the poetry environment and install de dependencies

```bash
make install_packages
```

and then to run the application:

```bash
make run
```

You can also do it by yourself using poetry and streamlit to run it. We also can find the traditional requirements.txt in this repo.

## Contact

If you have any questions or suggestions related to this project, please contact us through the following channels:

- Linkedin: [https://www.linkedin.com/in/dieguliomachado/](https://www.linkedin.com/in/dieguliomachado/)

We hope you enjoy using this application!

If you want to see more projects you can visit mi blog: 

[Diegulio’s Blog](https://diegulio.github.io/)