🧭 Week 1 — Day 1 Backend Learning Journal
🔹 Focus:

Backend Environment Setup | Node + TypeScript Configuration | API Basics | Documentation Preparation


1️⃣ Backend Project Initialization
✔ Repository & Folder Setup

Created the base structure inside backend-learning/Week2/:

backend/
notes/
project/

This keeps backend code, documentation, and project work clearly separated for professional workflow and GitHub readability.


2️⃣ Node.js + TypeScript Environment Setup

Installed and configured all core dependencies required to build a production–style backend.

📦 Runtime Dependencies
Package	        Purpose
express	        Web server framework
cors	        Handle cross-domain requests
dotenv	        Load environment variables


🧰 Dev Dependencies
Package	                                      Purpose
typescript	                                  TS language support
ts-node-dev	                                  Auto-reload during development
@types/node, @types/express, @types/cors	  Type definitions for TS


Initialized TypeScript config and resolved module-related errors:

* Enabled esModuleInterop

* Enabled moduleResolution: node

* Set compiler strict mode

* Ensured CommonJS module compatibility


3️⃣ DSA - Two Sum(Backend_leanring.ipynb)


4️⃣ Project Documentation — Architecture & API Planning

Created two major planning documents for the full-stack project TaskFlow:

📘 Project Structure Document

Covers:

	* Layered architecture

	* Folder responsibilities

	* Config, routes, services, middleware, repositories

📗 API Endpoint Blueprint

Covers:

	* Auth endpoints

	* User endpoints

	* Task CRUD

	* Dashboard endpoints

	* Comments & utilities

Both documents stored as Markdown in the notes/ folder for future referen