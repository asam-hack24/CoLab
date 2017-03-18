from app.script_execution.script_executor import ScriptExecutor


class PythonExecutor(ScriptExecutor):
    def execute(self, script):
        self.do_execute(script=script, kernel='python3')
