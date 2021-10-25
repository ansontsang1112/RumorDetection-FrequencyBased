import pandas as pd
from typing import Dict


def scoreLabelingSystem(label):
    scores = {
        'true': 2,
        'mostly-true': 1,
        'half-true': 0,
        'barely-true': -1,
        'false': -2,
        'pants-fire': -3
    }
    return scores[label]


def speakerStatementModel(inputDataFrame: pd.DataFrame) -> Dict[str, Dict[str, float]]:
    total = {}  # Whole dataset in DICT (All Speakers)
    count = {}  # How often it appear in all claims (All Speakers)

    for _, row in inputDataFrame.T.items():
        # General Information
        speaker = row['speaker']
        score = scoreLabelingSystem(row['statement'])
        words = row['subjects'].lower().split()

        # No Repeat words
        uniqueness = []

        for word in words:
            # if its a word we've already seen, skip processing
            if word in uniqueness:
                continue

            uniqueness.append(word)

            if speaker in total:
                if word in total[speaker]:
                    # Case 1: Word already in "Global Data", add the score for this word
                    total[speaker][word] += score
                    count[speaker][word] += 1
                else:
                    # Case 2: New words appear in "Global Data", add the score for this word
                    total[speaker][word] = score
                    count[speaker][word] = 1

            else:
                # Case 3: New speaker on "Global Data", add speaker and score
                total[speaker] = {}
                total[speaker][word] = score

                count[speaker] = {}
                count[speaker][word] = 1

    for speaker in total:
        # Loop for all speaker's words
        for word in total[speaker]:
            # The average mark for the word
            total[speaker][word] = total[speaker][word] / count[speaker][word]

    return total


def speakerStatementScore(model: Dict[str, Dict[str, float]], speaker: str, phrase: str):
    index = 0
    score = 0

    for word in phrase.split():
        word = word.lower()

        if word in model[speaker]:
            # Check if word spoken by the Speaker before and get the score of that words.
            score += model[speaker][word]
            index += 1

    if not index:
        return None

    # Take average score the speaker in that sentence
    return score / index
