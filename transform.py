def transform_data(data):
    data.columns = [column.lower().strip().replace(" ", "_")
                    for column in data.columns]
    data = data.drop_duplicates()
    data["total_amount"] = data["quantity"] * data["price"]
    return data
