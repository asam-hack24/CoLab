from abc import ABCMeta, abstractmethod
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor
from nbconvert import HTMLExporter
import os


class ScriptExecutor(metaclass=ABCMeta):
    @abstractmethod
    def execute(self, script):
        pass

    def do_execute(self, script, kernel, timeout=600):
        # Steps for script export the execution
        # 1. Save script to ipython notebook file
        # 2. Read it back in with nb format
        # 3. Execute the script with the correct kernel
        # 4. Export html from the notebook
        # 5. Extract the result from the html

        # Save to script
        notebook_filename = 'script_to_execute.ipynb'
        path_to_module = os.path.abspath(__file__)
        full_file_name = os.path.join(path_to_module,notebook_filename)
        with open(full_file_name, 'w') as f:
            f.write(script)

        # Read to notebook
        with open(notebook_filename) as f:
            nb = nbformat.read(f, as_version=4)

        # Execute the script
        executor = ExecutePreprocessor(timeout=timeout, kernel_name=kernel)
        executor.preprocess(nb, {'metadata': {'path': 'notebooks/'}})

        # Export html from the notebook
        html_exporter = HTMLExporter()
        html_exporter.template_file = 'basic'
        body, _ = html_exporter.from_notebook_node(nb)

        # Remove the temporary file
        if os.path.exists(full_file_name):
            os.remove(full_file_name)

        # Extract the result part of the html
        return ScriptExecutor.extract_output(body)

    @staticmethod
    def extract_output(html_string):
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
        for line in lines:
            cleaned_record += line
            cleaned_record += '\n'
        return cleaned_record
