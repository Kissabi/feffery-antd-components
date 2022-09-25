if True:
    import sys
    sys.path.append('../..')
    import dash
    import json
    from dash import html
    import feffery_antd_components as fac
    from dash.dependencies import Input, Output

app = dash.Dash(
    __name__,
    suppress_callback_exceptions=True
)

app.layout = html.Div(
    [
        fac.AntdButton(
            '执行',
            id='button-demo',
            type='primary',
            autoSpin=True
        ),
        fac.AntdParagraph(id='output')
    ],
    style={
        'width': '800px',
        'margin': '0 auto'
    }
)


@app.callback(
    [Output('button-demo', 'loading'),
     Output('output', 'children')],
    Input('button-demo', 'nClicks'),
    prevent_initial_call=True
)
def demo(nClicks):
    import time
    from datetime import datetime

    if nClicks:

        time.sleep(3)

        return [
            False,
            datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        ]

    return dash.no_update


if __name__ == '__main__':
    app.run(debug=True)
