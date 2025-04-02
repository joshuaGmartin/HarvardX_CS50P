from validator_collection import validators, checkers, errors

try:
    # email_address = validators.email("test@domain.dev")
    # email_address = validators.email("malan@harvard.edu")
    # email_address = validators.email("billy.bob@gmail.com")
    # email_address = validators.email("malan@@@harvard.edu")
    email_address = validators.email("malan@harvard..edu")
    # email_address = validators.email("test")
    # email_address = validators.email("my email is test@domain.dev")
    # email_address = validators.email()
except errors.InvalidEmailError:
    print("Invalid")
except errors.EmptyValueError:
    print("Invalid")
except errors.ValidatorUsageError:
    print("Invalid")
else:
    print("Valid")
