from api import get_api_data
from db import get_db_data
from compare import compare_data

api_data = get_api_data()
db_data = get_db_data()

results = compare_data(api_data, db_data)

print("\nMISMATCH REPORT")
print("=" * 50)

for item in results:
    print(
        f"Order ID: {item['order_id']}\n"
        f"API Amount: {item['api_amount']}\n"
        f"DB Amount: {item['db_amount']}\n"
        f"Reason: {item['reason']}\n"
        f"{'-' * 50}"
    )