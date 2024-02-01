import os
import pandas as pd
import time
import plotly.graph_objects as go
import numpy as np
import webbrowser
from const import dataPath, filePath, order

def loadDataFrame(folderPath):
    dfs = []
    for fileName in os.listdir(folderPath):
        if fileName.endswith('.csv'):
            filePath = os.path.join(folderPath, fileName)
            df = pd.read_csv(filePath)

            if 'id' not in df.columns:
                # only for current data w/o id
                df['id'] = df['createTime']
            df['fetchDataTime'] =  time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(fileName[:-4])))
            dfs.append(df)
            
    combinedDf = pd.concat(dfs, ignore_index=True)
    combinedDf = combinedDf.sort_values(by=['id', 'fetchDataTime'])
    combinedDf['delta_collectCount'] = combinedDf.groupby('id')['collectCount'].diff().fillna(0).astype(int)
    combinedDf['delta_commentCount'] = combinedDf.groupby('id')['commentCount'].diff().fillna(0).astype(int)
    combinedDf['delta_diggCount'] = combinedDf.groupby('id')['diggCount'].diff().fillna(0).astype(int)
    combinedDf['delta_playCount'] = combinedDf.groupby('id')['playCount'].diff().fillna(0).astype(int)
    
    unique_indices = combinedDf['id'].unique()
    random_values = np.random.randint(0, 256*64, (len(unique_indices), 3))
    index_to_random = dict(zip(unique_indices, random_values))

    combinedDf['colors'] = combinedDf['id'].map(lambda x: f'rgb({", ".join(map(str, index_to_random[x]/64))})')
    combinedDf = combinedDf[order]
    
    return combinedDf

def plotlyPlot(type, combinedDf):
    dfPlot = combinedDf.sort_values(by=[type, 'id', 'fetchDataTime'], ascending=False)

    fig = go.Figure()

    # Iterate over unique IDs and add a trace for each
    for id_value in dfPlot['id'].unique():
        id_desc = dfPlot[dfPlot['id'] == id_value]['desc'].unique()
        id_desc_short = id_desc[0][:10]
        id_data = dfPlot[dfPlot['id'] == id_value]
        id_data.insert(0, 'desc_short', id_desc_short)
        id_color = dfPlot[dfPlot['id'] == id_value]['colors'].unique()
        id_color = id_color[0]
        fig.add_trace(go.Scatter(x=id_data['fetchDataTime'], y=id_data[type],
                                marker=dict(size=12,line=dict(width=2), color=id_color),
                                line=dict(color=id_color),
                                mode='lines+markers', name=f'Video ID: {id_value} | Desc: {id_desc_short}',
                                customdata=np.stack((id_data['id'], id_data[f'delta_{type}'], id_data['desc_short']), axis=-1),
                                hovertemplate="<br>".join([
                                    "<b>Video ID: %{customdata[0]}</b>",
                                    "Link: <a href=https://www.tiktok.com/@geevideo/video/%{customdata[0]}>https://www.tiktok.com/@geevideo/video/%{customdata[0]}</a>",
                                    "Desc: %{customdata[2]}",
                                    "Date: %{x}",
                                    "Count: %{y}",
                                    "Delta: %{customdata[1]}",
                                    "<extra></extra>"
                                ])))

    # Customize layout
    fig.update_layout(
        xaxis_title='Fetch Data Time (UTC+8)',
        yaxis_title=type,
        title=f'{type} Over Time for Each ID (Video Posted After 29 Jan 2024 09:00:00 PM UTC+8)',
        hoverlabel=dict(
            bgcolor="white",
            font_size=12,
        ),
        modebar_add=[
            "v1hovermode",
            "toggleSpikeLines"
        ]
    )

    return fig

    
if __name__ == '__main__':
    df = loadDataFrame(dataPath)
    
    playFig = plotlyPlot('playCount', df)
    collectFig = plotlyPlot('collectCount', df)
    diggFig = plotlyPlot('diggCount', df)
    commentFig = plotlyPlot('commentCount', df)
    
    with open(filePath + 'p_graph.html', 'w') as f:
        f.write(playFig.to_html(full_html=False, include_plotlyjs=True, div_id='playCount'))
        f.write(collectFig.to_html(full_html=False, include_plotlyjs='cdn', div_id='collectCount'))
        f.write(diggFig.to_html(full_html=False, include_plotlyjs='cdn', div_id='diggCount'))
        f.write(commentFig.to_html(full_html=False, include_plotlyjs='cdn', div_id='commentCount'))
    webbrowser.open('file://' + filePath + 'p_graph.html')
    