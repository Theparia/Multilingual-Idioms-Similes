MAPS_ORIGINAL_LANGUAGE_PATHS = {
    # "English": "data/MAPS/en/test_proverbs.xlsx",
    # "Indonesian": "data/MAPS/id/test_proverbs.xlsx",
    # "Chinese": "data/MAPS/zh/test_proverbs.xlsx",
    # "Russian": "data/MAPS/ru/test_proverbs.xlsx",
    # "German": "data/MAPS/de/test_proverbs.xlsx",
    # "Bengali": "data/MAPS/bn/test_proverbs.xlsx",
    "Persian": "data/MAPS/fa/test_proverbs.xlsx",
}

MAPS_ENGLISH_TRANSLATED_PATHS = {
    # "Indonesian": "data/MAPS/id/machine_translation_2en.xlsx",
    # "Chinese": "data/MAPS/zh/machine_translation_2en.xlsx",
    # "Russian": "data/MAPS/ru/machine_translation_2en.xlsx",
    # "German": "data/MAPS/de/machine_translation_2en.xlsx",
    # "Bengali": "data/MAPS/bn/machine_translation_2en.xlsx",
    "Persian": "data/MAPS/fa/machine_translation_2en.xlsx",
}

MABL_ORIGINAL_LANGUAGE_PATHS = {
    # "English": "data/MABL/sampled_langdata/en_dev.csv",
    # "Indonesian": "data/MABL/sampled_langdata/id.csv",
    # "Hindi": "data/MABL/sampled_langdata/hi.csv",
    # "Javanese": "data/MABL/sampled_langdata/jv.csv",
    # "Kannada": "data/MABL/sampled_langdata/kn.csv",
    # "Swahili": "data/MABL/sampled_langdata/sw.csv",
    # "Sundanese": "data/MABL/sampled_langdata/su.csv",
    "Persian": "data/MABL/sampled_langdata/fa.csv",
}

MABL_ENGLISH_TRANSLATED_PATHS = {
    # "Indonesian": "data/MABL/sampled_translate-test/id_id.csv",
    # "Hindi": "data/MABL/sampled_translate-test/hi_hi.csv",
    # "Javanese": "data/MABL/sampled_translate-test/jv_jv.csv",
    # "Kannada": "data/MABL/sampled_translate-test/kn_kn.csv",
    # "Swahili": "data/MABL/sampled_translate-test/sw_sw.csv",
    # "Sundanese": "data/MABL/sampled_translate-test/su_su.csv",
    "Persian": "data/MABL/sampled_translate-test/fa_fa.csv",
}

MAPS_DATASET_NAME = "maps"
MABL_DATASET_NAME = "mabl"

ORIGINAL_LANGUGAE = "original"
TRANSLATED = "english"

MABL_ANSWER_COLUMN_NAME = "labels"
MAPS_ANSWER_COLUMN_NAME = "answer_key"

GPT_MODEL_NAME = "gpt"
GEMINI_MODEL_NAME = "gemini"

ZERO_SHOT_PROMPTING_NAME = "zero_shot"
ONE_SHOT_PROMPTING_NAME = "one_shot"
CHAIN_OF_THOUGHT_PROMPTING_NAME = "chain_of_thought"
SELF_TRANSLATION_PROMPTING_NAME = "self_translation"

NUMBER_OF_TRIALS = 3
NUMBER_OF_ATTEMPTS = 3
EXCEPTION_SLEEP_TIME = 10
