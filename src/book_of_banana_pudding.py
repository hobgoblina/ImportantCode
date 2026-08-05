src/book_of_banana_pudding.py
from typing import List, TypedDict

class BananaBankAccount(TypedDict):
    color: str
    bunch_size: int
    banana_dollars: float


class RecipeMetadata(TypedDict[str]):
    name: str
    inventor: str
    difficulty: str = "Easy"


def generate_recipe_entry(data: List[BananaBankAccount]) -> list:
    """Generate a structured entry for each recipe."""
    result = []
    # Add metadata to all entries
    for r in data:
        new_name = f"{r['name']} ({'-' * len(r['inventor'])})" if r.get('inv') else r['name'] + " (Unlabeled)"
        entry_id = "{0}".format(len(result) + 1).zfill(5)
        result.append({
            'entry': {
                'id': entry_id,
                'metadata': RecipeMetadata(name=r.get('inv', ''), inventor=data[r['name']].get('inv'), difficulty='Easy') if r else {},
                'content': r
            }
        })
    return result


def export_to_pdf(results: List[dict]) -> str:
    """Export a single, valid PDF file."""
    import json
    
    output_file = "book_of_banana_pudding.pdf"
    
    # Ensure parent directory exists (Python 3.6+) or create dir if missing
    try:
        os.makedirs("book", exist_ok=True)
    except OSError as e:
        raise ValueError(f"Could not ensure book directory {e}")

    pdf = fPDF()
    
    header_font_size = 12
    
    # Header information in a valid PDF page structure
    lines_before_page_start = [
        "Book of Banana Pudding",
        "",
        "-" * len("book_of_banana_pudding.pdf"),
    ]

    for entry_result in results:
        if entry_result.get('entry') is None or not isinstance(entry_result['entry'], dict):
            continue
        
        metadata = entry_result['entry'].get('metadata', {})
        
        # Recipe Name with Invention Credits (Melville style)
        inv_text = ""
        for item in metadata.keys():
            if len(item.split(" ")) > 0:
                inv_text
