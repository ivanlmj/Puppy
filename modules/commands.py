
import subprocess as sp

class Shell:

    def execute(self, command):
        try:
            p = sp.Popen(command, shell=True, stdout=sp.PIPE, stderr=sp.PIPE)
            output = p.communicate()[0].decode('utf-8')
            return_code = p.returncode
            return (return_code, output)
        except Exception as e:
            return (e)
