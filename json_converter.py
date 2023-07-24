import json
import openpyxl


def convert_json_to_xlsx(input_file, output_file):
    try:
        with open(input_file, 'r') as json_file:
            data = json.load(json_file)

        for item in data:
            item['comment_id_safe'] = item.pop('comment_id', None)

        workbook = openpyxl.Workbook()
        sheet = workbook.active

        headers = list(data[0].keys())
        sheet.append(headers)

        for item in data:
            sheet.append(list(item.values()))

        workbook.save(output_file)
        print("Conversion successfully completed.")
    except Exception as e:
        print(f"Exception: {e}. Failed to convert JSON to XLSX.")


convert_json_to_xlsx(
    input_file='file.json',
    output_file='file.xlsx')
