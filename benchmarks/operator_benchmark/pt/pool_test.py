from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals


import operator_benchmark as op_bench
import torch
import torch.nn as nn


"""
Microbenchmarks for MaxPool1d and AvgPool1d operators.
"""


# Configs for pool-1d ops
pool_1d_configs = op_bench.config_list(
    attr_names=[
        "kernel", "stride", "N", "C", "L"
    ],
    attrs=[
        [3, 1, 1, 3, 32],
        [3, 2, 8, 3, 128],
        [3, 2, 16, 3, 256],
    ],
    tags=["short"]
)


pool_1d_ops_list = op_bench.op_list(
    attr_names=["op_name", "op"],
    attrs=[
        ["MaxPool1d", nn.MaxPool1d],
        ["AvgPool1d", nn.AvgPool1d],
    ],
)


class Pool1dBenchmark(op_bench.TorchBenchmarkBase):
    def init(self, kernel, stride, N, C, L):
        self.input = torch.rand(N, C, L) 
        self.kernel = kernel
        self.stride = stride

    def set_op(self, op):
        self.op = op(self.kernel, stride=self.stride)

    def forward(self):
        return self.op(self.input)


op_bench.generate_pt_tests_from_list(pool_1d_ops_list, pool_1d_configs, Pool1dBenchmark)


"""
Microbenchmarks for MaxPool2d and AvgPool2d operators.
"""


# Configs for pool-2d ops
pool_2d_configs = op_bench.config_list(
    attr_names=[
        "kernel", "stride", "N", "C", "H", "W"
    ],
    attrs=[
        [[3, 1], [2, 1], 1, 16, 32, 32],
        [[3, 2], [2, 2], 8, 32, 64, 64],
        [[3, 3], [2, 2], 16, 32, 64, 64],
    ],
    tags=["short"]
)


pool_2d_ops_list = op_bench.op_list(
    attr_names=["op_name", "op"],
    attrs=[
        ["MaxPool2d", nn.MaxPool2d],
        ["AvgPool2d", nn.AvgPool2d],
    ],
)


class Pool2dBenchmark(op_bench.TorchBenchmarkBase):
    def init(self, kernel, stride, N, C, H, W):
        self.input = torch.rand(N, C, H, W) 
        self.kernel = kernel
        self.stride = stride

    def set_op(self, op):
        self.op = op(self.kernel, stride=self.stride)

    def forward(self):
        return self.op(self.input)


op_bench.generate_pt_tests_from_list(pool_2d_ops_list, pool_2d_configs, Pool2dBenchmark)


"""
Microbenchmarks for MaxPool3d and AvgPool3d operators.
"""


# Configs for pool-3d ops
pool_3d_configs = op_bench.config_list(
    attr_names=[
        "kernel", "stride", "N", "C", "D", "H", "W"
    ],
    attrs=[
        [[3, 1, 3], [2, 1, 2], 1, 16, 16, 32, 32],
        [[3, 2, 3], [2, 2, 2], 8, 32, 32, 64, 64],
        [[3, 3, 3], [2, 2, 2], 16, 32, 32, 64, 64],
    ],
    tags=["short"]
)


pool_3d_ops_list = op_bench.op_list(
    attr_names=["op_name", "op"],
    attrs=[
        ["MaxPool3d", nn.MaxPool3d],
        ["AvgPool3d", nn.AvgPool3d],
    ],
)


class Pool3dBenchmark(op_bench.TorchBenchmarkBase):
    def init(self, kernel, stride, N, C, D, H, W):
        self.input = torch.rand(N, C, D, H, W) 
        self.kernel = kernel
        self.stride = stride

    def set_op(self, op):
        self.op = op(self.kernel, stride=self.stride)

    def forward(self):
        return self.op(self.input)


op_bench.generate_pt_tests_from_list(pool_3d_ops_list, pool_3d_configs, Pool3dBenchmark)


if __name__ == "__main__":
    op_bench.benchmark_runner.main()
