class MablPrompts:
    def zero_shot(self, language: str, row) -> str:
        return (
            f"In this task, you are given a start phrase indicating a figurative expression in {language} culture. "
            "Please select 0 if the start phrase conveys the meaning of ending 0, and 1 if it conveys the meaning of ending 1.\n\n"
            f"Start phrase: {row['startphrase']}\n"
            f"Ending 0: {row['ending1']}\n"
            f"Ending 1: {row['ending2']}\n"
            "Answer: \n"
        )

    def one_shot_original_language(self, language: str, row) -> str:
        return (
            f"In this task, you are given a start phrase indicating a figurative expression in {language} culture. "
            "Please select 0 if the start phrase conveys the meaning of ending 0, and 1 if it conveys the meaning of ending 1.\n"
            "Below is an example showing you how to do the task: \n\n"
            f"{self.ONE_SHOT_ORIGINAL_LANGUAGE_EXAMPLES[language]}\n\n"
            "Now answer the following question: \n\n"
            f"Start phrase: {row['startphrase']}\n"
            f"Ending 0: {row['ending1']}\n"
            f"Ending 1: {row['ending2']}\n"
            "Answer: \n"
        )

    def one_shot_english_translated(self, language: str, row) -> str:
        return (
            f"In this task, you are given a start phrase indicating a figurative expression in {language} culture. "
            "Please select 0 if the start phrase conveys the meaning of ending 0, and 1 if it conveys the meaning of ending 1.\n"
            "Below is an example showing you how to do the task: \n\n"
            f"{self.ONE_SHOT_ENGLISH_EXAMPLE[language]}\n\n"
            "Now answer the following question: \n\n"
            f"Start phrase: {row['startphrase']}\n"
            f"Ending 0: {row['ending1']}\n"
            f"Ending 1: {row['ending2']}\n"
            "Answer: \n"
        )

    def chain_of_thought_original_language(self, language: str, row) -> str:
        return (
            f"In this task, you are given a start phrase indicating a figurative expression in {language} culture. "
            "Please select 0 if the start phrase conveys the meaning of ending 0, and 1 if it conveys the meaning of ending 1.\n"
            "Below is an example showing you how to do the task: \n\n"
            f"{self.CHAIN_OF_THOUGHT_ORIGIANL_LANGUAGE_EXAMPLES[language]}\n\n"
            "Now answer the following question: \n\n"
            f"Start phrase: {row['startphrase']}\n"
            f"Ending 0: {row['ending1']}\n"
            f"Ending 1: {row['ending2']}\n"
            "Answer: \n"
        )

    def chain_of_thought_english_translated(self, language: str, row) -> str:
        return (
            f"In this task, you are given a start phrase indicating a figurative expression in {language} culture. "
            "Please select 0 if the start phrase conveys the meaning of ending 0, and 1 if it conveys the meaning of ending 1.\n"
            "Below is an example showing you how to do the task: \n\n"
            f"{self.CHAIN_OF_THOUGHT_ENGLISH_EXAMPLES[language]}\n\n"
            "Now answer the following question: \n\n"
            f"Start phrase: {row['startphrase']}\n"
            f"Ending 0: {row['ending1']}\n"
            f"Ending 1: {row['ending2']}\n"
            "Answer: \n"
        )

    def self_translation(self, language: str, row) -> str:
        return (
            f"In this task, you are given a starting phrase indicating a figurative expression in {language} culture. "
            "Please first translate the start phrase, ending 0, and ending 1 into English. "
            "Then, select 0 if the translated start phrase conveys the meaning of the translated Ending 0, and 1 if it conveys the meaning of the translated Ending 1. \n"
            "Below is an example showing you how to do the task: \n\n"
            f"{self.SELF_TRANSLATION_EXAMPLES[language]}\n\n"
            "Now answer the following question: \n\n"
            f"Start phrase: {row['startphrase']}\n"
            f"Ending 0: {row['ending1']}\n"
            f"Ending 1: {row['ending2']}\n"
            "Translated into English: \n"
            "Start phrase: \n"
            "Ending 0: \n"
            "Ending 1: \n"
            "Answer: \n"
        )

    ONE_SHOT_ORIGINAL_LANGUAGE_EXAMPLES = {
        "English": """Start phrase: Money is a helpful stranger.
Ending 0: Money is good.
Ending 1: Money is bad.
Answer: 0
    """,
        "Hindi": f"""Start phrase: कालिदास भारत के शेख्चिली हैं।.
Ending 0: कालिदास मुर्ख हैं।.
Ending 1: कालिदास बुद्धिमान हैं।.
Answer: 1
    """,
        "Indonesian": f"""Start phrase: Siswa SD itu membawa tas layaknya orang yang mau kabur dari rumah.
Ending 0: Tasnya besar.
Ending 1: Tasnya kecil.
Answer: 0
    """,
        "Swahili": """Start phrase: Maneno yake ni kama kinanda.
Ending 0: Maneno yako yanaumiza.
Ending 1: Maneno yake yanafariji.
Answer: 1
    """,
        "Javanese": """Start phrase: Lungguh ning kursi iku rasane kaya watu
Ending 0: Lungguh ning kursi iku rasane empuk
Ending 1: Lungguh ning kursi iku rasane atos
Answer: 1
    """,
        "Kannada": """Start phrase: ನನ್ನ ಮುದ್ದಿನ ಬೆಕ್ಕು ನರಿಯಂತೆ ಪ್ರಾಮಾಣಿಕವಾಗಿದೆ
Ending 0: ನನ್ನ ಮುದ್ದಿನ ಬೆಕ್ಕು ಪ್ರಾಮಾಣಿಕವಾಗಿದೆ
Ending 1: ನನ್ನ ಮುದ್ದಿನ ಬೆಕ್ಕು ಪ್ರಾಮಾಣಿಕವಾಗಿಲ್ಲ
Answer: 1
    """,
        "Sundanese": """Start phrase: Kadang jelema teh bisa kandel kulit bengeut
Ending 0: Kadang jelema teh bisa teu boga kaera
Ending 1: Kadang jelema teh bisa eraan.
Answer: 0
    """,
        "Persian": """Start phrase: او مثل قاصدکی در باد است.
Ending 0: او بسیار آزاد و بی‌قید است.
Ending 1: او بسیار محدود و مقید است.
Answer: 0
    """,
    }

    ONE_SHOT_ENGLISH_EXAMPLE = {
        "English": """Start phrase: Money is a helpful stranger.
Ending 0: Money is good.
Ending 1: Money is bad.
Answer: 0
    """,
        "Hindi": f"""Start phrase: The burger tastes like the hands of a washerman.
Ending 0: Burger is very tasty.
Ending 1: Burger is very tasteless.
Answer: 1
    """,
        "Indonesian": f"""Start phrase: The news came like a hurricane.
Ending 0: The news came as a shock.
Ending 1: The news came quietly.
Answer: 0
    """,
        "Swahili": """Start phrase: He felt his chest freeze like ice.
Ending 0: His heart rate was too fast.
Ending 1: His heartbeat slowed.
Answer: 1
    """,
        "Javanese": """Start phrase: Sitting on the chair felt like a stone.
Ending 0: Sitting in the chair feels soft.
Ending 1: Sitting on the chair is hard.
Answer: 1
    """,
        "Kannada": """Start phrase: My pet cat is as honest as a fox.
Ending 0: My pet cat is honest.
Ending 1: My pet cat is not honest.
Answer: 1
    """,
        "Sundanese": """Start phrase: Sometimes people can have thick skin.
Ending 0: Sometimes people can't have a sense of humor.
Ending 1: Sometimes people can make mistakes..
Answer: 0
    """,
        "Persian": """Start phrase: He is like a dandelion in the wind.
Ending 0: He is very free and unrestricted.
Ending 1: He is very limited.
Answer: 0
    """,
    }

    CHAIN_OF_THOUGHT_ORIGIANL_LANGUAGE_EXAMPLES = {
        "English": """Start phrase: Money is a helpful stranger.
Ending 0: Money is good.
Ending 1: Money is bad.
Answer: In English culture, the expression Money is a helpful stranger" is used to convey that money can be beneficial or advantageous, akin to the assistance one might receive from a helpful stranger. In this context, "helpful stranger" implies someone who offers assistance or support when needed. Therefore, the expression suggests that money can be useful or advantageous, indicating a positive connotation. Hence, the answer is 0.
    """,
        "Hindi": f"""Start phrase: बर्गर में धोबी के हाथो सा स्वाद है।
Ending 0: बर्गर बहुत स्वादिष्ट है।
Ending 1: बर्गर बहुत बेस्वाद है।
Answer: इस वाक्यांश में, "बर्गर में धोबी के हाथो सा स्वाद है" वाक्य द्वारा बताया जा रहा है कि बर्गर का स्वाद अच्छा नहीं होता है, और यह वाक्य बेस्वादता की भावना को दर्शाता है। धोबी के हाथों का मतलब होता है कि इस बर्गर का स्वाद कच्चा और अच्छा नहीं होता है, जैसा कि हम धोबी के द्वारा धोए हुए कपड़े के स्वाद को सोच सकते हैं। इस प्रकार, यह वाक्य व्यक्ति के मन में नकारात्मक अनुभूति को प्रकट करता है, बर्गर के स्वाद को बेस्वाद घोषित करता है। इसलिए, उत्तर 1 है।
    """,
        "Indonesian": f"""Start phrase: Berita itu datang seperti angin badai.
Ending 0: Berita itu datang mengangetkan.
Ending 1: Berita itu datang dengan tenang.
Answer: Dalam budaya Indonesia, ungkapan "Berita itu datang seperti angin badai" digunakan untuk menyampaikan bahwa berita tersebut datang dengan kejutan yang besar, menggambarkan situasi yang mendebarkan dan mengganggu. "Angin badai" mengimplikasikan datangnya sesuatu yang bersifat hebat, tidak terduga, dan dapat mengganggu ketenangan. Oleh karena itu, jawabannya adalah 0.
    """,
        "Swahili": """Start phrase: Alihisi kifua chake kimeganda kama barafu
Ending 0: Mapigo yake ya moyo yalienda kwa kasi mno
Ending 1: Mapingo yake ya moyo yalienda taratibu
Answer: Katika utamaduni wa Kiswahili, usemi "Alihisi kifua chake kimeganda kama barafu" hutumiwa kuonyesha kwamba mtu alihisi hofu, wasiwasi au kutokuwa na uhakika. "Kifua kimeganda kama barafu" inamaanisha kwamba hisia zake zilikuwa zimekwama au zilikuwa zimefriji kama barafu. Kwa hiyo, usemi huo unaashiria hali ya kukosa uchangamfu au shauku. Katika muktadha huu, "Mapigo yake ya moyo yalienda taratibu" inaonyesha kwamba mapigo ya moyo wa mtu yalikuwa yanakwenda polepole na kwa utulivu. Hii inaonyesha hali ya kutokuwa na haraka au msisimko. Kwa hiyo, jibu ni 1.
    """,
        "Javanese": """Start phrase: Lungguh ning kursi iku rasane kaya watu
Ending 0: Lungguh ning kursi iku rasane empuk
Ending 1: Lungguh ning kursi iku rasane atos
Answer: Ing budaya Jawa, ungkapan "Lungguh ning kursi iku rasane kaya watu" nggambarake yen lungguhan ing kursi kuwi ora nyaman, atos, lan angel, kaya lungguh ing watu. Piwulang iki nuduhake yen kursi iki ora empuk lan ora nyenengake kanggo di lungguhi. Mula, ungkapan iki nduweni konotasi negatif bab kepenakane kursi, lan tegese mirip karo "Lungguh ning kursi iku rasane atos". Mula, jawabané yaiku 1.
    """,
        "Kannada": """Start phrase: ನನ್ನ ಮುದ್ದಿನ ಬೆಕ್ಕು ನರಿಯಂತೆ ಪ್ರಾಮಾಣಿಕವಾಗಿದೆ
Ending 0: ನನ್ನ ಮುದ್ದಿನ ಬೆಕ್ಕು ಪ್ರಾಮಾಣಿಕವಾಗಿದೆ
Ending 1: ನನ್ನ ಮುದ್ದಿನ ಬೆಕ್ಕು ಪ್ರಾಮಾಣಿಕವಾಗಿಲ್ಲ
Answer: ಕನ್ನಡ ಸಂಸ್ಕೃತಿಯಲ್ಲಿ "ನನ್ನ ಮುದ್ದಿನ ಬೆಕ್ಕು ನರಿಯಂತೆ ಪ್ರಾಮಾಣಿಕವಾಗಿದೆ" ಎಂಬ ವಾಕ್ಯದಲ್ಲಿ ಬಳಸುವ ನರಿಯ ದೃಷ್ಟಾಂತವು ನರಿಯು ಅಪರಾಧಿ ಮತ್ತು ಮೋಸದ ಸಂಕೇತವಾಗಿದೆ. ಇಲ್ಲಿ ನರಿಯಂತೆ ಎಂದರೆ ಮೋಸದ ಮನಸ್ಥಿತಿಯನ್ನು ಬಿಂಬಿಸುತ್ತವೆ. ಆದ್ದರಿಂದ, "ನರಿಯಂತೆ ಪ್ರಾಮಾಣಿಕವಾಗಿದೆ" ಎಂಬ ವಾಕ್ಯವು ವ್ಯಂಗ್ಯಪ್ರಯೋಗವಾಗಿದೆ ಮತ್ತು ನಿಜವಾಗಿ ಪ್ರಾಮಾಣಿಕವಲ್ಲ ಎಂದು ಹೇಳಲು ಪ್ರಯತ್ನಿಸುತ್ತವೆ. ಹಾಗಾಗಿ, ಉತ್ತರ 1.
    """,
        "Sundanese": """Start phrase: Kadang jelema teh bisa kandel kulit bengeut
Ending 0: Kadang jelema teh bisa teu boga kaera
Ending 1: Kadang jelema teh bisa eraan.
Answer: Dina budaya Sunda, ungkapan "Kadang jelema teh bisa kandel kulit bengeut" dipaké pikeun ngajelaskeun yén aya jalma anu teu boga kaera atawa teu ngarasa isin. Istilah "kandel kulit bengeut" hartina éta jalma bisa tahan narima kritik atawa teu gampang isin, anu nuduhkeun yén jalma éta teu boga kaera. Ku kituna, ungkapan éta ngabogaan konotasi yén jalma éta teu boga kaera, anu nuduhkeun jawabanana nyaeta 0.
    """,
        "Persian": """Start phrase: او مثل قاصدکی در باد است.
Ending 0: او بسیار آزاد و بی‌قید است.
Ending 1: او بسیار محدود و مقید است.
Answer: در فرهنگ فارسی، عبارت "او مثل قاصدکی در باد است" به معنای آزادی و بی‌قیدی است. بنابراین، پایان 0 (او بسیار آزاد و بی‌قید است) با این توصیف هماهنگ است. این تصویر به فردی اشاره دارد که بدون هیچ گونه محدودیتی حرکت می‌کند و به نظر نمی‌رسد که تحت تأثیر محدودیت‌های خارجی باشد.
    """,
    }

    CHAIN_OF_THOUGHT_ENGLISH_EXAMPLES = {
        "English": """Start phrase: Money is a helpful stranger.
Ending 0: Money is good.
Ending 1: Money is bad.
Answer: In English culture, the expression "Money is a helpful stranger" is used to convey that money can be beneficial or advantageous, akin to the assistance one might receive from a helpful stranger. In this context, "helpful stranger" implies someone who offers assistance or support when needed. Therefore, the expression suggests that money can be useful or advantageous, indicating a positive connotation. Hence, the answer is 0.
    """,
        "Hindi": f"""Start phrase: The burger tastes like the hands of a washerman.
Ending 0: Burger is very tasty.
Ending 1: Burger is very tasteless.
Answer: In Hindi culture, the expression "tastes like the hands of a washerman" is used to convey that something lacks flavor or taste, akin to how the hands of a washerman might not retain any taste or flavor due to constant exposure to water and detergent. Therefore, when describing a burger as tasting like the hands of a washerman, it implies that the burger is tasteless or bland. Hence, the answer is 1.
    """,
        "Indonesian": f"""Start phrase: The news came like a hurricane.
Ending 0: The news came as a shock.
Ending 1: The news came quietly.
Answer: In Indonesian culture, the expression "came like a hurricane" implies that the news arrived suddenly and with great force or impact, similar to how a hurricane sweeps through with powerful winds and intensity. Therefore, when describing the news as coming like a hurricane, it suggests that it was shocking or surprising, akin to the impact of a natural disaster. Hence, the answer is 0.
    """,
        "Swahili": """Start phrase: He felt his chest freeze like ice.
Ending 0: His heart rate was too fast.
Ending 1: His heartbeat slowed.
Answer: In Swahili culture, the expression "felt his chest freeze like ice" typically signifies a moment of fear or intense emotional coldness, suggesting a sudden and chilling sensation in the chest area, akin to the feeling of ice. Therefore, when someone feels their chest freeze like ice, it implies a decrease in heart rate due to shock or fear, leading to a slowed heartbeat. Hence, the answer is 1.
    """,
        "Javanese": """Start phrase: Sitting on the chair felt like a stone.
Ending 0: Sitting in the chair feels soft.
Ending 1: Sitting on the chair is hard.
Answer: In Javanese culture, the expression "Sitting on the chair felt like a stone" conveys the idea that the chair is uncomfortable and hard. The comparison to a stone emphasizes the chair's lack of softness and comfort. Therefore, this expression indicates that sitting in the chair is difficult and uncomfortable, similar to sitting on a hard, unyielding surface like a stone. Hence, the answer is 1.
    """,
        "Kannada": """Start phrase: My pet cat is as honest as a fox.
Ending 0: My pet cat is honest.
Ending 1: My pet cat is not honest.
Answer: In Kannada culture, the expression "as honest as a fox" is used sarcastically to imply dishonesty, as foxes are traditionally seen as cunning and deceptive animals. By comparing the pet cat to a fox, the phrase suggests that the cat is not honest. Therefore, the answer is 1.
    """,
        "Sundanese": """Start phrase: Sometimes people can have thick skin.
Ending 0: Sometimes people can't have a sense of humor.
Ending 1: Sometimes people can make mistakes..
Answer: In Sundanese culture, the expression "having thick skin" means being able to withstand criticism, insults, or negative comments without being easily offended or upset. This trait often implies that the person is resilient and not overly sensitive. Therefore, the phrase suggests that people with thick skin might not take things personally, including jokes or criticisms, indicating they might lack sensitivity or a sense of humor about certain things. Hence, the answer is 0.
    """,
        "Persian": """Start phrase: He is like a dandelion in the wind.
Ending 0: He is very free and unrestricted.
Ending 1: He is very limited.
Answer: In Persian culture, the expression "He is like a dandelion in the wind" means freedom and unrestrainedness. Therefore, the ending 0 (he is very free and unrestrained) fits this description. This image refers to a person who moves without any restrictions and does not seem to be affected by external restrictions.
    """,
    }

    SELF_TRANSLATION_EXAMPLES = {
        "English": """
    Start phrase: Money is a helpful stranger.
    Ending 0: Money is good.
    Ending 1: Money is bad.

    The answer:
      The English translation is:
      Start phrase: Money is a helpful stranger.
      Ending 0: Money is good.
      Ending 1: Money is bad.

      The final answer is: 0
    """,
        "Hindi": f"""
    Start phrase: कालिदास भारत के शेख्चिली हैं।.
    Ending 0: कालिदास मुर्ख हैं।.
    Ending 1: कालिदास बुद्धिमान हैं।.

    The answer:
      The English translation is:
      Start phrase: Kalidas is the Shakespeare of India.
      Ending 0: Kalidas is a fool.
      Ending 1: Kalidas is intelligent.

      The final answer is: 1
    """,
        "Indonesian": f"""
    Start phrase: Siswa SD itu membawa tas layaknya orang yang mau kabur dari rumah.
    Ending 0: Tasnya besar.
    Ending 1: Tasnya kecil.

    The answer:
      The English translation is:
      Start phrase: The elementary school student was carrying a bag like someone who wanted to run away from home.
      Ending 0: The bag is big.
      Ending 1: The bag is small.


      The final answer is: 0
    """,
        "Javanese": f"""
    Start phrase: Nyawang esemmu sing rupane kaya ngemut glali.
    Ending 0: Nyawang esemmu sing manis.
    Ending 1: Nyawang esemmu sing pahit.

    The answer:
      The English translation is:
      Start phrase: Look at your smile that looks like you're looking at it.
      Ending 0: Look at your sweet smile.
      Ending 1: Look at your bitter smile.

      The final answer is: 0
    """,
        "Kannada": f"""
    Start phrase: ಅವನು ದುರ್ಬಲನಾಗಿದ್ದಾನೆ,ಅವನು ದುರ್ಬಲನಾಗಿಲ್ಲ.
    Ending 0: ಅವನು ದುರ್ಬಲನಾಗಿದ್ದಾನೆ.
    Ending 1: ಅವನು ದುರ್ಬಲನಾಗಿಲ್ಲ.

    The answer:
      The English translation is:
      Start phrase: He is as weak as a youth.
      Ending 0: He is weak.
      Ending 1: He is not weak.

      The final answer is: 1
    """,
        "Sundanese": """
    Start phrase: si Udin jadi jalma teh meni buntut kasiran.
    Ending 0: si Udin jadi jalma teh meni koret, pedit.
    Ending 1: si Udin jadi jalma teh meni reseup babagi.

    The answer:
      The English translation is:
      Start phrase: si Udin is a person with a tail.
      Ending 0: si Udin is a lazy person.
      Ending 1: Udin is a person who likes to share.

      The final answer is: 0
    """,
        "Swahili": """
    Start phrase: Maneno yake ni kama kinanda.
    Ending 0: Maneno yako yanaumiza.
    Ending 1: Maneno yake yanafariji.

    The answer:
      The English translation is:
      Start phrase: His words are like a piano.
      Ending 0: Your words hurt.
      Ending 1: His words are comforting.

      The final answer is: 1
    """,
        "Persian": """
    Start phrase: او مثل قاصدکی در باد است.
    Ending 0: او بسیار آزاد و بی‌قید است.
    Ending 1: او بسیار محدود و مقید است.

    The answer:
        The English translation is:
        Start phrase: He is like a dandelion in the wind.
        Ending 0: He is very free and unrestricted.
        Ending 1: He is very limited.

        The final answer is: 0
    """,
    }
