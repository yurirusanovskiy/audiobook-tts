from sqlmodel import Session, select
from db.database import engine
from db.models import Character, DictionaryEntry

def test():
    with Session(engine) as session:
        # Create a character
        hero = Character(
            id="hero_01",
            name="Commander Shepard",
            language_code="en-US",
            voice_id="en-US-Journey-F",
            pitch="-2st",
            speed=1.05
        )
        
        # Create a dictionary entry
        dict_entry = DictionaryEntry(
            language="en",
            word="AI",
            phonetic_replacement="A-I"
        )
        
        session.add(hero)
        session.add(dict_entry)
        session.commit()
        
        # Query back
        statement = select(Character).where(Character.id == "hero_01")
        retrieved_hero = session.exec(statement).first()
        print("\n--- DB Test Results ---")
        print("Retrieved Character:", retrieved_hero)
        
        statement_dict = select(DictionaryEntry).where(DictionaryEntry.word == "AI")
        retrieved_dict = session.exec(statement_dict).first()
        print("Retrieved Dictionary Entry:", retrieved_dict)
        print("-----------------------\n")

if __name__ == "__main__":
    test()
