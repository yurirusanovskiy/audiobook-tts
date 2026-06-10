from ruaccent import RUAccent
accentuator = RUAccent()
accentuator.load(omograph_model_size='big_poetry', use_dictionary=True)
res = accentuator.process_all("замок")
print(f"RUACCENT OUTPUT: {res}")
