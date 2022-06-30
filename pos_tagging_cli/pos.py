import sys
import subprocess

import colorful as cf
import nltk

TAGS = {
    "CC": "Coordinating conjunction",
    "CD": "Cardinal number",
    "DT": "Determiner",
    "EX": "Existential there",
    "FW": "Foreign word",
    "IN": "Preposition or subordinating conjunction",
    "JJ": "Adjective",
    "JJR": "Adjective, comparative",
    "JJS": "Adjective, superlative",
    "LS": "List item marker",
    "MD": "Modal",
    "NN": "Noun, singular or mass",
    "NNS": "Noun, plural",
    "NNP": "Proper noun, singular",
    "NNPS": "Proper noun, plural",
    "PDT": "Predeterminer",
    "POS": "Possessive ending",
    "PRP": "Personal pronoun",
    "PRP$": "Possessive pronoun",
    "RB": "Adverb",
    "RBR": "Adverb, comparative",
    "RBS": "Adverb, superlative",
    "RP": "Particle",
    "SYM": "Symbol",
    "TO": "to",
    "UH": "Interjection",
    "VB": "Verb, base form",
    "VBD": "Verb, past tense",
    "VBG": "Verb, gerund or present participle",
    "VBN": "Verb, past participle",
    "VBP": "Verb, non-3rd person singular present",
    "VBZ": "Verb, 3rd person singular present",
    "WDT": "Wh-determiner",
    "WP": "Wh-pronoun",
    "WP$": "Possessive wh-pronoun",
    "WRB": "Wh-adverb",
}


def tag_colors(tag: str):
    if "DT" in tag:
        return cf.white_on_purple
    elif "RB" in tag:
        return cf.white_on_brown
    elif tag.startswith("PRP"):
        return cf.black_on_khaki
    elif tag.startswith("V") or tag == "MD":
        return cf.black_on_green
    elif tag.startswith("NN"):
        return cf.black_on_grey
    elif tag.startswith("JJ"):
        return cf.black_on_orange
    elif tag.startswith("CC"):
        return cf.black_on_burlywood
    elif tag == "IN":
        return cf.black_on_pink
    elif tag == "TO":
        return cf.black_on_white
    return cf.white


def pos_tagging(sentence: str):
    text = nltk.word_tokenize(sentence)
    for word, tag in nltk.pos_tag(text):
        c = tag_colors(tag)
        if tag not in TAGS:
            print(word)
        else:
            print(c(tag.center(4)), "%-30s %s" % (word, c(TAGS[tag])))
    print()


def main():
    if len(sys.argv) > 1:
        pos_tagging(sys.argv[1])
    else:
        while True:
            sentence = input("[pt]: ")

            if len(sentence.split()) == 1:
                subprocess.run(["zdict", sentence])
            else:
                pos_tagging(sentence)


if __name__ == "__main__":
    main()
