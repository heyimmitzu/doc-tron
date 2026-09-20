from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # LLM Settings
    LLM_BASE_URL: str = "http://localhost:8080/v1"
    LLM_API_KEY: str = "mock-key"
    LLM_MODEL_NAME: str = "llama-3"

    # Embedding & Reranker
    EMBEDDING_MODEL: str = "huggingface/all-MiniLM-L6-v2"
    RERANKER_MODEL: str = "BAAI/bge-reranker-base"

    # Database Settings
    LANCEDB_URI: str = "./data/lancedb"

    # Study Assistant Specifics
    MAX_CHUNK_SIZE: int = 1000
    TOP_K_RESULTS: int = 5

    class Config:
        # This tells Pydantic to look for a .env file
        env_file = ".env"

# Create a single instance to be used across the app
settings = Settings()
