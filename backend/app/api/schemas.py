from pydantic import BaseModel
from enum import Enum

class DocStatus(str, Enum):
    PENDING = "pending"
    PROCESSING = "processing"
    COMPLETED = "completed"
    FAILED = "failed"

class Document(BaseModel):
    doc_id: str
    source_path: str
    name: str
    tags: list[str] = []
    status: DocStatus = DocStatus.PENDING

class Chunk(BaseModel):
    chunk_id: str
    doc_id: str
    content: str
    chunk_index: int
