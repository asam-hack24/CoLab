from abc import ABCMeta, abstractmethod
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor
from nbconvert import HTMLExporter


class ScriptExecutor(metaclass=ABCMeta):
    @abstractmethod
    def execute(self, script):
        pass

    def do_execute(self, script, kernel, timeout=600):
        cells = [nbformat.v4.new_code_cell(source=script)]
        nb = nbformat.v4.new_notebook(cells=cells,
                                      metadata={'language': 'python'})

        # Execute the script
        executor = ExecutePreprocessor(timeout=timeout, kernel_name=kernel)
        nb, metadata = executor.preprocess(nb, {'metadata': {}})

        # Export html from the notebook
        html_exporter = HTMLExporter()
        html_exporter.template_file = 'basic'
        body, _ = html_exporter.from_notebook_node(nb)

        # Extract the result part of the html
        output = ScriptExecutor.extract_output(body, kernel)

        return output

    @staticmethod
    def extract_output(html_string, kernel):
        # Remove the first bit
        cleaned_record = ""
        number_of_lines = 0
        do_keep = False
        for line in html_string.splitlines():
            if '<div class="output">' in line:
                do_keep = True
            if do_keep and line:
                cleaned_record += line
                cleaned_record += '\n'
                number_of_lines += 1

        # Remove the first an the last three lines
        lines = cleaned_record.splitlines()
        lines = lines[1:-3]
        cleaned_record = ""

        print(kernel)
        if kernel == "ir":
            ScriptExecutor._clean_r(lines)

        remove_newlines = False
        for line in lines:
            if line.startswith('<img'):
                remove_newlines = True
            if remove_newlines and line.startswith('>'):
                remove_newlines = False
            cleaned_record += line
            if not remove_newlines:
                cleaned_record += '\n'

        return cleaned_record

    @staticmethod
    def _clean_r(lines):
        for index in range(len(lines)):
            line = lines[index]
            if line.startswith("<pre>[1]"):
                lines[index] = line.replace("<pre>[1]", "<pre>")

