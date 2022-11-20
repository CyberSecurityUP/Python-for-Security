from pywebcopy import save_webpage

kwargs = {'project_name': 'uniciv site'}

save_webpage(
    url='https://desecsecurity.com/',
    project_folder='pycopy/',
    **kwargs
    )
