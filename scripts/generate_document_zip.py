import os, zipfile, urllib.parse, uuid

TENANT_CODE = "bostonu"
IMPORT_ID = "import2025"
SERVICE_NAME = "irb"
SRC_DIR = "data/documents"
OUT_ZIP = "output/document_import.zip"

def make_zip():
    with zipfile.ZipFile(OUT_ZIP, "w", zipfile.ZIP_DEFLATED) as zipf:
        for file in os.listdir(SRC_DIR):
            if not file.endswith(".pdf"):
                continue
            base, _ = os.path.splitext(file)
            protocol_id = base.split("_")[-1]
            project_hrn = urllib.parse.quote(f"hrn:hrs:irb:{protocol_id}", safe="")
            category_hrn = urllib.parse.quote("hrn:hrs:lists:document-category/protocol-document", safe="")
            doc_id = uuid.uuid4().hex
            folder = f"scan/{TENANT_CODE}/document/import_v2/{IMPORT_ID}/{SERVICE_NAME}/{project_hrn}/{category_hrn}/{doc_id}/_unknown_/1/"
            zipf.write(os.path.join(SRC_DIR, file), arcname=f"{folder}{file}")
    print(f"✅ Document import ZIP created: {OUT_ZIP}")

if __name__ == "__main__":
    make_zip()
