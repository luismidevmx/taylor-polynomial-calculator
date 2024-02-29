GRADE_TOO_LOW_ERROR = {
    "type": "Low Grade",
    "title": "The grade must be between 3 and 20",
    "message": "Calculating less than 3 terms doesn't make sense, why not a few more? 🤔",
}

GRADE_TOO_HIGH_ERROR = {
    "type": "Grade Too High",
    "title": "The grade must be between 3 and 20",
    "message": "The more terms you ask me for, the longer it takes to solve the derivatives, as much as I would like to, they are so many 😵.",
}

INVALID_NUMBER_ERROR = {
    "type": "Invalid Number",
    "title": "The grade must be an integer",
    "message": "Check that the URL contains the key 'grade' with an integer value between 3 and 20 (e.g., '&grade=5') 😅.",
}

INVALID_X0_ERROR = {
    "type": "Invalid Value",
    "title": "The value of 'x0' is not a number",
    "message": "Check that the URL contains the key 'x0' with a number (e.g., '&x0=5') 😅.",
}

INVALID_EXPRESSION_ERROR = {
    "type": "Invalid Expression",
    "title": "The function is not processable",
    "message": "Check that the function is well written (e.g., 'sin(x)') 😅.",
}

UNKNOWN_ERROR = {
    "title": "An unexpected or private error has occurred",
    "type": "Unknown Error",
    "message": "I am not prepared for that level of mathematics  😵.",
}
