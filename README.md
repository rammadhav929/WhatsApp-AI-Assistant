# WhatsApp AI Assistant
Developed a cloud-hosted backend system to automate WhatsApp message handling and generate intelligent real-time AI responses.
- Implemented secure webhook-based event processing to receive and respond to live WhatsApp messages.
- Integrated Google Gemini LLM to generate dynamic, context-aware conversational replies.
- Added Meta webhook signature verification and request validation to ensure authenticated event delivery.
- Deployed Django backend on Render with a public HTTPS endpoint registered with Meta WhatsApp Cloud API.
- Managed token-based authentication, API limits, and free-tier operational constraints in a live production environment.
- Tech Stack: Django, Meta WhatsApp Cloud API, Google Gemini API, REST APIs, Secure Webhooks, Render, Git

# Why Is Proxy Needed? 
Because your Django app is not designed to face the internet directly.

**→** Django’s development server (runserver) and even gunicorn:
- Do not handle TLS (HTTPS) efficiently
- Do not manage load balancing
- Do not handle DDoS protection
- Do not optimize connection reuse
- Do not handle edge caching
- Do not isolate network exposure
  
So the proxy handles all of that.

# What Is Webhooks?
A webhook is a mechanism that allows one system to automatically send real-time data to another system when a specific event occurs.

**The Process**
- You Register a Webhook URL , the endpoint is our's public exposed point
- An Event Happens Examples: Payment succeeds
- The Service Sends an HTTP POST
- Your Server Processes It




