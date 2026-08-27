
# Context-Aware-AI-Assistant
# ♡ Our Little Space

> A personalized AI space designed to help people understand each other better.

**Our Little Space** is a context-aware AI application built around a simple idea: conversations become more useful when an AI understands the people and context behind them.

Instead of treating every message as an isolated prompt, the system uses structured information about the people involved — including personality, communication style, preferences, patterns, and relevant past experiences — to generate responses that are more personal and context-aware.

The same approach can be adapted to different kinds of connections between two people, including friends, siblings, partners, family members, or anyone who wants to understand another person better.

---

## ✨ What It Does

The application provides three response modes, each designed for a different situation.

### 🧠 Understand

Helps the user make sense of a situation by considering:

- The personalities of both people
- Communication styles
- Previous patterns and experiences
- Relevant memories
- Different perspectives
- Possible reasons behind someone's behavior

The assistant is instructed to separate known information from possible interpretations rather than treating assumptions as facts.

### 🌷 Cheer Me Up

When the user needs something lighter, the assistant focuses on emotional support.

It can use relevant positive memories, familiar patterns, gentle humor, and comforting context to make the conversation feel more personal.

The goal is to acknowledge the user's feelings first instead of forcing positivity.

### 💬 Help Me Reply

Helps the user decide what to say in a particular situation.

The assistant considers:

- The situation
- The other person's communication style
- The user's natural way of speaking
- The context between the two people
- What is likely to keep the conversation open and comfortable

The goal is to suggest something natural rather than producing generic copy-paste responses.

---

## 🧩 Context-Aware Personalization

The core of the project is its structured context system.

Each person can have their own context containing information such as:

- Personality and temperament
- Hobbies and interests
- Likes and dislikes
- Communication style
- Habits
- Typical reactions
- Things that make them happy
- Things that frustrate them
- Behavior under stress
- Relevant past experiences
- Communication patterns
- Names and pronouns

The system combines relevant context with the current conversation and selected response mode.

This allows the same underlying AI model to respond differently depending on:

**who is using it + what is happening + what kind of help they need.**

---

## 🏗️ Architecture

The project separates the user interface, backend logic, and prompt system.

```text
                     ┌────────────────────┐
                     │      Gradio UI     │
                     │       app.py       │
                     └─────────┬──────────┘
                               │
                    Message + Perspective
                         + Response Mode
                               │
                               ▼
                     ┌────────────────────┐
                     │     backend.py     │
                     │                    │
                     │  Chat Logic        │
                     │  API Integration   │
                     │  Prompt Assembly   │
                     └─────────┬──────────┘
                               │
                 ┌─────────────┴─────────────┐
                 │                           │
                 ▼                           ▼
        ┌─────────────────┐        ┌─────────────────┐
        │ Modular Prompts │        │ Conversation    │
        │                 │        │ History         │
        └────────┬────────┘        └─────────────────┘
                 │
                 ▼
        ┌────────────────────┐
        │    Gemini Model    │
        └────────────────────┘
````

---

## 📁 Project Structure

```text
AI-Personal-Analyzer/
│
├── app.py
├── backend.py
│
├── prompts/
│   ├── __init__.py
│   ├── system.py
│   ├── friendly.py
│   ├── interpretation.py
│   ├── memory.py
│   ├── examples.py
│   ├── cheerful.py
│   ├── pronouns.py
│   ├── modes.py
│   ├── partner_a.py
│   └── partner_b.py
│
├── .env
├── .gitignore
└── README.md
```

### Why Separate the Prompts?

The prompt system is intentionally divided into smaller files instead of keeping one large prompt inside `backend.py`.

This makes it easier to independently improve:

* General system behavior
* Friendly conversational behavior
* Situation interpretation
* Memory handling
* One-shot and multi-shot examples
* Cheer-up behavior
* Pronoun and reference handling
* Response modes
* Individual context

This modular structure makes future prompt tuning easier without having to work inside one large backend file.

---

## 🎨 User Interface

The frontend is built using **Gradio** and is designed to keep the interaction simple and focused on the conversation.

The current interface includes:

* Individual selection
* Response mode selection
* Conversational chat interface
* Streaming AI responses
* Conversation history
* Authentication
* Responsive layout
* Minimal visual design

The UI intentionally avoids unnecessary features so that the conversation remains the primary focus.

---

## 🔄 Response Flow

A typical interaction follows this process:

```text
User selects their perspective
            ↓
User selects a response mode
            ↓
User sends a message
            ↓
Conversation history is collected
            ↓
Relevant personal context is included
            ↓
Mode-specific instructions are applied
            ↓
Prompt is sent to the language model
            ↓
Response is streamed back
            ↓
Conversation continues with updated history
```

---

## 🧠 Design Philosophy

### Context Over Generic Responses

The assistant should understand the situation and the people involved before responding.

### Multiple Perspectives

The system considers the perspectives of both people instead of automatically assuming that one person is right.

### Facts Before Assumptions

Known information and possible interpretations should not be treated as the same thing.

### Relevant Memory

Previous experiences should be used when they genuinely help explain the current situation rather than simply repeating everything the system knows.

### Personalized, Not Overconfident

The AI can use the context provided to it, but should not pretend to know another person's thoughts or feelings with certainty.

### Natural Conversation

The goal is to feel like a thoughtful, context-aware companion rather than a formal analysis tool.

### Mode-Based Responses

The same situation can require different kinds of help. Understanding a situation, feeling better, and deciding what to say are different needs, so the system treats them separately.

### Simple Language

Responses are designed to remain natural and easy to understand rather than unnecessarily using complex or overly formal language.

---

## 🛠️ Technology Stack

### Python

Used as the primary programming language for the application, backend logic, prompt management, and API integration.

### Gradio

Used to build the conversational frontend, user controls, authentication, and streaming chat interface.

### Google Gemini

Used as the language model that generates the personalized responses.

### OpenAI Python SDK

Used as the API interface for communicating with the Gemini-compatible API endpoint.

### python-dotenv

Used to load API credentials and other sensitive configuration through environment variables.

### Git & GitHub

Used for version control and project management.

---

## 🔐 Privacy & Security

Because the application works with highly personalized context, privacy is an important part of the project.

The project uses:

* Authentication for application access
* Environment-based API credentials
* `.env` excluded from version control
* Anonymized personal information in the public-facing project
* Separate prompt files for managing personalized context

Sensitive credentials such as API keys and passwords are not intended to be stored directly in source code.

### `.gitignore`

The project excludes sensitive and generated files such as:

```text
.venv/
.env
__pycache__/
.ipynb_checkpoints/
```

Personal context included in the public-facing version has been anonymized.

---

## 🧪 Current Status

**V1 — Working Personal Prototype**

The current version focuses on building and testing the core experience rather than trying to provide a large number of features.

### Implemented

* [x] Gradio frontend
* [x] Separate frontend and backend
* [x] Gemini integration
* [x] Streaming responses
* [x] Conversation history
* [x] Individual perspective handling
* [x] Three response modes
* [x] Context-aware responses
* [x] Modular prompt architecture
* [x] Authentication
* [x] Environment-based secrets
* [x] Anonymized public-facing context
* [x] Responsive interface

### Current Scope

The current version is intentionally small and focused.

It is primarily a personal AI application and learning project rather than a production-scale platform.

---

## 📌 Why I Built This

I wanted to explore whether an AI system could become more useful when it understands the context between people rather than treating every conversation as an isolated prompt.

Instead of building another generic chatbot, I wanted to experiment with giving the AI structured knowledge about people, their communication patterns, and relevant past experiences.

This project became an opportunity to explore how personalization can change the way an AI responds to the same situation.

It also gave me practical experience with:

* LLM application architecture
* Prompt engineering
* Context management
* Memory and conversation history
* Multiple response modes
* Streaming responses
* Conversational UX
* Frontend and backend separation
* Modular prompt design
* API integration
* Authentication
* Environment variables
* Secret management
* Version control

---

## 🔍 What I Learned

Building this project helped me understand that creating an AI application is not only about connecting an API to a chat interface.

A large part of the work involves designing the context given to the model, deciding how information should be organized, controlling how the model interprets situations, and making sure the generated response fits the user's actual need.

The project especially helped me explore:

### Prompt Architecture

Breaking a large system prompt into smaller, maintainable components.

### Context Management

Providing relevant information about people without treating every piece of stored information as equally important.

### Perspective Handling

Allowing the AI to understand that the person asking a question and the person being discussed may be different.

### Mode-Based Behavior

Changing the response style and purpose based on what the user actually needs.

### Conversational UX

Keeping the interface simple while still supporting personalization and streaming responses.

### Frontend / Backend Separation

Keeping UI logic separate from the AI and API logic so that both can be developed independently.

---

## 🚧 Future Improvements

The current version is intentionally limited. Future versions may explore:

* Long-term conversation memory
* Persistent conversation storage
* Smarter memory retrieval
* Improved context selection
* More advanced authentication
* Additional response modes
* Better personalization
* Improved conversation management
* More refined conversational UX
* Production deployment and security improvements

These are planned as future iterations rather than part of the current V1 scope.

---

## ⚠️ Disclaimer

This is a personal AI learning project and experimental prototype.

The responses generated by the system are AI-generated and should not be treated as professional medical, mental-health, legal, or other professional advice.

---

## 👩‍💻 Project Status

**Project:** Our Little Space
**Version:** V1
**Type:** Personal AI Application / Working Prototype
**Focus:** Context-Aware Conversational AI

Built as part of my exploration into **LLM applications, prompt engineering, personalized AI systems, and conversational interfaces.**

```
```
