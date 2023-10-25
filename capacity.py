from autogen import AssistantAgent, UserProxyAgent, GroupChat, GroupChatManager, config_list_from_json

config_list = config_list_from_json(env_or_file="OAI_CONFIG_LIST")
llm_config = {"config_list": config_list, "seed": 42, "request_timeout": 120}

user_proxy = UserProxyAgent(
    name="user_proxy",
    system_message="A human user.",
    code_execution_config={"last_n_messages": 2, "work_dir": "code"},
    human_input_mode="ALWAYS"
)

analyst = AssistantAgent(
    name="people_analyst",
    system_message="Use data to build people analytics projections",
    llm_config=llm_config
)

recruiter = AssistantAgent(
    name="recruiting_leader",
    system_message="Incorporate recruiting experience into the planning cycle",
    llm_config=llm_config
)

groupchat = GroupChat(
    agents=[user_proxy, analyst, recruiter], messages=[]
)
manager = GroupChatManager(groupchat=groupchat, llm_config=llm_config)

user_proxy.initiate_chat(manager, message="Design a recruiting capacity plan for 2024")