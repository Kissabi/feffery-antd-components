import dash
from dash import html
import feffery_antd_components as fac

app = dash.Dash(__name__)

app.layout = html.Div(
    [fac.AntdQRCode(value='测试')],
    style={'padding': 50},
)

if __name__ == '__main__':
    app.run(debug=True)
