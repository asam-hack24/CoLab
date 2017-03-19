from app.messages.message import MessageType
import nbformat


def create_notebook_from_messages(messages, kernel_type):
    cells = []
    for message in messages:
        message_type = message.get_message_type()
        if message_type is kernel_type:
            cells.append(nbformat.v4.new_code_cell(source=message.get_raw_message()))
        elif message_type is MessageType.TEXT:
            cells.append(nbformat.v4.new_markdown_cell(source=message.get_raw_message()))
        elif message_type is MessageType.IMAGE:
            cells.append(nbformat.v4.new_markdown_cell(source=message.get_html()))
        else:
            raise ValueError("The message of type {} cannot be added to python notebook".format(type(message_type)))
    if not cells:
        return None

    if kernel_type is MessageType.PYTHON:
        nbformat.v4.new_notebook(cells=cells, metadata={'language': 'python'})
    else:
        nbformat.v4.new_notebook(cells=cells, metadata={'language': 'python'}) # TODO is this correct?


def save_python_notebook_to_file(to_convert, file_object):
    print(len(to_convert))
   # print(type(file_object))

    notebook = create_notebook_from_messages(to_convert, MessageType.PYTHON)
    if notebook is not None:
        nbformat.write(nb=notebook, fp=file_object)


def save_r_notebook_to_file(to_convert, file_object):
    notebook = create_notebook_from_messages(to_convert, MessageType.R)
    if notebook is not None:
        nbformat.write(nb=notebook, fp=file_object)
