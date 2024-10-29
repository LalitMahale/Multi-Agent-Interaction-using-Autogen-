from autogen import ConversableAgent
import autogen
from ..configuration import config
config_list = autogen.config_list_from_json(config.CONFIG_LIST)


agent = ConversableAgent(
    name = "News collector",
    llm_config= {"config_list":config_list},
    code_execution_config=False,
    human_input_mode="NEVER",
    function_map= None
)

reply = agent.generate_reply({"content":"Who are you ?","role":"user"})

print(reply)