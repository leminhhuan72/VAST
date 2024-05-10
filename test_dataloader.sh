python3 -m torch.distributed.launch \
--nnodes 1 \
--node_rank 0 \
--nproc_per_node 1 \
--master_port 9834 \
./build_dataloader.py \
--config ./config/vast/finetune_cfg/VQA-msrvtt.json