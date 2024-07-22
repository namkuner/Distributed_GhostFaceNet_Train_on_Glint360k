from easydict import EasyDict as edict

config = edict()

#Train
config.batch_size = 128

#dataset
config.rec = "ms1-mv3-asian-face"
config.num_classes = 6579
config.num_image = 300000
config.num_epoch = 30
config.warmup_epoch = 0
config.val_targets =['lfw', 'cfp_fp', "agedb_30","vilfw"]
config.seed = 2048
# Margin Base Softmax
config.margin_list = (1.0, 0.5, 0.0)
config.optimizer = "sgd"
config.lr = 0.1
config.momentum = 0.9
config.weight_decay = 5e-4
config.num_workers = 2 #dataloader num_worker
#Model
config.network = "ghostfacenetsv2"
config.IMAGE_SIZE = 112
config.drop_out = 0.1
config.width = 1.3
config.embedding_size = 512
config.fp16 = True

#Resume
config.resume = False
config.checkpoint = 0
# WandB Logger
config.wandb_key = "daa38a012f1993bc802203d31f828a53c6605938"
config.suffix_run_name = None
config.using_wandb = True
config.wandb_entity = "namkunerr"
config.wandb_project = "GhostFaceNets on Asian and MS1MV3 Dataset"
config.wandb_log_all = True
config.save_artifacts = True
config.wandb_resume = "allow" # resume wandb run: Only if the you wand t resume the last run that it was interrupted
config.wandb_id = "bdx6o42y"
config.notes ="namkuner"
# Partial FC
config.sample_rate = 1
config.interclass_filtering_threshold = 0

#Logging
config.save_all_states = True
config.output = "ms1mv3_asian_arcface_ghostfacenets"
config.verbose = 2000
config.frequent = 10

# Gradient ACC
config.gradient_acc = 1



