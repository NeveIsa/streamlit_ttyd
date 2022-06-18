# streamlit_ttyd

streamlit_ttyd implements a terminal plugin for streamlit using the amazing [ttyd](https://github.com/tsl0922/ttyd) project.

### Installation

`pip install git+https://github.com/NeveIsa/streamlit_ttyd`



### Usage

```python
from streamlit_ttyd import terminal

streamlit.text("Terminal showing processes running on your system using the htop command")

# start the ttyd server and display the terminal on streamlit
ttydprocess, port = terminal(cmd = "htop")

# info on ttyd port
streamlit.text(f"ttyd server is running on port : {port}")

# kill the ttyd server
ttydproc.kill()
```

> Arguments for terminal

- cmd: str -> the command to run 
- readonly: bool -> readonly terminal (default -> False)
- port: int -> port number to run the ttyd server on (default -> 0, automatically picked in the range 5000-7000)
- exit_on_disconnect -> whether to kill ttyd server when web-terminal is disconnected (default -> True)
- height: int -> height in pixels which is passed to streamlit.component.v1.iframe (default -> 500)