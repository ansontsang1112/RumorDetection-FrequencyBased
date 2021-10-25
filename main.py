import dataFrameManagement

# Executable
import speakerBasedModel

if __name__ == '__main__':
    # Get data from dataset
    df = dataFrameManagement.readDataFrame('LIAR-PLUS/dataset/train2.tsv')

    # Gen Graph based on "Statement"
    #graph.createBarChartOnStatementDistribution(df)
    #plt.show()

    pharse = '"Household income among Hispanic Americans has just set a new record high."'
    test = speakerBasedModel.speakerStatementScore(speakerBasedModel.speakerStatementModel(df), "donald-trump", pharse)

    print(test)
