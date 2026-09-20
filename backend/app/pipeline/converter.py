from markitdown import MarkItDown
from pathlib import Path
import logging

logger = logging.getLogger(__name__)

class FileConverter:
    def __init__(self) -> None:
               """
               Initializes the converter with a MarkItDown instance.
               """
               self.converter = MarkItDown()

    def convert_to_markdown(self, files_to_convert: list[dict[str, str]]) -> list[dict[str, str]]:
        results: list[dict[str, str]] = []
        for doc in files_to_convert:
            file_path = doc["path"]
            file_name = doc["name"]

            if not file_path:
                logger.error("Missing file path in input dict.")
                continue

            if not Path(file_path).exists():
                logger.error(f"File not found {file_name}")
                continue

            try:
                text = self.converter.convert(doc["path"]).text_content
                new_doc = doc.copy()
                new_doc["text"] = text
                results.append(new_doc)
            except Exception as e:
                logger.error(f"Failed to convert {file_path}: {str(e)}")

        return results
