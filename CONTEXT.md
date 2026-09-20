# Project Context: Doc-Tron (Study Assistant)

## Project Summary
Doc-Tron is a local-first AI-powered study assistant designed to help university students interact with their own documentation, notes, and textbooks. It uses Retrieval-Augmented Generation (RAG) to provide accurate, context-aware answers based on the user's specific uploaded materials.

## Core Goals
- **Local-First:** Prioritize privacy and speed by running the LLM, embedding models, and vector database locally.
- **Knowledge Mining (MVP):** The primary goal of Version 1.0 is to allow users to upload documents and ask the assistant to "mine" and explain specific concepts from those documents.
- **Provider Agnostic:** The backend is designed to interact with any OpenAI-compatible API, allowing easy switching between local models (llama.cpp, Ollama) and cloud models (GPT-4, Claude).

## Technical Architecture

### Backend (Python / FastAPI)
- **Architecture:** Layered architecture separating API routes, core logic, services, and the data pipeline.
- **Framework:** FastAPI for high-performance, async-capable API endpoints.
- **Data Management:** 
    - **LlamaIndex:** Used as the primary framework for data indexing, retrieval, and RAG orchestration.
    - **LanceDB:** Used as the local vector database for high-performance, disk-based storage.
    - **Reranking:** Implemented a reranking step (Cross-Encoder) to filter the top results for higher accuracy.
- **Data Pipeline:**
    - **Conversion:** Uses `markitdown` to convert various formats (PDF, Word) into clean Markdown.
    - **Chunking:** Recursive character splitting with a focus on maintaining structural context (headers).
- **Configuration:** Managed via `pydantic-settings` and environment variables (`.env`) for seamless switching between development and production.

### Frontend (Vue.js)
- **UI:** A clean interface for document management (uploading, tagging) and a chat interface for the study assistant.

## Key Decisions
- **Monorepo Structure:** Backend and frontend live in the same repository but are logically separated into `backend/` and `frontend/` folders.
- **Markdown Focus:** Internal processing focuses on Markdown as the primary intermediate representation of data.
- **Metadata Filtering:** The system uses tags to filter the search space, ensuring the LLM only sees relevant context.
- **Python Management:** Using `uv` for lightning-fast dependency management and environment handling.

## Roadmap
- [ ] **Phase 1:** Backend Infrastructure (FastAPI, LlamaIndex, LanceDB, Configuration).
- [ ] **Phase 2:** Data Ingestion Pipeline (File Loading, Markitdown conversion, Chunking, Embedding).
- [ ] **Phase 3:** Retrieval & RAG Service (Querying, Reranking, LLM synthesis).
- [ ] **Phase 4:** Frontend Development (Vue.js integration, UI/UX).
- [ ] **Phase 5:** Optimization (Performance tuning, advanced prompt engineering).
