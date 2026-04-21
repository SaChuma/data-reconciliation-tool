def compare_data(api_data, db_data):
    api_dict = {item["order_id"]: item["amount"] for item in api_data}
    db_dict = {item["order_id"]: item["amount"] for item in db_data}

    all_ids = set(api_dict.keys()).union(set(db_dict.keys()))

    mismatches = []

    for order_id in all_ids:
        api_amount = api_dict.get(order_id)
        db_amount = db_dict.get(order_id)

        reason = None

        if api_amount is None:
            reason = "Missing in API"

        elif db_amount is None:
            reason = "Missing in Database"

        elif api_amount != db_amount:
            reason = "Amount mismatch"

        if reason:
            mismatches.append({
                "order_id": order_id,
                "api_amount": api_amount,
                "db_amount": db_amount,
                "reason": reason
            })

    return mismatches