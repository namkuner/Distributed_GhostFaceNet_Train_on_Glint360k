from backbones import get_model
from eval.verification import test

backbone = get_model(
    "ghostfacenetsv2", image_size=112, width=1.3, dropout=0.1, fp16=True).cuda()
    # test("")