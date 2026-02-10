# WhatsApp AI Assistant
Developed a cloud-hosted backend system to automate WhatsApp message handling and generate intelligent replies in real time using AI.

- Implemented webhook-based event processing to receive and respond to live WhatsApp messages.
-	Integrated Google Gemini LLM to generate dynamic, context-aware responses.
-	Deployed the Django backend on Render with a public HTTPS endpoint registered in Meta
-	Managed token-based authentication, API limits, and free-tier constraints in a live environment
-	Tech Stack: Django, Meta WhatsApp Cloud API, Gemini API, REST APIs, Webhooks, Render, Git

# Why Is a Proxy Needed? 
Because your Django app is not designed to face the internet directly.
-- Django’s development server (runserver) and even gunicorn:
- Do not handle TLS (HTTPS) efficiently
- Do not manage load balancing
- Do not handle DDoS protection
- Do not optimize connection reuse
- Do not handle edge caching
- Do not isolate network exposure
- 
So the proxy handles all of that.

#What Are Webhooks?
A webhook is a mechanism that allows one system to automatically send real-time data to another system when a specific event occurs.
