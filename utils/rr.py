import markdown

def read_Readme():
    with open('README.md','r', encoding='utf-8') as f:
        x = f.read()
        html = markdown.markdown(x)
    return html

