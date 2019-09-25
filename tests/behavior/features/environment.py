from ipdb import spost_mortem


def before_all(context):
    context.base_url = context.config.userdata.get('base_url', None)

def after_step(context, step):
    if context.config.userdata.get('debug', None) and step.status == 'failed':
        spost_mortem(step.exc_traceback)
