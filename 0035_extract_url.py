def domain_name(url):
    for i in ["http://", "https://", "www."]:
        if i in url:
            url = url.replace(i,"")
    return url[:url.index(".")]
print(domain_name("http://www.zombie-bites.com"))
