#!/bin/bash -l

SCRIPTPATH=$(dirname $(readlink -f "$0"))
PROJECT_DIR="${SCRIPTPATH}/../../"

# conda activate loftr
export PYTHONPATH=$PROJECT_DIR:$PYTHONPATH
cd $PROJECT_DIR

data_cfg_path="configs/data/cambridge.py"
main_cfg_path="configs/neumap/cambridge_stage2.py"

n_nodes=1
n_gpus_per_node=1
torch_num_workers=12
batch_size=2
pin_memory=true
exp_name="cambridge_stage2=$(($n_gpus_per_node * $n_nodes * $batch_size))"

python -u ./train.py \
    ${data_cfg_path} \
    ${main_cfg_path} \
    --exp_name=${exp_name} \
    --gpus=${n_gpus_per_node} --num_nodes=${n_nodes} --accelerator="ddp" \
    --batch_size=${batch_size} --num_workers=${torch_num_workers} --pin_memory=${pin_memory} \
    --check_val_every_n_epoch=5 \
    --log_every_n_steps=100 \
    --limit_val_batches=1. \
    --num_sanity_val_steps=0 \
    --benchmark=True \
    --max_epochs=400 \
    --tensorboard \
    --neumap_pretrained_ckpt $MODEL_STAGE1 #replace this with models trained in the first stage