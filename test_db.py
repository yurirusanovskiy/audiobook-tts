from sqlmodel import Session, select
from db.database import engine
from db.models import Character, DictionaryEntry
from db.crud import get_dictionary_for_language

def test():
    with Session(engine) as session:
        # Create a dictionary entry if not exists
        statement_dict = select(DictionaryEntry).where(DictionaryEntry.word == "AI")
        retrieved_dict = session.exec(statement_dict).first()
        if not retrieved_dict:
            dict_entry = DictionaryEntry(
                language="en",
                word="AI",
                phonetic_replacement="A-I"
            )
            session.add(dict_entry)
            session.commit()
        
        # Test CRUD method
        en_dict = get_dictionary_for_language(session, "en-US")
        print("\n--- CRUD Test Results ---")
        print("Dictionary for 'en-US':", en_dict)
        print("-----------------------\n")

if __name__ == "__main__":
    test()
