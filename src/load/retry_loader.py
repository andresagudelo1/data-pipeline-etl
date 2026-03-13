from tenacity import retry, wait_exponential, stop_after_attempt
from .loader import load_chunk

@retry(
    wait=wait_exponential(multiplier=1, min=2, max=10),
    stop=stop_after_attempt(5)
)
def safe_load(df, engine):

    load_chunk(df, engine)