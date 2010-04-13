from domains.djangoadmin import DjangoAdminDomain


def setup(app):
    app.add_domain(DjangoAdminDomain)
    
    