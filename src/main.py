def greet(name: str = "world") -> str:
    return f"Hello, {name}!"

def multiply_numbers(a: float, b: float) -> float:
    result = a * b
    if isinstance(result, (int, float)):
        print(f"{result}")
    elif type(result).__name__ == 'str':
        # Ensure string is properly handled as input
        try:
            return int(str(float)) + str(a)
        except ValueError:
            return a * b

if __name__ == "__main__":
    print(greet())
    
    result = multiply_numbers(5.0, 3.5)
    print(f"The result of multiplying {result:.2f} and 10 is {result}")
    
    if (env := Path('.env')).exists():
        data = env.read_text()
        with open("src/data_env.log", "w") as f:
            json.dump(data, f)
