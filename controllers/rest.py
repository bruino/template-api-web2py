from pydal.restapi import RestAPI, Policy

policy = Policy()
policy.set('superhero', 'GET', authorize=True, allowed_patterns=['*'])
#policy.set('*', 'GET', authorize=True, allowed_patterns=['*'])
policy.set('*', 'PUT', authorize=False)
policy.set('*', 'POST', authorize=False)
policy.set('*', 'DELETE', authorize=False)

def api():
    return RestAPI(db, policy)(request.method, 
                               request.args(0), # tablename
                               request.args(1), # id
                               request.get_vars, 
                               request.post_vars) 