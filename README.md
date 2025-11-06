# Huron IRB Data Migration v2

Enhanced project including Submissions and Document ZIP import generator.

## Commands
```bash
pip install -r requirements.txt
python scripts/transform_protocols.py
python scripts/transform_submissions.py
python scripts/generate_document_zip.py
python scripts/validate_hrn_file.py
```
Outputs:
- output/irb_protocols_transformed.csv
- output/irb_submissions_transformed.csv
- output/document_import.zip
