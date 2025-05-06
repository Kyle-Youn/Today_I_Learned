from fastapi import Query

# ...

async def search_for_db(
    # ...
    CustomerAge: Optional[int] = Query(
        None,
        ge=0,    # 최소 0 이상
        le=100,  # 최대 100 이하
        description="Patient age in years (0–100)"
    ),
    # ...
