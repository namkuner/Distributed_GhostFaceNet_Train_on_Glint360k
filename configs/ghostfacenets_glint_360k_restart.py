from easydict import EasyDict as edict

config = edict()

#Train
config.batch_size = 128

#dataset
config.rec = "glint360k"
config.num_classes = 360232
config.num_image = 17091657
config.num_epoch = 20
config.warmup_epoch = 0
config.val_targets =['lfw', 'cfp_fp','agedb_30']
config.seed = 2048
# Margin Base Softmax
config.margin_list = [1.0, 0.0, 0.4]
config.optimizer = "sgd"
config.lr = 0.1
config.momentum = 0.9
config.weight_decay = 1e-4
config.num_workers = 6 #dataloader num_worker
#Model
config.network = "ghostfacenetsv2"
config.IMAGE_SIZE = 112
config.drop_out = 0.0
config.width = 1.3
config.embedding_size = 512
config.fp16 = True

#Resume
config.resume = True
config.checkpoint = 0
# WandB Logger
config.wandb_key = "daa38a012f1993bc802203d31f828a53c6605938"
config.suffix_run_name = None
config.using_wandb = True
config.wandb_entity = "namkunerr"
config.wandb_project = "Glint_360k"
config.wandb_log_all = False
config.save_artifacts = True
config.wandb_resume = "must" # resume wandb run: Only if the you wand t resume the last run that it was interrupted
config.wandb_id = "db6bngah"
config.notes ="namkuner"
# Partial FC
config.sample_rate = 1
config.interclass_filtering_threshold = 0

#Logging
config.save_all_states = True
config.output = "glint"
config.verbose = 2000
config.frequent = 10

# Gradient ACC
config.gradient_acc = 1



