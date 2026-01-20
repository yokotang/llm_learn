from langchain_openai import OpenAI
from langchain_openai import ChatOpenAI

#补全模型
# llm=OpenAI(
#     openai_api_key="08558d65eebd077d79c86050cad45418:MDFiNGJmNjcyOThjOWI3N2NkOTliZDMw",
#     base_url="https://maas-api.cn-huabei-1.xf-yun.com/v2",
#     model="xop3qwen1b7",
#     timeout=30,
#     max_retries=2,
# )
#对话模型
chatmodel=ChatOpenAI(
    openai_api_key="08558d65eebd077d79c86050cad45418:MDFiNGJmNjcyOThjOWI3N2NkOTliZDMw",
    base_url="https://maas-api.cn-huabei-1.xf-yun.com/v2",
    model="xop3qwen1b7",
    timeout=30,
    max_retries=2,
)
# print(llm.invoke("你好"))
print("------------------------")
print(chatmodel.invoke("之前买基金被套了，在商业航天和ai软件我该如何解套，后续走势是怎么样"))
