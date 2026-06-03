from core.preprocessor import PreprocessorFactory

def test():
    print("Testing English Preprocessor...")
    en_proc = PreprocessorFactory.get_preprocessor("en-US")
    en_text = en_proc.process("The AI system is offline.", {"AI": "A-I"})
    print(f"EN: {en_text}")

    print("\nTesting Romanian Preprocessor...")
    ro_proc = PreprocessorFactory.get_preprocessor("ro-RO")
    ro_text = ro_proc.process("A fost o chestie.", {"chestie": "kestie"})
    print(f"RO: {ro_text}")

    print("\nTesting Russian Preprocessor (This will load the model!)...")
    ru_proc = PreprocessorFactory.get_preprocessor("ru-RU")
    # ruaccent needs properly cased dictionary words sometimes or it might ignore, 
    # but let's test our dictionary replacement and then ruaccent.
    ru_text = ru_proc.process("Замок был закрыт на замок.", {"Замок": "Замо+к"})
    print(f"RU: {ru_text}")

if __name__ == "__main__":
    test()
