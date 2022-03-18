import plotly.express as px
import irisBasic

def main():
    df = px.data.iris()
    irisBasic.saveData(df)

if __name__ == '__main__':
    main()