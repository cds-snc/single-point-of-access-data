
# coding: utf-8

# In[2]:


def exec_command(command_text):
    import subprocess
    p = subprocess.call(command_text, shell=True)
    if p == 1: raise Exception('failed command')

def convert_to_py(fname):
    """This function converts an ipython notebook to a .py file,
    removes the convert command, and copies the .py to the Anaconda
    directory where it can be imported by other notebooks.
    Don't forget to add '# end of .py file'."""
    exec_command("ipython nbconvert --to=python " + fname + ".ipynb")
    f = open(fname + '.py', 'r')
    all_lines = f.readlines()
    f.close()
    end_line_num = all_lines.index('# end of .py file\n')
    f = open(fname + '.py', 'w')
    f.writelines(all_lines[:end_line_num])
    f.close()
    
