from fastapi import APIRouter, Depends

from ..dependencies import farmer_required

router = APIRouter(
    prefix="/farmer",
    tags=["Farmer"]
)


@router.get("/dashboard")
def farmer_dashboard(current_user=Depends(farmer_required)):
    return {
        "message": f"Welcome Farmer {current_user['sub']}",
        "role": current_user["role"]
    }