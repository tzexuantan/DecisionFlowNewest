import pandas as pd

certification = pd.read_csv("itjob_certification.csv")
header = pd.read_csv("itjob_header.csv")

merged_df = pd.merge(header, certification, on='jobid', how='left')

merged_df.to_excel('Certificate.xlsx', index=False)