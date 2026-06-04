from sqlmodel import Session
from db.database import engine
from core.preprocessor import PreprocessorFactory

def test():
    with Session(engine) as session:
        preprocessor = PreprocessorFactory.get_preprocessor("ru-RU")
        text = "Он подошел к двери и увидел огромный замок. Это был самый большой замок в его жизни."
        print("Original:", text)
        processed = preprocessor.process(text, session)
        print("Processed:", processed)

if __name__ == "__main__":
    test()
