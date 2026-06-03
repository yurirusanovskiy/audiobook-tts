from sqlmodel import Session
from db.database import engine
from db.models import DictionaryEntry
from db.crud import get_dictionary_for_language, get_available_dictionary_languages

def test():
    with Session(engine) as session:
        # 1. Let's add a few more words in different languages
        session.add(DictionaryEntry(language="ru", word="Замок", phonetic_replacement="Замо+к"))
        session.add(DictionaryEntry(language="ru", word="Света", phonetic_replacement="Све+та"))
        session.add(DictionaryEntry(language="ro", word="chestie", phonetic_replacement="kestie"))
        session.commit()

        # 2. Test fetching words for 'ru-RU' (should map to 'ru')
        ru_dict = get_dictionary_for_language(session, "ru-RU")
        print("1. Dictionary mapping for Russian ('ru-RU'):")
        print(ru_dict)

        # 3. Test fetching the list of all available languages
        langs = get_available_dictionary_languages(session)
        print("\n2. List of available languages in the dictionary DB:")
        print(langs)

if __name__ == "__main__":
    test()
