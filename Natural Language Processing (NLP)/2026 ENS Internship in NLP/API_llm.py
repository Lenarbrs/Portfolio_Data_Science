import pandas as pd
# from openai import OpenAI # for chat gpt
from google import genai # for Gemini 
import time
import os
import traceback
from google.genai import types



#===================================
# Script for Chat GPT (gpt-4o-mini, gpt-5o-mini)
#===================================

# print("=== SCRIPT STARTED ===")

# client = OpenAI()

# # Ensure output directory exists
# os.makedirs("data/reconstructed", exist_ok=True)

# # Load distorted dataset
# df = pd.read_csv("data/distorted/wiki_distorted_LPCMKRE.csv")

# print("Columns in dataset:", df.columns.tolist())

# output_file = "data/reconstructed/wiki_reconstructed_LLM_LPCMKRE.csv"

# reconstructed_texts = []

# developer_prompt = """You are a deterministic reconstruction system.
# Rules:
# - Each 'x' represents exactly one letter.
# - The number of letters in each reconstructed word must be identical to the number of characters in its masked form.
# - Only 'x' characters may be replaced.
# - Every non-'x' character must remain exactly unchanged.
# - Word boundaries must remain identical.
# - Spacing must remain identical.
# - Punctuation must remain identical.
# - Capitalization must match exactly.
# - If any single word violates the exact character count, the output is invalid.
# - Do not optimize for plausibility over structural accuracy.
# - Output ONLY the reconstructed paragraph.
# - No explanations.
# - No comments.
# """

# # TEST ONLY FIRST ROW FIRST
# # Change to range(len(df)) when working
# for i in range(1):

#     distorted_text = df.loc[i, "text"]

#     try:
#         response = client.chat.completions.create(
#             model="gpt-4o-mini", # One of the cheapest models, however i think it is not good enough for this task (I tried gpt-5o-mini too)
#             temperature=0, # in our case, i think it is better to have a deterministic output, so we set temperature to 0
#             messages=[
#                 {"role": "developer", "content": developer_prompt},
#                 {"role": "user", "content": distorted_text}
#             ]
#         )

#         reconstructed = response.choices[0].message.content.strip()

#         reconstructed_texts.append(reconstructed)

#         print("\n=== SUCCESS ===")
#         print("Original distorted:")
#         print(distorted_text[:300])
#         print("\nReconstructed:")
#         print(reconstructed[:300])

#     except Exception:
#         print(f"\n=== ERROR AT ROW {i} ===")
#         traceback.print_exc()
#         reconstructed_texts.append("ERROR")

#     time.sleep(0.5)

# print("\n=== TEST FINISHED ===")

# # Uncomment below when test works

# """
# final_df = pd.DataFrame({
#     "id": df["id"],
#     "text": reconstructed_texts
# })

# final_df.to_csv(output_file, index=False)

# print("Saved to:", output_file)
# """

# ===================================
# Script for Gemini 
# ===================================

print("=== SCRIPT STARTED (GEMINI FEWSHOT) ===")

# ===================================
# CONFIGURATION
# ===================================

TEST_MODE = False   # first line if true
                   # false = full dataset

INPUT_FILE = "data/distorted/wiki_distorted_LPCMKRE.csv"

OUTPUT_FILE_TEST = "data/reconstructed/wiki_reconstructed_GEMINI_TEST.csv"
OUTPUT_FILE_FULL = "data/reconstructed/wiki_reconstructed_GEMINI_FEWSHOT.csv"

THINKING_FILE_TEST = "data/reconstructed/wiki_thinking_GEMINI_TEST.csv"
THINKING_FILE_FULL = "data/reconstructed/wiki_thinking_GEMINI_FEWSHOT.csv"

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

df = pd.read_csv(INPUT_FILE)

print("Columns:", df.columns.tolist())

os.makedirs("data/reconstructed", exist_ok=True)

# ===================================
# PROMPT
# ===================================

developer_prompt = """
You will be shown a paragraph from Wikipedia that has been heavily distorted, with many letters replaced by the character "x".

Your task is to recover the original paragraph by determining what the missing words are and restoring the text to its most likely original form.

Each "x" represents exactly one missing letter. The structure of the paragraph (including spacing, punctuation, capitalization, and word length) must remain unchanged.

Only output the recovered paragraph. Do not return a question or any additional information.
"""

# ===================================
# EXAMPLES
# ===================================

example1_distorted = """Before the xxxxxxxxx of xxxxxxxxxxx-xxxxed xxxxxs in 2017, some xxxxxxxx xxxxxs were xxxxxxxxxx xxxxx xxxxxxxx to the xxxxxxxxxxxxx and xxxx xxxxxxxxxxx of their xxxx. 
In the xxxxx 1990s, XXX's xxxxxxxxxxx xxxxxs xxxxxxxed xxxx xxxxxxxxx xxxxxxxxxx for xxxxxxx xxxxxxxxxxx, xxxing the xxxxxxxxxx for xxxxxx-xxxxed xxxxxxxx xxxxxxxx.
"""

example1_original = """Before the emergence of transformer-based models in 2017, some language models were considered large relative to the computational and data constraints of their time. 
In the early 1990s, IBM's statistical models pioneered word alignment techniques for machine translation, laying the groundwork for corpus-based language modeling.
"""

example2_distorted = """It may be xxxxxxxx with xxxed xxxxx xxxx as xxxxxxxx or xxxxxxs, or xxxxx xxxxxx xxxx as xxxxxs. 
In Xxxxxx and Xxxxx, xxxxxxxxxs are xxxxxxxxx xxxx without xxxxxxx and xxxen without xxxxed xxxxxx, but xxxxxxxxx with xxxxxx xxxxxxx.
"""

example2_original = """It may be flavored with dried fruit such as sultanas or raisins, or other fruits such as apples. 
In France and Spain, croissants are generally sold without filling and eaten without added butter, but sometimes with almond filling.
"""

# ===================================
# BUILD MULTI-TURN PROMPT
# ===================================

def build_messages(distorted_text):

    return [

        types.Content(
            role="user",
            parts=[types.Part.from_text(text=developer_prompt)]
        ),

        types.Content(
            role="user",
            parts=[types.Part.from_text(text=example1_distorted)]
        ),

        types.Content(
            role="model",
            parts=[types.Part.from_text(text=example1_original)]
        ),

        types.Content(
            role="user",
            parts=[types.Part.from_text(text=example2_distorted)]
        ),

        types.Content(
            role="model",
            parts=[types.Part.from_text(text=example2_original)]
        ),

        types.Content(
            role="user",
            parts=[types.Part.from_text(text=distorted_text)]
        ),
    ]


# ===================================
# DATASET MODE
# ===================================

if TEST_MODE:
    indices = [0]
    output_file = OUTPUT_FILE_TEST
    thinking_file = THINKING_FILE_TEST
    print("=== TEST MODE ===")
else:
    indices = range(len(df))
    output_file = OUTPUT_FILE_FULL
    thinking_file = THINKING_FILE_FULL
    print("=== FULL DATASET MODE")


# ===================================
# GENERATION LOOP
# ===================================

answers = []
thinking_list = []
ids = []

for i in indices:

    distorted_text = df.loc[i, "text"]
    idx = df.loc[i, "id"]

    try:

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=build_messages(distorted_text),
            config={
                "max_output_tokens": 10000
            }
        )

        reconstructed = response.text.strip()

        thinking = ""

        try:
            candidate = response.candidates[0]

            if hasattr(candidate, "content"):
                thinking = str(candidate.content)

        except Exception:
            thinking = ""

        answers.append(reconstructed)
        thinking_list.append(thinking)
        ids.append(idx)

        if TEST_MODE:

            print("\n" + "=" * 80)
            print("DISTORTED TEXT:\n")
            print(distorted_text)

            print("\nRECONSTRUCTED TEXT:\n")
            print(reconstructed)

            print("\nRAW THINKING DATA:\n")
            print(thinking)

            print("=" * 80 + "\n")

        print(f"Done {i+1}/{len(df)}")

    except Exception:

        print(f"\nERROR AT ROW {i}")
        traceback.print_exc()

        answers.append("ERROR")
        thinking_list.append("ERROR")
        ids.append(idx)

    time.sleep(0.5)


# ===================================
# SAVE OUTPUT
# ===================================

result_df = pd.DataFrame({
    "id": ids,
    "text": answers
})

thinking_df = pd.DataFrame({
    "id": ids,
    "thinking": thinking_list
})

result_df.to_csv(output_file, index=False)
thinking_df.to_csv(thinking_file, index=False)

print("Saved reconstruction:", output_file)
print("Saved thinking:", thinking_file)

print("=== FINISHED ===")


#### Old code with example directly in the prompt, without multi-turn structure, and without thinking extraction (not used in final version, but kept here for reference) ---   


# print("=== SCRIPT STARTED (GEMINI NEW API) ===")


# # CONFIGURATION --- 

# TEST_MODE = False   # first line if true
#                    # false = full dataset

# INPUT_FILE = "data/distorted/wiki_distorted_LPCMKRE.csv"
# OUTPUT_FILE_TEST = "data/reconstructed/wiki_reconstructed_GEMINI_TEST.csv"
# OUTPUT_FILE_FULL = "data/reconstructed/wiki_reconstructed_GEMINI_NEW_PROMPT_LPCMKRE.csv"


# client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))


# df = pd.read_csv(INPUT_FILE)
# print("Columns in dataset:", df.columns.tolist())

# os.makedirs("data/reconstructed", exist_ok=True)


# developer_prompt = """
# You will be shown a paragraph from Wikipedia that has been heavily distorted, with many letters replaced by the character "x".

# Your task is to recover the original paragraph by determining what the missing words are and restoring the text to its most likely original form.

# Each "x" represents exactly one missing letter. The structure of the paragraph (including spacing, punctuation, capitalization, and word length) must remain unchanged.

# Only output the recovered paragraph. Do not return a question or any additional information.

# For example, if the distorted text is "Before the xxxxxxxxx of xxxxxxxxxxx-xxxxed xxxxxs in 2017, some xxxxxxxx xxxxxs were xxxxxxxxxx xxxxx xxxxxxxx to the xxxxxxxxxxxxx and xxxx xxxxxxxxxxx of their xxxx. 
# In the xxxxx 1990s, XXX's xxxxxxxxxxx xxxxxs xxxxxxxed xxxx xxxxxxxxx xxxxxxxxxx for xxxxxxx xxxxxxxxxxx, xxxing the xxxxxxxxxx for xxxxxx-xxxxed xxxxxxxx xxxxxxxx."
# You should output the original text "Before the emergence of transformer-based models in 2017, some language models were considered large relative to the computational and data constraints of their time. 
# In the early 1990s, IBM's statistical models pioneered word alignment techniques for machine translation, laying the groundwork for corpus-based language modeling."
# """

# # DEFINE INDICES --- 

# if TEST_MODE:
#     indices = [0]
#     output_file = OUTPUT_FILE_TEST
#     print("=== TEST MODE (1 row only) ===")
# else:
#     indices = range(len(df))
#     output_file = OUTPUT_FILE_FULL
#     print("=== FULL DATASET MODE ===")


# # GENERATION LOOP ---

# reconstructed_texts = []

# for i in indices:

#     distorted_text = df.loc[i, "text"]

#     try:
#         response = client.models.generate_content(
#             model="gemini-2.5-flash",
#             contents=developer_prompt + "\n\n" + distorted_text,
#             config={
#                 "max_output_tokens": 10000
#             }
#         )

#         reconstructed = response.text.strip()
#         reconstructed_texts.append(reconstructed)

#         # Affichage en mode test uniquement
#         if TEST_MODE:
#             print("\n" + "=" * 80)
#             print("DISTORTED TEXT:\n")
#             print(distorted_text)
#             print("\n" + "-" * 80)
#             print("RECONSTRUCTED TEXT:\n")
#             print(reconstructed)
#             print("=" * 80 + "\n")

#         print(f"Done {i+1}/{len(df)}")

#     except Exception:
#         print(f"\nERROR AT ROW {i}")
#         traceback.print_exc()
#         reconstructed_texts.append("ERROR")

#     time.sleep(0.5)
# # Save --- 

# if TEST_MODE:
#     result_df = pd.DataFrame({
#         "id": [df.loc[0, "id"]],
#         "text": reconstructed_texts
#     })
# else:
#     result_df = pd.DataFrame({
#         "id": df.loc[indices, "id"],
#         "text": reconstructed_texts
#     })

# result_df.to_csv(output_file, index=False)

# print("=== FINISHED ===")
# print("Saved to:", output_file)

