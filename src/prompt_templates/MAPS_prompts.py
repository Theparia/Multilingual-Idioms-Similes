class MapsPrompts:
    def zero_shot(self, language: str, row) -> str:
        return (
            f"Question: How would one interpret this proverb in {language} culture, given the context? "
            f"Please choose between A and B.\n"
            f"Proverb: {row['proverb']}\n"
            f"Context: {row['conversation']}\n"
            f"Choices: A: {row['answer1']} B: {row['answer2']}\n"
            "Answer: \n"
        )

    def one_shot_original_language(self, language: str, row) -> str:
        return (
            f"Question: How would one interpret this proverb in {language} culture, given the context? "
            "Please choose between A and B.\n"
            f"{self.ONE_SHOT_ORIGINAL_LANGUAGE_EXAMPLES[language]}\n\n"
            "Question: How would one interpret this proverb in {language} culture, given the context? "
            "Please choose between A and B.\n"
            f"Proverb: {row['proverb']}\n"
            f"Context: {row['conversation']}\n"
            f"Choices: A: {row['answer1']} B: {row['answer2']}\n"
            "Answer: \n"
        )

    def one_shot_english_translated(self, language: str, row) -> str:
        return (
            f"Question: How would one interpret this proverb in {language} culture, given the context? "
            "Please choose between A and B.\n"
            f"{self.ONE_SHOT_ENGLISH_EXAMPLE}\n\n"
            f"Question: How would one interpret this proverb in {language} culture, given the context? "
            f"Proverb: {row['proverb']}\n"
            f"Context: {row['conversation']}\n"
            f"Choices: A: {row['answer1']} B: {row['answer2']}\n"
            "Answer: \n"
        )

    def chain_of_thought_original_language(self, language: str, row) -> str:
        return (
            f"Question: How would one interpret this proverb in {language} culture, given the context? "
            "Please first think about the proverb's meaning, "
            "then write an explanation of the proverb's meaning, and finally choose between A and B.\n"
            f"{self.CHAIN_OF_THOUGHT_ORIGIANL_LANGUAGE_EXAMPLES[language]}\n\n"
            f"Question: How would one interpret this proverb in {language} culture, given the context? "
            "Please first think about the proverb's meaning, "
            f"then write an explanation of the proverb's meaning, and finally choose between A and B.\n"
            f"Proverb: {row['proverb']}\n"
            f"Context: {row['conversation']}\n"
            f"Choices: A: {row['answer1']} B: {row['answer2']}\n"
            f"Explanation:\n"
            f"Answer:\n"
        )

    def chain_of_thought_english_translated(self, language: str, row) -> str:
        return (
            f"Question: How would one interpret this proverb in {language} culture, given the context? "
            "Please first think about the proverb's meaning, "
            "then write an explanation of the proverb's meaning, and finally choose between A and B.\n"
            f"{self.CHAIN_OF_THOUGHT_ENGLISH_EXAMPLES[language]}\n\n"
            f"Question: How would one interpret this proverb in {language} culture, given the context? "
            "Please first think about the proverb's meaning, "
            f"then write an explanation of the proverb's meaning, and finally choose between A and B.\n"
            f"Proverb: {row['proverb']}\n"
            f"Context: {row['conversation']}\n"
            f"Choices: A: {row['answer1']} B: {row['answer2']}\n"
            f"Explanation:\n"
            f"Answer:\n"
        )

    def self_translation(self, language: str, row) -> str:
        return (
            f"Question: How would one interpret this proverb in {language} culture, given the context? "
            "Please first translate the Proverb, Context, and Choices into English. Then, choose between A and B."
            f"{self.SELF_TRANSLATION_EXAMPLES[language]}\n\n"
            f"Question: How would one interpret this proverb in {language} culture, given the context? "
            "Please first translate the Proverb, Context, and Choices into English. Then, choose between A and B."
            f"Proverb: {row['proverb']}\n"
            f"Context: {row['conversation']}\n"
            f"Choices: A: {row['answer1']} B: {row['answer2']}\n"
            f"The English translation is:\n"
            f"Final answer:\n"
        )

    ONE_SHOT_ORIGINAL_LANGUAGE_EXAMPLES = {
        "English": (
            "Proverb: half a loaf is better than none\n"
            "Context: Person 1: 'I didn't get the promotion I wanted, but at least I got a raise.'\n"
            "Person 2: 'Of course, half a loaf is better than none.'\n"
            "Choices: A: A raise is worth nothing. B: A raise is better than nothing.\n"
            "Answer: B"
        ),
        "Indonesian": (
            "Proverb: Seperti kucing lepas senja\n"
            "Context: Orang 1: 'Apa kabar teman lama kita, Andi?' Orang 2: 'Dia pergi ke luar, seperti kucing lepas senja ya'.\n"
            "Choices: A: Andi telah pergi dan sepertinya tidak akan kembali. B: Andi telah pergi dan akan segera kembali.\n"
            "Answer: A"
        ),
        "Chinese": (
            "Proverb: 民以食为天\n"
            "Context: A: '你最近忙什么呢？' B: '我在学做菜。' A: '你那么忙，还有时间做菜呀！' B: '民以食为天嘛。'\n"
            "Choices: A: B认为吃饭是人生中无足轻重的事情。 B: B认为吃饭是人生中重要的事情。\n"
            "Answer: B"
        ),
        "Bengali": (
            "Proverb: যদি আমড়াতলায় আম পাই তবে আমতলায় কেন যাই\n"
            "Context: ব্যক্তি ১: 'আমি জঙ্গলের ভেতর দিয়ে যাবার একটা সহজ রাস্তা জানি।' ব্যক্তি ২: 'আমি শুধুমাত্র সাধারণ পথটি চিনি। আমরা কি সহজ রাস্তা টি নেব?' ব্যক্তি ১: 'যদি আমড়াতলায় আম পাই তবে আমতলায় কেন যাই।'\n"
            "Choices: A: তাদের শর্টকাট নেওয়া উচিত।  B: তাদের শর্টকাট নেওয়া উচিত নয়।\n"
            "Answer: A"
        ),
        "Russian": (
            "Proverb: eдешь нa день, хлeба бери на недeлю\n"
            "Context: Человек 1: 'Я готовлюсь к конкурсу пианистов, который состоится на следующей неделе.' Я занимаюсь по 5 часов в неделю, как вы думаете, этого достаточно?' Человек 2: 'Едешь нa день, хлeба бери на недeлю.'\n"
            "Choices: A: Человеку 1 следует больше практиковаться, чтобы быть уверенным, что он полностью готов. B: Человек 1 достаточно практиковался.\n"
            "Answer: A"
        ),
        "German": (
            "Proverb: die hoffnung stirbt zuletzt\n"
            "Context: Person 1: 'Denkst du, dass wir es schaffen werden?' Person 2: 'Ich weiß es nicht, aber die Hoffnung stirbt zuletzt.'\n"
            "Choices: A: Person 2 hofft, dass sie es schaffen werden. B: Person 2 hat keine Hoffnung, dass sie es schaffen werden.\n"
            "Answer: A"
        ),
        "Persian": (
            "Proverb: ماه پشت ابر نمی‌ماند\n"
            "Context: شخص ۱: 'مدیرمون ماه‌هاست که مخفیانه قراردادها رو دستکاری می‌کنه. فکر می‌کنی کسی می‌فهمه؟' شخص ۲: 'نگران نباش، ماه پشت ابر نمی‌ماند.'\n"
            "Choices: A: شخص ۲ معتقد است که حقیقت بالاخره آشکار خواهد شد. B: شخص ۲ معتقد است که حقیقت هرگز آشکار نخواهد شد.\n"
            "Answer: A"
        ),
    }

    ONE_SHOT_ENGLISH_EXAMPLE = (
        "Proverb: half a loaf is better than none\n"
        "Context: Person 1: 'I didn't get the promotion I wanted, but at least I got a raise.'\n"
        "Person 2: 'Of course, half a loaf is better than none.'\n"
        "Choices: A: A raise is worth nothing. B: A raise is better than nothing.\n"
        "Answer: B"
    )

    CHAIN_OF_THOUGHT_ORIGIANL_LANGUAGE_EXAMPLES = {
        "English": (
            "Proverb: half a loaf is better than none\n"
            "Context: Person 1: 'I didn't get the promotion I wanted, but at least I got a raise.'\n"
            "Person 2: 'Of course, half a loaf is better than none.'\n"
            "Choices: A: A raise is worth nothing. B: A raise is better than nothing.\n"
            "Explanation: Something is better than nothing: some reward, achievement, result, etc.\n"
            "Answer: B"
        ),
        "Indonesian": (
            "Proverb: Seperti kucing lepas senja\n"
            "Context: Orang 1: 'Apa kabar teman lama kita, Andi?' Orang 2: 'Dia pergi ke luar, seperti kucing lepas senja ya'.\n"
            "Choices: A: Andi telah pergi dan sepertinya tidak akan kembali. B: Andi telah pergi dan akan segera kembali.\n"
            "Explanation: orang yang kalau sudah pergi tidak akan kembali lagi.\n"
            "Answer: A"
        ),
        "Chinese": (
            "Proverb: 民以食为天\n"
            "Context: A: '你最近忙什么呢？' B: '我在学做菜。' A: '你那么忙，还有时间做菜呀！' B: '民以食为天嘛。'\n"
            "Choices: A: B认为吃饭是人生中无足轻重的事情。 B: B认为吃饭是人生中重要的事情。\n"
            "Explanation: 人们认为食物是他们的主要需求。\n"
            "Answer: B"
        ),
        "Bengali": (
            "Proverb: যদি আমড়াতলায় আম পাই তবে আমতলায় কেন যাই\n"
            "Context: ব্যক্তি ১: 'আমি জঙ্গলের ভেতর দিয়ে যাবার একটা সহজ রাস্তা জানি।' ব্যক্তি ২: 'আমি শুধুমাত্র সাধারণ পথটি চিনি। আমরা কি সহজ রাস্তা টি নেব?' ব্যক্তি ১: 'যদি আমড়াতলায় আম পাই তবে আমতলায় কেন যাই।'\n"
            "Choices: A: তাদের শর্টকাট নেওয়া উচিত।  B: তাদের শর্টকাট নেওয়া উচিত নয়।\n"
            "Explanation: সহজে কোন কাজ উদ্ধার হ'লে অনর্থক কষ্টকর পথ অবলম্বন করার কোন অর্থ হয় না।\n"
            "Answer: A"
        ),
        "Russian": (
            "Proverb: eдешь нa день, хлeба бери на недeлю\n"
            "Context: Человек 1: 'Я готовлюсь к конкурсу пианистов, который состоится на следующей неделе.' Я занимаюсь по 5 часов в неделю, как вы думаете, этого достаточно?' Человек 2: 'Едешь нa день, хлeба бери на недeлю.'\n"
            "Choices: A: Человеку 1 следует больше практиковаться, чтобы быть уверенным, что он полностью готов. B: Человек 1 достаточно практиковался.\n"
            "Explanation: Английский эквивалент: Всегда будь готов (или всегда бери с собой больше, чем тебе нужно); Лучше иметь и не нуждаться, чем нуждаться и не иметь.\n"
            "Answer: A"
        ),
        "German": (
            "Proverb: die hoffnung stirbt zuletzt\n"
            "Context: Person 1: 'Denkst du, dass wir es schaffen werden?' Person 2: 'Ich weiß es nicht, aber die Hoffnung stirbt zuletzt.'\n"
            "Choices: A: Person 2 hofft, dass sie es schaffen werden. B: Person 2 hat keine Hoffnung, dass sie es schaffen werden.\n"
            "Explanation: die Hoffnung sollte das letzte sein, was man aufgibt.\n"
            "Answer: A"
        ),
        "Persian": (
            "Proverb: ماهی را هر وقت از آب بگیری تازه است\n"
            "Context: شخص ۱: 'فکر می‌کنم برای شروع یادگیری زبان جدید خیلی دیر شده.' شخص ۲: 'اصلاً اینطور نیست، ماهی را هر وقت از آب بگیری تازه است.'\n"
            "Choices: A: شخص ۲ معتقد است که همیشه برای شروع یک کار دیر است. B: شخص ۲ معتقد است که هیچ وقت برای شروع یک کار دیر نیست.\n"
            "Explanation: هیچ وقت، برای انجام کار دیر نیست و هر لحظه میتوان اقدام کرد، کار را هر زمانی شروع کنید آن چنان است که پیش از آن شروع کرده‌اید. \n"
            "Answer: B"
        ),
    }

    CHAIN_OF_THOUGHT_ENGLISH_EXAMPLES = {
        "English": (
            "Proverb: half a loaf is better than none\n"
            "Context: Person 1: 'I didn't get the promotion I wanted, but at least I got a raise.' "
            "Person 2: 'Of course, half a loaf is better than none.'\n"
            "Choices: A: A raise is worth nothing. B: A raise is better than nothing.\n"
            "Explanation: Something is better than nothing: some reward, achievement, result, etc.\n"
            "Answer: B"
        ),
        "Indonesian": (
            "Proverb: Like your back misses the moon\n"
            "Context: Person 1: 'How are you, have you achieved your dream of becoming a famous singer?' "
            "Person 2: 'Not yet, it seems like that dream is too high for me to achieve.' "
            "Person 1: 'Yes, sometimes we want something that is difficult to achieve.' "
            "Person 2: 'That's right, it's like your back misses the moon.' "
            "Choices: A: Person 2 agrees that the dream is too difficult. B: Person 2 disagrees that the dream is too difficult.\n"
            "Explanation: Wanting something that is difficult to achieve.\n"
            "Answer: A"
        ),
        "Chinese": (
            "Proverb: Water can carry a boat, but it can also overturn it\n"
            "Context: A: 'Do you think I should protest to my boss?' "
            "B: 'I think it might be risky.' "
            "A: 'I think water can carry a boat, but it can also capsize it.' "
            "Choices: A: A thinks that it is time to protest, and the result may be good. "
            "B: A feels that it is wrong to protest, and the result may be bad. "
            "Explanation: If used correctly, this can be beneficial.\n"
            "Answer: A"
        ),
        "Bengali": (
            "Proverb: Chucking doesn't make gold\n"
            "Context: Person 1: 'Have you heard about the new restaurant opening?' "
            "Person 2: 'Yes! The new restaurant is very elegant and bright.' "
            "Person 1: 'Chucking doesn't make gold.'\n"
            "Choices: A: The new restaurant is not good. B: The new restaurant is good.\n"
            "Explanation: Fake or genuine, it cannot be understood by appearance; The outward form of a thing does not reveal its quality; Everything cannot be judged by external appearances.\n"
            "Answer: A"
        ),
        "Russian": (
            "Proverb: God does not give a horn to a carnivorous cow\n"
            "Context: Person 1: 'I discovered that someone hacked my email account and tried to access my personal information.' "
            "Person 2: 'How did they get access? I thought I told you to enable two-factor authentication.' "
            "Person 1: 'I was too lazy to turn it on.' "
            "Person 2: 'God does not give a horn to a carnivorous cow.'\n"
            "Choices: A: Person 2 probably thinks that a random hacker is to blame for Person 1's misfortune. "
            "B: Person 2 probably believes that Person 1 is to blame for his own misfortunes.\n"
            "Explanation: If a person is his own enemy, then God will not help him. Usually used in response to complaints or excuses from a person who is to blame for his own misfortunes.\n"
            "Answer: B"
        ),
        "German": (
            "Proverb: When you talk about the devil, he comes running\n"
            "Context: Person 1: 'Have you heard from the new colleague yet?' "
            "Person 2: 'No, who is that?'\ "
            "Person 1: 'Oh, when you talk about the devil, he comes running.'\n"
            "Choices: A: Person 2 is currently seeing their new colleague. B: Person 2 has not seen the new colleague.\n"
            "Explanation: Colloquial: Joking description for the situation in which one is talking about a certain person and that person then appears to the speaker at exactly that moment.\n"
            "Answer: A"
        ),
        "Persian": (
            "Proverb: The fish is fresh whenever you take it out of the water. \n"
            "Context: Person 1: 'I think it is too late to start learning a new language.' Person 2: 'Not at all, the fish is fresh whenever you take it out of the water.'\n"
            "Choices: A: Person 2 believes that it is always too late to start something. B: Person 2 believes that it is never too late to start something.\n"
            "Explanation: It is never too late to do the work and you can take action at any moment, start the work at any time as you have started before. \n"
            "Answer: B"
        ),
    }

    SELF_TRANSLATION_EXAMPLES = {
        "Indonesian": f"""Proverb: Bagai pungguk merindukan bulan
Context: Orang 1: Apa kabar, kamu sudah mencapai impianmu untuk menjadi seorang penyanyi terkenal? Orang 2: Belum, sepertinya impian itu terlalu tinggi untuk saya capai. Orang 1: Ya, memang terkadang kita menginginkan sesuatu yang sulit untuk digapai. Orang 2: Betul sekali, bagai pungguk merindukan bulan.
Choices: A: Orang 2 setuju bahwa mimpi itu terlalu sulit. B: Orang 2 tidak setuju bahwa mimpi itu terlalu sulit.
The English translation is:
Proverb: Like your back misses the moon
Context: Person 1: How are you, have you achieved your dream of becoming a famous singer? Person 2: Not yet, it seems like that dream is too high for me to achieve. Person 1: Yes, sometimes we want something that is difficult to achieve. Person 2: That's right, it's like your back misses the moon.
Choices: A: Person 2 agrees that the dream is too difficult. B: Person 2 disagrees that the dream is too difficult.
Final answer: A
""",
        "Chinese": f"""Proverb: 水能载舟，亦能覆舟
Context: A: 你觉得我应该跟老板抗议吗？B: 我觉得可能会有风险。A: 我却觉得水能载舟，亦能覆舟。
Choices: A: A觉得因该去抗议，结果可能会很好。 B: A觉得不因该去抗议，结果可能会很差。
The English translation is:
Proverb: Water can carry a boat, but it can also overturn it
Context: A: Do you think I should protest to my boss? B: I think it might be risky. A: I think water can carry a boat, but it can also capsize it.
Choices: A: A thinks that it is time to protest, and the result may be good. B: A feels that it is wrong to protest, and the result may be bad.
Final answer: A
""",
        "Bengali": f"""Proverb: চক চক করলেই সোনা হয় না
Context: ব্যক্তি ১: তুমি কি নতুন রেস্তোরা খোলা সম্পর্কে শুনেছ? ব্যক্তি ২: হ্যাঁ! নতুন রেস্তোরাঁ খুব সুশোভিত এবং ঝকমকে। ব্যক্তি ১: চক চক করলেই সোনা হয় না।
Choices: A: নতুন রেস্তোঁরাটি ভাল নয়।  B: নতুন রেস্তোঁরা ভাল।
The English translation is:
Proverb: Chucking doesn't make gold
Context: Person 1: Have you heard about the new restaurant opening? Person 2: Yes! The new restaurant is very elegant and bright. Person 1: Chucking doesn't make gold.
Choices: A: The new restaurant is not good.  B: The new restaurant is good.
Final answer: A
""",
        "Russian": f"""Proverb: Бодливой корове Бог рог не даёт
Context: Человек 1: Я обнаружил, что кто -то взломал мою учетную запись электронной почты и попытался получить доступ к моей личной информации. Человек 2: Как они получили доступ? Я думал, что сказал вам включить двухфакторную аутентификацию. Человек 1: Я был слишком ленив, чтобы включить это. Человек 2: Бодливой корове Бог рог не даёт.
Choices: A: Человек 2, вероятно, думает, что в несчастье человека 1 виноват случайный хакер.  B: TЧеловек 2, вероятно, считает, что человек 1 сам виноват в своих несчастьях.
The English translation is:
Proverb: God does not give a horn to a carnivorous cow
Context: Person 1: I discovered that someone hacked my email account and tried to access my personal information. Person 2: How did they get access? I thought I told you to enable two-factor authentication. Person 1: I was too lazy to turn it on. Person 2: God does not give a horn to a carnivorous cow.
Choices: A: Person 2 probably thinks that a random hacker is to blame for Person 1's misfortune.  B: Person 2 probably believes that Person 1 is to blame for his own misfortunes.
Final answer: B
""",
        "German": f"""Proverb: wenn man vom teufel spricht, dann kommt er gelaufen
Context: Person 1: Hast du schon von dem neuen Kollegen gehört? Person 2: Nein, wer ist das? Person 1: Ach, wenn man vom Teufel spricht, dann kommt er gelaufen.
Choices: A: Person 2 sieht gerade den neuen Kollegen.  B: Person 2 hat den neuen Kollegen nicht gesehen.
The English translation is:
Proverb: When you talk about the devil, he comes running
Context: Person 1: Have you heard from the new colleague yet? Person 2: No, who is that? Person 1: Oh, when you talk about the devil, he comes running.
Choices: A: Person 2 is currently seeing their new colleague.  B: Person 2 has not seen the new colleague.
Final answer: A
""",
        "Persian": f"""Proverb: ماهی را هر وقت از آب بگیری تازه است
Context: شخص ۱: 'فکر می‌کنم برای شروع یادگیری زبان جدید خیلی دیر شده.' شخص ۲: 'اصلاً اینطور نیست، ماهی را هر وقت از آب بگیری تازه است.'
Choices: A: شخص ۲ معتقد است که همیشه برای شروع یک کار دیر است. B: شخص ۲ معتقد است که هیچ وقت برای شروع یک کار دیر نیست.
The English translation is:
Proverb: The fish is fresh whenever you take it out of the water.
Context: Person 1: 'I think it is too late to start learning a new language.' Person 2: 'Not at all, the fish is fresh whenever you take it out of the water.
Choices: A: Person 2 believes that it is always too late to start something. B: Person 2 believes that it is never too late to start something.
Final answer: B
""",
    }
