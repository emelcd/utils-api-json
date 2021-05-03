import markdown

def read_Readme():
    with open('README.md','r', encoding='utf-8') as f:
        x = f.read()
        html = markdown.markdown(x)
    return html

def auto_Render(fp):
    fp = './utils/'+fp+".py"
    with open(fp) as f:
        x = f.read()
        html = f"<pre><code class='python'>"+x+"</pre></code>"
    return html
        
