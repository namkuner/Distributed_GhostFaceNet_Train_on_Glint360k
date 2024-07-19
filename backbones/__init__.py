from .ghostfacenetsv2 import GhostFaceNetsV2
def get_model(name, **kwargs):
    if name == "ghostfacenetsv2":
        return GhostFaceNetsV2(**kwargs)
    else:
        ValueError()