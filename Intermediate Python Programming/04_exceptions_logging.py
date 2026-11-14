# 04 - Exception Handling and Logging

import logging

# Logging records program events; the level controls what is shown.
logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s"
)

def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        logging.exception("Cannot divide by zero")
        return None
    except TypeError:
        logging.exception("Please provide numbers")
        return None
    else:
        logging.info("Division completed successfully")
        return result
    finally:
        print("The divide function has finished.")

print("10 / 2 =", divide(10, 2))
print("10 / 0 =", divide(10, 0))

# Raising your own exception
def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    return age

try:
    print("Age:", check_age(-2))
except ValueError as error:
    logging.error("Invalid input: %s", error)
