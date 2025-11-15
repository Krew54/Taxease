from fastapi import FastAPI
import uvicorn
from .views.user.user_auth import user_router
from .views.reviews.reviews_router import review_router
from .views.profile.profile_router import profile_router
from .views.chat.chat_router import chat_router


app = FastAPI(
    docs_url="/docs",
    redoc_url="/redocs",
    title="TaxFix NG",
    description="TaxFix NG is a tax filing application that helps users to file their taxes easily and efficiently.",
    version="1.0",
    contact={
        "Name": "TaxFixNG",
        "website": "www.taxfixng.com",
        "email": "info@taxfixng.com",
        "Phone":"08033796049",
    }
)


app.include_router(user_router)
app.include_router(profile_router)
app.include_router(documentation_router)
app.include_router(tax_compute_router)

if __name__ == "__main__":
    uvicorn.run("app.runner:app", host="0.0.0.0", port=8000, reload=True)