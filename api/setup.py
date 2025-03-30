import os

def create_project_structure(project_name):
    folders = [
        project_name,
        f"{project_name}/app",
        f"{project_name}/app/routes",
        f"{project_name}/app/models",
        f"{project_name}/app/schemas",
        f"{project_name}/app/services",
        f"{project_name}/app/utils",
        f"{project_name}/app/filters"
    ]

    files = {
        f"{project_name}/main.py": "from fastapi import FastAPI\n\napp = FastAPI()\n\n@app.get('/')\ndef read_root():\n    return {\"message\": \"Welcome to FastAPI!\"}\n",
        f"{project_name}/app/routes/items.py": "from fastapi import APIRouter, Query\nfrom typing import List, Optional\n\nrouter = APIRouter()\n\n@router.get('/items/')\ndef get_items(q: Optional[str] = Query(None, min_length=2, max_length=50)):\n    return {\"query\": q}\n",
        f"{project_name}/app/filters/item_filter.py": "def filter_items(items, query):\n    return [item for item in items if query.lower() in item.lower() if query]",
        f"{project_name}/app/models/item.py": "from pydantic import BaseModel\n\nclass Item(BaseModel):\n    name: str\n    description: str = None\n    price: float\n    tax: float = None\n",
        f"{project_name}/app/schemas/item_schema.py": "from pydantic import BaseModel\n\nclass ItemSchema(BaseModel):\n    name: str\n    description: str\n    price: float\n",
        f"{project_name}/app/services/item_service.py": "from ..models.item import Item\n\ndef get_item_details():\n    return Item(name='Sample', description='A sample item', price=9.99, tax=0.5)",
        f"{project_name}/app/utils/helper.py": "def format_price(price):\n    return f'${price:.2f}'\n"
    }

    for folder in folders:
        os.makedirs(folder, exist_ok=True)
    
    for file, content in files.items():
        with open(file, 'w') as f:
            f.write(content)

    print(f"FastAPI project '{project_name}' created successfully!")

if __name__ == "__main__":
    project_name = "fastapi_project"
    create_project_structure(project_name)
