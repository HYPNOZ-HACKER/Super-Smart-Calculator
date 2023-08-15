# main.py
from app.calculator import Calculator
from app.ai_model import AIModel

def main():
    calculator = Calculator()
    ai_model = AIModel()

    while True:
        expression = input("Enter an expression or type 'exit' to quit: ")
        if expression.lower() == 'exit':
            break

        try:
            result = calculator.evaluate(expression)
            print("Calculator Result:", result)
            
            ai_result = ai_model.predict(expression)
            print("AI Result:", ai_result)

        except Exception as e:
            print("Error:", str(e))

if __name__ == "__main__":
    main()
