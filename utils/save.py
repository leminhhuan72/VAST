import os
import torch
from os.path import join
from utils.logger import LOGGER




class ModelSaver(object):
    def __init__(self, output_dir, prefix='model_step', suffix='pt',remove_before_ckpt=True):
        self.output_dir = output_dir
        self.prefix = prefix
        self.suffix = suffix
        self.remove_before_ckpt = remove_before_ckpt
    def save(self, model, step, optimizer=None, best_indicator=None, save_best=False):
        ###remove previous model
        previous_state = [i  for i in os.listdir(self.output_dir) if i.startswith('model')]
        # if not self.pretraining:
        if self.remove_before_ckpt:
            for p in previous_state:
                os.remove(os.path.join(self.output_dir,p))
        output_model_file = join(self.output_dir,
                                 f"{self.prefix}_{step}.{self.suffix}")
        state_dict = {k: v.cpu() if isinstance(v, torch.Tensor) else v
                      for k, v in model.state_dict().items()}
        torch.save(state_dict, output_model_file)

        if save_best:
            for k in best_indicator:
                if best_indicator[k]:
                    torch.save(state_dict, join(self.output_dir,
                                 f"best_{k}.{self.suffix}"))

        if optimizer is not None:
            if hasattr(optimizer, '_amp_stash'):
                pass  # TODO fp16 optimizer
            previous_state = [i  for i in os.listdir(self.output_dir) if i.startswith('optimizer')]
            if self.remove_before_ckpt:
                for p in previous_state:
                    os.remove(os.path.join(self.output_dir,p))
            torch.save(optimizer.state_dict(), f'{self.output_dir}/optimizer_step_{step}.pt')
