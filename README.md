# streamlit_ttyd

streamlit_ttyd implements a terminal plugin for streamlit using the amazing [ttyd](https://github.com/tsl0922/ttyd) project.

### Installation

pip install git+https://github.com/NeveIsa/streamlit_ttyd



### Usage

```python
from streamlit_ttyd import terminal

streamlit.text("Terminal showing processes running on your system using the htop command")

ttydprocess, port = terminal(cmd = "htop",
                             readonly = True,
                            exit_on_disconnect = True,
                            height = 500)

streamlit.text(f"ttyd server is running on port : {port}")

```


> Arguments for terminal

- cmd: str -> the command to run
- readonly: bool -> readonly terminal
- port: int -> port number to run the ttyd server on
- exit_on_disconnect -> whether to kill ttyd server when web-terminal is disconnected
- height: int -> height in pixels which is passed to streamlit.component.v1.iframe