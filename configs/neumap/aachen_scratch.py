from src.config.default import _CN as cfg

cfg.TRAINER.MSLR_MILESTONES = [30, 60, 90, 120, 150, 180]

cfg.TRAINER.TRUE_LR=2e-3
cfg.TRAINER.DATA_SAMPLER = 'scene_balance' 

cfg.MODEL.CODE_NUM=100
cfg.MODEL.D_MODEL=256
cfg.MODEL.RESNETFPN.BLOCK_DIMS = [128, 196, 256] 
cfg.MODEL.RESNETFPN.INITIAL_DIM = 128
cfg.MODEL.TRANS_BLOCK_NUM=6
cfg.MODEL.BACKBONE_FREEZE=True
cfg.MODEL.N_SAMPLE_POINTS = 1000
cfg.MODEL.N_SAMPLE_IN_VOXEL_POINTS = 500

cfg.LOSS.SPARSITY_LOSS=True