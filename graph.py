import pandas as pd


# Create Graph
def createBarChartOnStatementDistribution(inputDF: pd.DataFrame, title="LIAR DataSet"):
    # computes frequencies of labels and converts to percentages
    label_frequencies = inputDF['statement'].value_counts(normalize=True)

    # Reach %
    def multiply100(x):
        return x * 100

    label_frequencies = label_frequencies.apply(multiply100)

    # bar chart ordering and  colors for readability.
    labels = ['pants-fire', 'false', 'barely-true', 'half-true', 'mostly-true', 'true']
    colors = [
        'orangered',  # pants-fire
        'coral',  # false
        'salmon',  # barely-true
        'peachpuff',  # half-true
        'skyblue',  # mostly-true
        'deepskyblue'  # true
    ]

    label_frequencies = label_frequencies.reindex(index=labels)

    # creates a horizontal bar chart with a descriptive title
    axis = label_frequencies.plot(kind='barh', figsize=(12, 8), color=colors)
    axis.set_title(f"Distribution of label values ({title}, sample_size={len(inputDF)})", size=20)
