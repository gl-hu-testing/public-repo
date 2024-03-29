"""Contains routing for CHA₂DS₂-VASc score calculator."""
from fastapi import APIRouter, Depends

from src.chads_vasc_score.schemas import ChadsVascScore
from src.chads_vasc_score.utils import unpack_and_calc_cvs
from src.config import settings, Settings
router = APIRouter()


@router.post(
    "/",
    status_code=200,
    name="CHA₂DS₂-VASc Score Calculator",
    description="Calculates CHA₂DS₂-VASc score based on input parameters.",
    response_model=ChadsVascScore,
)
async def index(score: int = Depends(unpack_and_calc_cvs)) -> ChadsVascScore:
    """Calculates CHA₂DS₂-VASc score based on input parameters.

    Args:
        score: Input parameters with `ChadsVascInput` data attributes.

    Returns:
        CHA₂DS₂-VASc score.
    """
    return ChadsVascScore(score=score)


@router.post(
    "/settings",
    status_code=200,
    name="Settings dump",
    description="test settings dump.",
)
async def test_settings() -> Settings:
    """Test dump settings.

    Returns:
        Settingso bject.
    """
    return settings.dict()
