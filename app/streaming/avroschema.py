schema = {
    'name': 'Message',
    'type': 'record',
    'fields': [
        {'name': 'id', 'type': 'int'},
        {'name': 'author', 'type': 'string'},
        {'name': 'type', 'type': 'int'},
        {'name': 'raw_text', 'type': ['null', 'string'], "default": None},
        {'name': 'binary', 'type': ['null', 'bytes'], "default": None},
        {'name': 'html', 'type': 'string'},
        {'name': 'timestamp', 'type': 'float'},
        {'name': 'topic', 'type': 'string'}
    ],
}

event_schema = {
    'name': 'EventMessage',
    'type': 'record',
    'fields': [
        {'name': 'event_type', 'type': 'string'},
        {'name': 'name', 'type': 'string'}
    ]
}
