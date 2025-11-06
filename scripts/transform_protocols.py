import pandas as pd
import json, yaml, os

with open("config/settings.yaml", "r") as f:
    cfg = yaml.safe_load(f)

protocols = pd.read_csv(cfg["source"]["protocols_file"])
personnel = pd.read_csv(cfg["source"]["personnel_file"])
with open(cfg["source"]["list_mapping_file"], "r") as f:
    review_map = json.load(f)

protocols = protocols.rename(columns={
    "STUDY_TITLE": "protocolTitle",
    "PI_NETID": "principalInvestigator:hrn",
    "REVIEW_TYPE": "reviewType:hrn",
    "APPROVAL_DT": "approvalDate",
    "ACTIVE_FLAG": "active"
})

protocols["reviewType:hrn"] = protocols["reviewType:hrn"].map(
    lambda x: f"{cfg['hrn_prefix']['review_type']}{review_map.get(x, x.lower().replace(' ', '-'))}"
)

protocols["principalInvestigator:hrn"] = protocols["principalInvestigator:hrn"].apply(
    lambda netid: f"{cfg['hrn_prefix']['person']}{netid}"
)

protocols["active"] = protocols["active"].map({"Y": True, "N": False})
protocols["approvalDate"] = pd.to_datetime(protocols["approvalDate"]).dt.strftime("%Y-%m-%d")

people_dict = personnel.groupby("PROTOCOL_ID")["PERSON_ID"].apply(list).to_dict()
protocols["personnel::hrn"] = protocols["PROTOCOL_ID"].map(
    lambda pid: json.dumps([f"{cfg['hrn_prefix']['person']}{p}" for p in people_dict.get(pid, [])])
)

protocols["protocol:hrn"] = protocols["PROTOCOL_ID"].apply(lambda x: f"{cfg['hrn_prefix']['protocol']}{x}")

final_cols = ["protocol:hrn","protocolTitle","principalInvestigator:hrn","reviewType:hrn","personnel::hrn","approvalDate","active"]
df_out = protocols[final_cols]

os.makedirs(cfg["target"]["output_dir"], exist_ok=True)
output_file = os.path.join(cfg["target"]["output_dir"], cfg["target"]["protocols_output"])
df_out.to_csv(output_file, index=False, encoding="utf-8")
print(f"✅ Protocols file created: {output_file}")
