def greet(*args, **kwargs):
    # Join args into a single string
    full_name = " ".join(args)
    # If there are keyword arguments, format them
    last_name = kwargs.get('last_name', '')
    print(f"Hello, {full_name} {last_name}")

greet("John", last_name="Doe")