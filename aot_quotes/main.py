from fastapi import FastAPI

from aot_quotes.core.quote.views import router as get
from starlette.responses import RedirectResponse

app = FastAPI(title="Attack on Titan - Quotes API", docs_url="/", redoc_url=None)

app.include_router(get, prefix="/random")