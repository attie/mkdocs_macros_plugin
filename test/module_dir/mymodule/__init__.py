import os




def define_env(env):
    """
    This is the hook for the functions (new form)
    """

    env.variables.cwd = os.getcwd()

    # use dot notation for adding
    env.variables.baz = env.variables.fix_url('foo')



    # Optional: a special function for making relative urls point to root
    fix_url = env.variables.fix_url

    @env.macro
    def button(label, url):
        "Add a button"
        url = fix_url(url)
        HTML = """<a class='md-button' href="%s">%s</a>"""
        return HTML % (url, label)

    
    env.variables.special_docs_dir = env.variables.config['docs_dir']