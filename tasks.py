from atelier.tasks import *
env.setup_from_tasks(globals(), "lino_presto")

env.locale_dir = 'lino_presto/lib/presto/locale'
env.languages = "en de fr et".split()
# env.tolerate_sphinx_warnings = True

env.add_demo_project('lino_presto.projects.std.settings.demo')

env.revision_control_system = 'git'

env.cleanable_files = ['docs/api/lino_presto.*']
