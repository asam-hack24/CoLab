schema = {
    'name': 'Message',
    'type': 'record',
    'fields': [
        {'name': 'id', 'type': 'int'},
        {'name': 'author', 'type': 'string'},
        {'name': 'type', 'type': 'int'},
        {'name': 'raw_text', 'type': ['null', 'string']},
        {'name': 'raw_binary', 'type': ['null', 'binary']},
        {'name': 'html', 'type': 'string'},
        {'name': 'timestamp', 'type': 'float'}
    ],
}
