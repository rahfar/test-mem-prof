# Tensorflow 2.13 memory leak

To reproduce:

1. install [uv](https://docs.astral.sh/uv/getting-started/installation/)
2. `uv sync`
3. run server `mprof run python main.py`
4. run client `python api-client.py`
5. stop server and run `mprof plot -o output` to get png
