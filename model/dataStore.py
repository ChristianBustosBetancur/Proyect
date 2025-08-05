import json
from pathlib import Path
from model.client  import Client
from model.product import Product

BASE_DIR      = Path(__file__).parent.parent / "data"
CLIENTS_FILE  = BASE_DIR / "clients.json"
PRODUCTS_FILE = BASE_DIR / "products.json"

def LoadClients():
    try:
        text = CLIENTS_FILE.read_text(encoding="utf-8").strip()
        if not text:
            return {}         # está vacío
        raw = json.loads(text)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}             # no existe o no es JSON válido
    result = {}
    for cid, info in raw.items():
        result[cid] = Client.FromDict(info)
    return result

def SaveClients(clients):
    """Recibe dict{id: Client} y lo vuelca a JSON."""
    BASE_DIR.mkdir(exist_ok=True)
    raw = { cid: clients[cid].ToDict() for cid in clients }
    CLIENTS_FILE.write_text(json.dumps(raw, ensure_ascii=False, indent=2),encoding="utf-8")

def LoadProducts():
    """
    Carga productos desde JSON;
    si falta, está vacío o el JSON es inválido, devuelve el inventario por defecto.
    """
    Inventory = {
        'Water': Product('Water', 10, 3000),
        'Apple': Product('Apple', 5, 500),
    }
    try:
        RawText = PRODUCTS_FILE.read_text(encoding="utf-8").strip()
        if not RawText:
            return Inventory
        RawData = json.loads(RawText)
    except (FileNotFoundError, json.JSONDecodeError):
        return Inventory
    Result = {}
    for ProductName, ProductInfo in RawData.items():
        try:
            Result[ProductName] = Product.FromDict(ProductInfo)
        except:
            continue
    return Result or Inventory

def SaveProducts(products):
    """Recibe dict{name: Product} y lo vuelca a JSON."""
    BASE_DIR.mkdir(exist_ok=True)
    raw = { name: products[name].ToDict() for name in products }
    PRODUCTS_FILE.write_text(json.dumps(raw, ensure_ascii=False, indent=2),encoding="utf-8")