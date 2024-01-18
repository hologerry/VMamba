_base_ = './tood_r50_fpn_ms-2x_coco.py'

model = dict(
    backbone=dict(
        depth=101,
        init_cfg=dict(type='Pretrained',
                      checkpoint='torchvision://resnet101')))