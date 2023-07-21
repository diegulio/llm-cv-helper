import typer
import yaml
from dotenv import find_dotenv, load_dotenv

from src.app import app

# Load config file
with open("config.yaml", "r") as file:
    cfg = yaml.safe_load(file)

# Load environment variables
_ = load_dotenv(find_dotenv())  # read local .env file
print(cfg)


def main(
    project_id: str = cfg["project_id"],
    model_name: str = cfg["model_name"],
    chunk_size: int = cfg["chunk_size"],
    chunk_overlap: int = cfg["chunk_overlap"],
    persist_directory: str = cfg["persist_directory"],
):
    app(
        project_id=project_id,
        model_name=model_name,
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        persist_directory=persist_directory,
    )


if __name__ == "__main__":
    typer.run(main)
