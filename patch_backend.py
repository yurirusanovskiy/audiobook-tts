with open("api/v1/routes/scenes.py", "r") as f:
    content = f.read()

content = content.replace("""        if line.prompt_override:
            parts.append(line.prompt_override)
        elif getattr(char, 'prompt_style', None):
            parts.append(char.prompt_style)""", """        if getattr(char, 'prompt_style', None):
            parts.append(f"Voice style: {char.prompt_style}")
            
        if line.prompt_override:
            parts.append(f"Expression: {line.prompt_override}")""")

with open("api/v1/routes/scenes.py", "w") as f:
    f.write(content)

with open("api/v1/routes/processing.py", "r") as f:
    content2 = f.read()

content2 = content2.replace("""            if final_line_prompt:
                parts.append(final_line_prompt)""", """            if getattr(char, 'prompt_style', None):
                parts.append(f"Voice style: {char.prompt_style}")
            if final_line_prompt and final_line_prompt != getattr(char, 'prompt_style', None):
                parts.append(f"Expression: {final_line_prompt}")""")

with open("api/v1/routes/processing.py", "w") as f:
    f.write(content2)

