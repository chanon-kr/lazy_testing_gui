# Py Topping Testing GUI

## A lazy testing GUI
In this GUI, include testing for;
1. Check Opening Port
2. Check Socket Sending and Listening

## How to use
1. Git Clone

```git clone https://github.com/chanon-kr/lazy_testing_gui.git```

2. --Optional-- Create Virtual Environment

```python -m venv test_gui```

3. --Optional-- Activate Virtual Environment

```test_gui\Scripts\activate```

4. Install Dependencies

```pip install -r requirements.txt```

5. Run the GUI

```python main.py```

6. --Optional-- Pack into an exe for user (You need to uncomment the pyinstaller in requirements.txt)

```pyinstaller --noconsole --onefile main.py```