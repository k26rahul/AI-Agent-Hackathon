"""
https://fetch.ai/docs/guides/agent-courses/introductory-course#create-a-second-agent-and-start-an-interaction

https://fetch.ai/docs/guides/agents/communicating-with-other-agents

https://fetch.ai/docs/apis/agentverse/hosting
"""

from uagents import Bureau
from test_agent import test_agent
from url_shortener_agent import url_shortener_agent

bureau = Bureau()
bureau.add(test_agent)
bureau.add(url_shortener_agent)
bureau.run()
