import pandas as pd
import re


def load_mabl_data(mabl_paths: dict) -> dict:
    mabl_data = {}
    for lang, path in mabl_paths.items():
        mabl_data[lang] = pd.read_csv(path)
    return mabl_data


def load_maps_data(maps_paths: dict) -> dict:
    maps_data = {}
    for lang, path in maps_paths.items():
        # preprocessing
        df = pd.read_excel(path)
        df = df[df["is_figurative"] == 1]
        df = df.drop(
            columns=["explanation", "is_figurative", "answer3"], errors="ignore"
        )
        df["answer_key"] = df["answer_key"].str.upper()

        # save
        maps_data[lang] = df

    return maps_data


def classify_gemini_maps_response(response: str):
    pattern = r"(?:The correct (?:interpretation|answer) is|The answer is) \*?\*?([AB])(?:\:|\.|$)"

    match = re.search(pattern, response, re.IGNORECASE)

    if match:
        return match.group(1)  # Returns 'A' or 'B'
    else:
        return "Uncertain"
