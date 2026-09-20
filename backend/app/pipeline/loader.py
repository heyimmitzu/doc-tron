from pathlib import Path
import logging

logger = logging.getLogger(__name__)

class FileLoader:
    """
    Responsible for scanning a local directory and identifying valid
    document files for ingestion into the knowledge base.
    """

    def __init__(self) -> None:
        """
        Initializes the FileLoader with a set of allowed file extensions.
        """
        # Changed to a set for O(1) lookup performance
        self.allowed_extensions: set[str] = {".pdf"}

    def load_files(self, file_dir: str) -> list[dict[str, str]]:
        """
        Scans a given directory and returns a list of metadata dictionaries
        for all files matching the allowed extensions.

        Args:
            file_dir (str): The filesystem path to the directory to scan.

        Returns:
            List[Dict[str, str]]: A list of dictionaries, where each dict
                contains 'name', 'path', and 'type' of a valid file.
        """
        directory: Path = Path(file_dir)

        # Safety checks to ensure the path is valid before proceeding
        if not directory.exists():
            logger.error(f"Path does not exist: {file_dir}")
            return []

        if not directory.is_dir():
            logger.error(f"Path is not a directory: {file_dir}")
            return []

        loaded_files: list[dict[str, str]] = []
        for file in directory.iterdir():
            # Check if file matches our allowed extensions (case-insensitive)
            if file.suffix.lower() in self.allowed_extensions:
                loaded_files.append({
                    "name": file.stem,
                    "path": str(file.absolute()), # Ensure we store the string path
                    "type": file.suffix.lower().replace(".", "")
                })

        return loaded_files
