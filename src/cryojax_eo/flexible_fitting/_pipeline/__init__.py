try:
    from .flexible_fitting_openmm import (
        FlexibleFittingPipeline as FlexibleFittingPipeline,
    )
except (ImportError, AttributeError):
    pass
