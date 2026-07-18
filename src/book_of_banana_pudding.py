import json
from typing import TypedDict
from recipe_library import RecipeLibrary, BananaPudding

class BananaBankAccount(TypedDict):
    color: str
    bunch_size: int
    banana_dollars: float


# Define the Melville-style PDF content structure for consistency with previous code blocks
pdf_content = """[0] [Color Unknown]\n\nInvented by: Unknown"""

def load_recipes():
    return json.loads("banabank.json")

def export_to_pdf(output_path="book_of_banana_pudding.pdf"):
    pdf_output = FPDF().output(output_path)
    
    if not loads.recipes_data:
        return
    
    for idx, recipe in enumerate(loads.recipes_data):
        text_content = f"[{idx+1}] {recipe['name']}\n\nInvented by: {recipe.get('inventor', 'Unknown')}"
        
        pdf_output.cell(50, 8) 
        if recipe['color']:
            pdf_output.text(recipe['color'], color=127, align='C')
        else:
            pdf_output.text("Color Unknown", color="black")

def save_json_data():
    data = {
        "library": loads.library,
        "version": 1,
        "last_modified": __import__("os").getmtime() // (10**8) if hasattr(__import__("os"), 'getmtime') else int(0),
        "notes": "",
        "_metadata_created_by_user: true"
    }

    with open(output_path.replace('.pdf', '.json'), 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)


def export_to_pdf_with_content(output_path):
    recipes_data = loads.library.get_recipe_data()
    
    if not recipes_data:
        return

    font_size = 14
    
    for idx, recipe in enumerate(recipes_data):
        text_content = f"[{idx+1}] {recipe['name']}\n\nInvented by: {recipe.get('inventor', 'Unknown')}"
        
        pdf_output.cell(50, 8) 
        if recipe['color']:
            pdf_output.text(recipe['color'], color=127, align='C')
        else:
            pdf_output.text("Color Unknown", color
