from app.script_execution.script_executor import ScriptExecutor


class PythonExecutor(ScriptExecutor):
    def execute(self, script):
        return self.do_execute(script=script, kernel='python3')
