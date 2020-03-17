---
name: Bug report
about: Create a report to help us improve
title: ''
labels: ''
assignees: ''
---

### Description of the Bug

Your text


### Code and Logs

```python
from kivy.app import App
from kivy.lang import Builder

kv = """
Screen:
    # KV-Code
"""


class MainApp(App):
    def build(self):
        self.root = Builder.load_string(kv)


if __name__ == '__main__':
    MainApp().run()
```


### Screenshots

Add images to explain us this bug. Paste urls here.

Remove this section if no images here


### Versions

* OS: 
* Python: 
* Kivy: 
* KivyMD: 
