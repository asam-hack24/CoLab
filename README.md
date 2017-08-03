# CoLab - Messaging for scientists

CoLab is Slack-like collaboration tool for scientists.
This repository contains the original concept developed at the [Hack24](http://www.hack24.co.uk/) hackathon, development of a full application is ongoing here: https://github.com/colab-chat/colab-server

Current key features:
- Persistent chat channels
- Rendered LaTeX equations
- Execution and editing of Python and R scripts
- Exporting chat history to [Jupyter](http://jupyter.org/) notebooks

The project started life as a hackathon entry to [Hack24](http://www.hack24.co.uk/) for a challenge set by [ELife](https://elife.elifesciences.org/).
We made a [YouTube video](https://youtu.be/TD3FUoyO5UY) for the hackathon entry.

## Usage

Improving usability is being worked on but the following instructions can be used to test the software in its current state.

Requires Python >3.5 and the packages listed in `requirements.txt` which can be installed with `pip` using
```
pip install -r requirements.txt
```

Username can be set [here](https://github.com/asam-hack24/CoLab/blob/master/app/userconfig.ini).
An Apache Kafka and a Zookeeper server must be running. This is very straightforward and is documented [here](https://kafka.apache.org/quickstart). The address of the Kafka broker must then be set [here](https://github.com/asam-hack24/CoLab/blob/master/app/views.py#L35).

Then run `run.py`.

## Development
CoLab is implemented in Python using the Flask framework. Some javascript is used in the front-end.
