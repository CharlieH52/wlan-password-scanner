import subprocess

class CommandProcessor:
    def __init__(self, command: list[str]):
        self.command = command
        
    def __execute_command(self) -> subprocess.CompletedProcess[str]:
        return subprocess.run(self.command, capture_output=True, text=True)
    
    def stdout_to_list(self) -> list[str]:
        cmd_output = self.__execute_command().stdout.split('\n')
        return cmd_output