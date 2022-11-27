

from src.config.default import _CN as cfg

cfg.TRAINER.MSLR_MILESTONES = [50, 100, 150, 200, 250, 300, 350]

cfg.TRAINER.TRUE_LR=2e-3
cfg.TRAINER.DATA_SAMPLER = 'scene_balance' 
cfg.TRAINER.N_SAMPLES_PER_SUBSET = 256
cfg.TRAINER.SCORE_THRESH=0.5
cfg.TRAINER.PRUNE_FINETUNE=True
cfg.TRAINER.PRUNE_THRESH=0.00001 # This value is not stable, please re-compute for different checkpoints

cfg.MODEL.CODE_NUM=100
cfg.MODEL.D_MODEL=256
cfg.MODEL.RESNETFPN.BLOCK_DIMS = [128, 256, 256] 
cfg.MODEL.RESNETFPN.STRIDES = [2, 2, 1] 
cfg.MODEL.RESNETFPN.INITIAL_DIM = 64
cfg.MODEL.TRANS_BLOCK_NUM=6
cfg.MODEL.BACKBONE_FREEZE=False
cfg.MODEL.RGB=True

cfg.DATASET.RANDOM_CROP=False
cfg.DATASET.RESOLUTION=480
cfg.DATASET.MAX_N_POINTS=4800
cfg.LOSS.SPARSITY_LOSS=False
