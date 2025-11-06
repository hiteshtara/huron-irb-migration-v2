import pandas as pd
import yaml, os

with open("config/settings.yaml", "r") as f:
    cfg = yaml.safe_load(f)

submissions = pd.read_csv(cfg["source"]["submissions_file"])

submissions = submissions.rename(columns={
    "SUBMISSION_ID": "submission:id",
    "PROTOCOL_ID": "protocol:hrn",
    "SUBMISSION_TYPE": "submissionType:hrn",
    "STATUS": "submissionStatus:hrn",
    "REVIEW_DATE": "reviewDate"
})

type_map = {
    "Initial Review": "hrn:hrs:lists:submission-type:initial-review",
    "Amendment": "hrn:hrs:lists:submission-type:amendment"
}
status_map = {
    "Approved": "hrn:hrs:lists:submission-status:approved",
    "Under Review": "hrn:hrs:lists:submission-status:under-review"
}

submissions["submissionType:hrn"] = submissions["submissionType:hrn"].map(type_map)
submissions["submissionStatus:hrn"] = submissions["submissionStatus:hrn"].map(status_map)
submissions["protocol:hrn"] = submissions["protocol:hrn"].apply(lambda x: f"hrn:hrs:irb:{x}")
submissions["reviewDate"] = pd.to_datetime(submissions["reviewDate"]).dt.strftime("%Y-%m-%d")

os.makedirs(cfg["target"]["output_dir"], exist_ok=True)
outfile = os.path.join(cfg["target"]["output_dir"], cfg["target"]["submissions_output"])
submissions.to_csv(outfile, index=False, encoding="utf-8")
print(f"✅ Submissions file ready: {outfile}")
