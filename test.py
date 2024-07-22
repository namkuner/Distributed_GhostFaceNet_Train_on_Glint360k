from backbones import get_model
from  eval.verification import test,load_bin
model = get_model("ghostfacenetsv2", fp16=False)
print(model)
dataset = load_bin("small_dataset/vilfw.bin", (112, 112))
# print(dataset)
acc1, std1, acc2, std2, xnorm, embeddings_list = test(
    dataset, model, 10, 10)
print(acc2)