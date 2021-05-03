import markdown

def read_Readme():
    with open('README.md','r', encoding='utf-8') as f:
        x = f.read()
        html = markdown.markdown(x)
    return html

def auto_Render():
    with open('./utils/cr.py') as f:
        x = f.read()
        html = "<pre><code class='python'>"+x+"</pre></code>"
    return html
        
