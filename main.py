import argparse
import torch
import numpy as np
from data_loader import load_data
from train import train
import os
import pickle as pk

torch.cuda.set_device(3)

parser = argparse.ArgumentParser()
parser.add_argument('-d', '--dataset', type=str, default='SH_S', help='which dataset to use (music, book, movie, restaurant)')
parser.add_argument('--n_epoch', type=int, default=200, help='the number of epochs')
parser.add_argument('--batch_size', type=int, default=64, help='batch size')
parser.add_argument('--n_layer', type=int, default=3, help='depth of layer')
parser.add_argument('--lr', type=float, default=0.002, help='learning rate')
parser.add_argument('--l2_weight', type=float, default=1e-5, help='weight of the l2 regularization term')

parser.add_argument('--dim', type=int, default=64, help='dimension of entity and relation embeddings')
parser.add_argument('--user_triple_set_size', type=int, default=16, help='the number of triples in triple set of user')
parser.add_argument('--item_triple_set_size', type=int, default=16, help='the number of triples in trip e set of item')
parser.add_argument('--agg', type=str, default='concat', help='the type of aggregator (sum, pool,  concat)')

parser.add_argument('--use_cuda', type=bool, default=True, help='whether using gpu or cpu')
parser.add_argument('--show_topk', type=bool, default=False, help='whether showing topk or not')
parser.add_argument('--random_flag', type=bool, default=False, help='whether using ra ndom seed or not')

parser.add_argument('--buget_num', type=int, default=10, help='whether using random seed or not')

args = parser.parse_args()

# name = '../data/' + args.dataset + '/' + 'data_info_' + str(args.buget_num) + '_' + str(args.user_triple_set_size)+ '_' + str(args.item_triple_set_size) +'.pk'
name = '../data/' + args.dataset + '/' + 'data_info_' + str(args.buget_num) + str(args.n_layer)  +'.pk'
if not os.path.exists(name):
    data_info = load_data(args)
    with open(name, 'wb') as f:
        pk.dump(data_info, f)

with open(name, 'rb') as f:
        data_info = pk.load(f)
        print('load data_info from disk.')

train(args, data_info)
