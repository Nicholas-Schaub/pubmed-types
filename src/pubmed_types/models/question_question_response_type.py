from enum import Enum


class QuestionQuestionResponseType(Enum):
    ESSAY = "essay"
    FILL_IN_THE_BLANK = "fill-in-the-blank"
    MULTI_SELECT = "multi-select"
    MULTIPLE_CHOICE = "multiple-choice"
    SHORT_ANSWER = "short-answer"
    TRUE_FALSE = "true-false"
