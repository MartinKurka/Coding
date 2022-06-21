"""
pip install googletrans==3.1.0a0
"""

from googletrans import Translator

def translate_text(txt, lang='cs'):
    translator = Translator()
    translation = translator.translate(txt, dest=lang)
    # print(translation.text)
    return(translation.text)


if __name__ == "__main__":
    translate_text()