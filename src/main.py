from dotenv import load_dotenv
import os
import time
import pandas as pd
from tqdm import tqdm

from consts import (
    CHAIN_OF_THOUGHT_PROMPTING_NAME,
    EXCEPTION_SLEEP_TIME,
    GEMINI_MODEL_NAME,
    GPT_MODEL_NAME,
    MABL_ANSWER_COLUMN_NAME,
    MABL_DATASET_NAME,
    MABL_ENGLISH_TRANSLATED_PATHS,
    MABL_ORIGINAL_LANGUAGE_PATHS,
    MAPS_ANSWER_COLUMN_NAME,
    MAPS_DATASET_NAME,
    MAPS_ENGLISH_TRANSLATED_PATHS,
    MAPS_ORIGINAL_LANGUAGE_PATHS,
    NUMBER_OF_ATTEMPTS,
    NUMBER_OF_TRIALS,
    ONE_SHOT_PROMPTING_NAME,
    ORIGINAL_LANGUGAE,
    SELF_TRANSLATION_PROMPTING_NAME,
    TRANSLATED,
    ZERO_SHOT_PROMPTING_NAME,
)
from models.model_interface import ModelInterface
from prompt_templates.MABL_prompts import MablPrompts
from utils import (
    classify_gemini_maps_response,
    load_mabl_data,
    load_maps_data,
)
from models.gpt import GPT
from models.gemini import Gemini
from prompt_templates.MAPS_prompts import MapsPrompts

load_dotenv()

gpt_api_key = os.getenv("GPT_API_KEY")
gemini_api_key = os.getenv("GEMINI_API_KEY")


def run_experiment(
    datasets: dict,
    prompt_function,
    model: ModelInterface,
    answer_column_name: str,
    classify_response_function,
    num_attempts: int,
    exception_sleep_time: int,
    output_file: str,
):
    results = []
    for language, df in datasets.items():
        print("language : ", language)
        for _, row in tqdm(df.iterrows(), total=df.shape[0]):
            prompt = prompt_function(language, row)
            for _ in range(num_attempts):
                try:
                    response = model.get_completion(prompt)
                    results.append(
                        {
                            "prompt": prompt,
                            "response": response,
                            "predict": (
                                classify_response_function(response)
                                if classify_response_function
                                else ""
                            ),
                            "answer_key": row[answer_column_name],
                            "language": language,
                        }
                    )
                    break
                except Exception as e:
                    # Save intermediate results
                    df_results = pd.DataFrame(results)
                    df_results.to_csv(f"{os.getcwd()}/{output_file}")

                    print("Exception: ", e)
                    print(f"Sleeping for {exception_sleep_time} seconds...")

                    time.sleep(exception_sleep_time)
                    continue

        # Save results after each language processing
        df_results = pd.DataFrame(results)
        df_results.to_csv(f"{os.getcwd()}/{output_file}")


if __name__ == "__main__":
    dataset_choice = (
        input(f"Enter dataset choice ({MAPS_DATASET_NAME}/{MABL_DATASET_NAME}): ")
        .strip()
        .lower()
    )
    orginal_or_translated_choice = (
        input(f"Enter your language preference ({ORIGINAL_LANGUGAE}/{TRANSLATED}): ")
        .strip()
        .lower()
    )
    model_choice = (
        input(f"Enter model choice ({GPT_MODEL_NAME}/{GEMINI_MODEL_NAME}): ")
        .strip()
        .lower()
    )
    prompt_engineering_choice = (
        input(
            f"Enter prompt engineering choice ({ZERO_SHOT_PROMPTING_NAME}/{ONE_SHOT_PROMPTING_NAME}/{CHAIN_OF_THOUGHT_PROMPTING_NAME}/{SELF_TRANSLATION_PROMPTING_NAME}): "
        )
        .strip()
        .lower()
    )

    if dataset_choice == MAPS_DATASET_NAME:
        answer_column_name = MAPS_ANSWER_COLUMN_NAME
        if orginal_or_translated_choice == ORIGINAL_LANGUGAE:
            datasets = load_maps_data(maps_paths=MAPS_ORIGINAL_LANGUAGE_PATHS)
        elif orginal_or_translated_choice == TRANSLATED:
            datasets = load_maps_data(maps_paths=MAPS_ENGLISH_TRANSLATED_PATHS)
        else:
            raise ValueError(
                f"Unsupported language prefernece: {orginal_or_translated_choice}"
            )
    elif dataset_choice == MABL_DATASET_NAME:
        answer_column_name = MABL_ANSWER_COLUMN_NAME
        if orginal_or_translated_choice == ORIGINAL_LANGUGAE:
            datasets = load_mabl_data(mabl_paths=MABL_ORIGINAL_LANGUAGE_PATHS)
        elif orginal_or_translated_choice == TRANSLATED:
            datasets = load_mabl_data(mabl_paths=MABL_ENGLISH_TRANSLATED_PATHS)
        else:
            raise ValueError(
                f"Unsupported language prefernece: {orginal_or_translated_choice}"
            )
    else:
        raise ValueError(f"Unsupported dataset: {dataset_choice}")

    if model_choice == GPT_MODEL_NAME:
        model = GPT(api_key=gpt_api_key)
        if gpt_api_key == "":
            raise ValueError(
                "The GPT API key is missing. Please ensure it is correctly set in your .env file."
            )
    elif model_choice == GEMINI_MODEL_NAME:
        model = Gemini(api_key=gemini_api_key)
        if gemini_api_key == "":
            raise ValueError(
                "The Gemini API key is missing. Please ensure it is correctly set in your .env file."
            )
    else:
        raise ValueError(f"Unsupported model: {model_choice}")

    if dataset_choice == MAPS_DATASET_NAME:
        maps_prompts = MapsPrompts()
        if prompt_engineering_choice == ZERO_SHOT_PROMPTING_NAME:
            prompt_function = maps_prompts.zero_shot
        elif prompt_engineering_choice == ONE_SHOT_PROMPTING_NAME:
            if orginal_or_translated_choice == ORIGINAL_LANGUGAE:
                prompt_function = maps_prompts.one_shot_original_language
            else:
                prompt_function = maps_prompts.one_shot_english_translated
        elif prompt_engineering_choice == CHAIN_OF_THOUGHT_PROMPTING_NAME:
            if orginal_or_translated_choice == ORIGINAL_LANGUGAE:
                prompt_function = maps_prompts.chain_of_thought_original_language
            else:
                prompt_function = maps_prompts.chain_of_thought_english_translated
        elif prompt_engineering_choice == SELF_TRANSLATION_PROMPTING_NAME:
            prompt_function = maps_prompts.self_translation
        else:
            raise ValueError(
                f"Unsupported prompt engineering method: {prompt_engineering_choice}"
            )
    elif dataset_choice == MABL_DATASET_NAME:
        mabl_prompts = MablPrompts()
        if prompt_engineering_choice == ZERO_SHOT_PROMPTING_NAME:
            prompt_function = mabl_prompts.zero_shot
        elif prompt_engineering_choice == ONE_SHOT_PROMPTING_NAME:
            if orginal_or_translated_choice == ORIGINAL_LANGUGAE:
                prompt_function = mabl_prompts.one_shot_original_language
            else:
                prompt_function = mabl_prompts.one_shot_english_translated
        elif prompt_engineering_choice == CHAIN_OF_THOUGHT_PROMPTING_NAME:
            if orginal_or_translated_choice == ORIGINAL_LANGUGAE:
                prompt_function = mabl_prompts.chain_of_thought_original_language
            else:
                prompt_function = mabl_prompts.chain_of_thought_english_translated
        elif prompt_engineering_choice == SELF_TRANSLATION_PROMPTING_NAME:
            prompt_function = mabl_prompts.self_translation
        else:
            raise ValueError(
                f"Unsupported prompt engineering method: {prompt_engineering_choice}"
            )

    classify_response_function = None
    if dataset_choice == MAPS_DATASET_NAME:
        if model_choice == GEMINI_MODEL_NAME:
            classify_response_function = classify_gemini_maps_response

    for trial in range(NUMBER_OF_TRIALS):
        output_dir = f"results/{model_choice}/{dataset_choice}/{orginal_or_translated_choice}/{prompt_engineering_choice}"
        os.makedirs(output_dir, exist_ok=True)
        output_filename = f"{output_dir}/{trial+1}.csv"

        print(f"Beginning trial {trial}...")

        run_experiment(
            datasets=datasets,
            prompt_function=prompt_function,
            model=model,
            answer_column_name=answer_column_name,
            classify_response_function=classify_response_function,
            num_attempts=NUMBER_OF_ATTEMPTS,
            exception_sleep_time=EXCEPTION_SLEEP_TIME,
            output_file=output_filename,
        )
