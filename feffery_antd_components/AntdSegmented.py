# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class AntdSegmented(Component):
    """An AntdSegmented component.
分段控制器组件AntdSegmented

Keyword arguments:

- id (string; optional):
    组件唯一id.

- aria-* (string; optional):
    `aria-*`格式属性通配.

- batchPropsNames (list of strings; optional):
    需要纳入[批量属性监听](/batch-props-values)的若干属性名.

- batchPropsValues (dict; optional):
    监听`batchPropsNames`中指定的若干属性值.

- block (boolean; default False):
    是否撑满父容器  默认值：`False`.

- className (string | dict; optional):
    当前组件css类名，支持[动态css](/advanced-classname).

- data-* (string; optional):
    `data-*`格式属性通配.

- defaultValue (string | number; optional):
    设置初始化选中值.

- disabled (boolean; default False):
    是否禁用当前组件  默认值：`False`.

- key (string; optional):
    对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果.

- loading_state (dict; optional)

    `loading_state` is a dict with keys:

    - component_name (string; optional):
        Holds the name of the component that is loading.

    - is_loading (boolean; optional):
        Determines if the component is loading or not.

    - prop_name (string; optional):
        Holds which property is loading.

- options (list of dicts; optional):
    配置选项相关参数.

    `options` is a list of dicts with keys:

    - disabled (boolean; optional):
        是否禁用当前选项  默认值：`False`.

    - icon (string; optional):
        选项前缀图标，`iconRenderer='AntdIcon'`时同`AntdIcon`，`iconRenderer='fontawesome'`时表示css类名.

    - iconRenderer (a value equal to: 'AntdIcon', 'fontawesome'; optional):
        选项前缀图标类型，可选项有`'AntdIcon'`、`'fontawesome'`  默认值：`'AntdIcon'`.

    - label (a list of or a singular dash component, string or number; required):
        组件型，必填，选项标题内容.

    - value (string | number; required):
        必填，选项值.

- persisted_props (list of a value equal to: 'value's; default ['value']):
    开启属性持久化功能的若干属性名，可选项有`'value'`  默认值：`['value']`.

- persistence (boolean | string | number; optional):
    是否开启[属性持久化](/prop-persistence).

- persistence_type (a value equal to: 'local', 'session', 'memory'; default 'local'):
    属性持久化存储类型，可选项有`'local'`（本地持久化），`'session'`（会话持久化），`'memory'`（内存持久化）
    默认值：`'local'`.

- size (a value equal to: 'large', 'middle', 'small'; default 'middle'):
    组件尺寸规格，可选项有`'small'`、`'middle'`、`'large'`  默认值：`'middle'`.

- style (dict; optional):
    当前组件css样式.

- value (string | number; optional):
    监听或设置当前选中值."""
    _children_props = ['options[].label']
    _base_nodes = ['children']
    _namespace = 'feffery_antd_components'
    _type = 'AntdSegmented'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, key=Component.UNDEFINED, style=Component.UNDEFINED, className=Component.UNDEFINED, options=Component.UNDEFINED, value=Component.UNDEFINED, defaultValue=Component.UNDEFINED, block=Component.UNDEFINED, disabled=Component.UNDEFINED, size=Component.UNDEFINED, batchPropsNames=Component.UNDEFINED, batchPropsValues=Component.UNDEFINED, loading_state=Component.UNDEFINED, persistence=Component.UNDEFINED, persisted_props=Component.UNDEFINED, persistence_type=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'aria-*', 'batchPropsNames', 'batchPropsValues', 'block', 'className', 'data-*', 'defaultValue', 'disabled', 'key', 'loading_state', 'options', 'persisted_props', 'persistence', 'persistence_type', 'size', 'style', 'value']
        self._valid_wildcard_attributes =            ['data-', 'aria-']
        self.available_properties = ['id', 'aria-*', 'batchPropsNames', 'batchPropsValues', 'block', 'className', 'data-*', 'defaultValue', 'disabled', 'key', 'loading_state', 'options', 'persisted_props', 'persistence', 'persistence_type', 'size', 'style', 'value']
        self.available_wildcard_properties =            ['data-', 'aria-']
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(AntdSegmented, self).__init__(**args)
