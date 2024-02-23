import dash
import json
from dash import html
import feffery_antd_components as fac
from dash.dependencies import Input, Output, State

app = dash.Dash(__name__)

app.layout = html.Div(
    fac.AntdSpace(
        [
            html.Pre(
                id='demo-output'
            ),
            html.Pre(
                id='status-output'
            ),
            fac.AntdForm(
                [
                    fac.AntdFormItem(
                        fac.AntdInput(
                            id='test-field1',
                            name='测试字段1',
                            value='初始值'
                        ),
                        label='测试字段1',
                        rules=[
                            {
                                'required': True,
                                'message': '不满足手机号码校验',
                                'validateTrigger': 'onBlur',
                                'pattern': '^(?:(?:\+|00)86)?1[3-9]\d{9}$'
                            },
                        ]
                    ),
                    fac.AntdFormItem(
                        fac.AntdInput(
                            id='test-field2',
                            name='测试字段2',
                            value='初始值'
                        ),
                        label='测试字段2',
                        rules=[
                            {
                                'required': True,
                                'message': '不能为空',
                                'validateTrigger': 'onChange',
                            },
                            {
                                'message': '长度不能大于5',
                                'validateTrigger': 'onChange',
                                'max': 5
                            }
                        ]
                    ),
                    fac.AntdFormItem(
                        fac.AntdInput(
                            id='test-field3',
                            name='测试字段3',
                            value='初始值'
                        ),
                        label='测试字段3',
                        rules=[
                            {
                                'required': True,
                                'message': '长度不能小于5',
                                'validateTrigger': 'onFocus',
                                'min': 5
                            }
                        ]
                    ),
                    fac.AntdFormItem(
                        fac.AntdSpace(
                            [
                                fac.AntdButton(
                                    '提交',
                                    id='submit-button',
                                    type='primary',
                                ),
                                fac.AntdButton(
                                    '重置',
                                    id='reset-button',
                                )
                            ]
                        )
                    ),
                ],
                id='demo-form'
            )
        ],
        direction='vertical',
        style={
            'width': '100%'
        }
    ),
    style={
        'padding': '50px 100px'
    }
)


@app.callback(
    Output('demo-form', 'submitForm'),
    Input('submit-button', 'nClicks'),
    prevent_initial_call=True
)
def submit_form(nClicks):
    if nClicks:
        return True
    return dash.no_update


@app.callback(
    [Output('demo-form', 'resetForm'),
     Output('test-field1', 'value'),
     Output('test-field2', 'value'),
     Output('test-field3', 'value')],
    Input('reset-button', 'nClicks'),
    prevent_initial_call=True
)
def reset_form(nClicks):
    if nClicks:
        return True, None, None, None
    return dash.no_update, dash.no_update, dash.no_update, dash.no_update


@app.callback(
    Output('demo-output', 'children'),
    Input('demo-form', 'submitFormClicks'),
    [State('demo-form', 'values'),
     State('demo-form', 'formValidateStatus')],
    prevent_initial_call=True
)
def demo(submitFormClicks, values, formValidateStatus):
    if formValidateStatus:
        return json.dumps(
            values,
            ensure_ascii=False,
            indent=4
        )
    return '校验失败'


if __name__ == '__main__':
    app.run(debug=True)
