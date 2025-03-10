from langserve import RemoteRunnable

remote_chain = RemoteRunnable("http://localhost:8000/chain/")
remote_chain.invoke({"language": "Spanish", "text": "Generative AI is a bigger opportunity than Internet"})