# import re
# import csv
# import os
# import time
# from generate_feedback import query_uf_ai, build_assessment_prompt, build_process_prompt, build_interaction_prompt

# # === Config ===
# INPUT_FILE = "train.txt"
# OUTPUT_FILE = "final_api_feedback_output.csv"
# BATCH_SIZE = 35

# def load_dialogues():
#     with open(INPUT_FILE, "r", encoding="utf-8") as f:
#         content = f.read().lower()
#     raw_dialogues = re.findall(r"<dialogue>(.*?)</dialogue>", content, re.DOTALL)
#     return [dlg.strip().replace("<eos>", " | ") for dlg in raw_dialogues]

# def initialize_csv():
#     if not os.path.exists(OUTPUT_FILE):
#         with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as f:
#             writer = csv.writer(f)
#             writer.writerow([
#                 "Dialogue ID", "Dialogue Text",
#                 "Assessment-Oriented Feedback",
#                 "Process-Based Feedback",
#                 "Interaction & Communication Feedback"
#             ])

# def get_last_processed_index():
#     if not os.path.exists(OUTPUT_FILE):
#         return 0
#     with open(OUTPUT_FILE, "r", encoding="utf-8") as f:
#         return sum(1 for line in f) - 1  # exclude header

# def append_feedback_to_csv(dialogue_id, dialogue, assessment, process, interaction):
#     with open(OUTPUT_FILE, "a", newline="", encoding="utf-8") as f:
#         writer = csv.writer(f)
#         writer.writerow([
#             f"Dialogue {dialogue_id}", dialogue,
#             assessment.strip(), process.strip(), interaction.strip()
#         ])

# # === Main Processing ===
# initialize_csv()
# dialogues = load_dialogues()
# total = len(dialogues)
# start_index = get_last_processed_index()
# end_index = min(start_index + BATCH_SIZE, total)

# print(f"\n🔁 Processing batch: Dialogues {start_index+1} to {end_index} of {total}")

# for idx in range(start_index, end_index):
#     dialogue = dialogues[idx]
#     print(f"\nProcessing Dialogue {idx+1}...")

#     assessment_prompt = build_assessment_prompt(dialogue)
#     process_prompt = build_process_prompt(dialogue)
#     interaction_prompt = build_interaction_prompt(dialogue)

#     assessment = query_uf_ai(assessment_prompt)
#     time.sleep(1)  # avoid rate limit
#     process = query_uf_ai(process_prompt)
#     time.sleep(1)
#     interaction = query_uf_ai(interaction_prompt)
#     time.sleep(1)

#     append_feedback_to_csv(idx+1, dialogue, assessment, process, interaction)

# print(f"\n✅ Batch complete. Results saved to: {OUTPUT_FILE}")
import re
import csv
import os
import time
import pandas as pd
from generate_feedback import query_uf_ai, build_assessment_prompt, build_process_prompt, build_interaction_prompt

# === Config ===
INPUT_FILE = "train.txt"
OUTPUT_FILE_CSV = "final_api_feedback_output.csv"
OUTPUT_FILE_XLSX = "final_api_feedback_output.xlsx"
BATCH_SIZE = 35

def load_dialogues():
    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        content = f.read().lower()
    raw_dialogues = re.findall(r"<dialogue>(.*?)</dialogue>", content, re.DOTALL)
    return [dlg.strip().replace("<eos>", " | ") for dlg in raw_dialogues]

def initialize_csv():
    if not os.path.exists(OUTPUT_FILE_CSV):
        with open(OUTPUT_FILE_CSV, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow([
                "Dialogue ID", "Dialogue Text",
                "Assessment-Oriented Feedback",
                "Process-Based Feedback",
                "Interaction & Communication Feedback"
            ])

def get_last_processed_index():
    if not os.path.exists(OUTPUT_FILE_CSV):
        return 0
    with open(OUTPUT_FILE_CSV, "r", encoding="utf-8") as f:
        return sum(1 for line in f) - 1  # exclude header

def clean_markdown(text):
    if not text:
        return ""
    text = text.replace("**", "")  # Remove markdown bold markers
    text = text.replace("*", "")   # Remove other asterisks
    text = text.replace("•", "-")  # Replace bullets
    return text.strip()

def append_feedback_to_csv(dialogue_id, dialogue, assessment, process, interaction):
    with open(OUTPUT_FILE_CSV, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([
            f"Dialogue {dialogue_id}",
            dialogue,
            clean_markdown(assessment),
            clean_markdown(process),
            clean_markdown(interaction)
        ])

def convert_csv_to_xlsx():
    df = pd.read_csv(OUTPUT_FILE_CSV)
    df.to_excel(OUTPUT_FILE_XLSX, index=False)

# === Main Execution ===
initialize_csv()
dialogues = load_dialogues()
total = len(dialogues)
start_index = get_last_processed_index()
end_index = min(start_index + BATCH_SIZE, total)

print(f"\n🔁 Processing batch: Dialogues {start_index+1} to {end_index} of {total}")

for idx in range(start_index, end_index):
    dialogue = dialogues[idx]
    print(f"\nProcessing Dialogue {idx+1}...")

    assessment_prompt = build_assessment_prompt(dialogue)
    process_prompt = build_process_prompt(dialogue)
    interaction_prompt = build_interaction_prompt(dialogue)

    assessment = query_uf_ai(assessment_prompt)
    time.sleep(1)
    process = query_uf_ai(process_prompt)
    time.sleep(1)
    interaction = query_uf_ai(interaction_prompt)
    time.sleep(1)

    append_feedback_to_csv(idx+1, dialogue, assessment, process, interaction)

convert_csv_to_xlsx()
print(f"\n✅ Batch complete. Feedback saved to '{OUTPUT_FILE_XLSX}'")

