### 

def build_profile(first, last, **user_info):
    """Controi um dicionario com tudo o que sabemos do usuario"""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in profile.items():
        profile[key] = value
        