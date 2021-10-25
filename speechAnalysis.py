import pandas as pd
import graph
import matplotlib as plt


def speakerAnalysis(inputDataFrame: pd.DataFrame):
    numOfUniqueSpeaker = inputDataFrame['speaker'].nunique()
    avgStatement = len(inputDataFrame) / numOfUniqueSpeaker

    print(f"Unique speakers in dataset: {numOfUniqueSpeaker}")
    print(f"Average statements made per speaker: {avgStatement}")


def speakerSpeechStatementVisualized(inputDataFrame: pd.DataFrame):
    # Looped in the speaker (unique)
    for speaker in list(inputDataFrame['speaker'].unique()):
        speakerDataFrame = inputDataFrame[inputDataFrame['speaker'] == speaker]
        speakerDataFrame.reset_index(inplace=True)

        # build a statement barchart
        graph.createBarChartOnStatementDistribution(speakerDataFrame, title=speaker)
        plt.show()
    return len(list(inputDataFrame['speaker'].unique()))
