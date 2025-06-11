import sys
from app import CalculatorApp

def main():
    app = CalculatorApp(sys.argv)
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
